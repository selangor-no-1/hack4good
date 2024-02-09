import { API_ENDPOINT } from "$env/static/private";
import type { Event, Volunteer, Response } from "$lib/types";
import { parseGoogleFormID } from "$lib/utils.js";
import { fail } from "@sveltejs/kit";

export const load = async ({ fetch, params }) => {
	async function getEventDetails(slug: string) {
		const res = await fetch(API_ENDPOINT + `events/${slug}`);
		const event = await res.json();
		return event as Event;
	}

	async function getEventVolunteers(slug: string) {
		const res = await fetch(API_ENDPOINT + `events/${slug}/volunteers`);
		const volunteers = await res.json();
		return volunteers as Volunteer[];
	}

	async function getAllVolunteers() {
		const res = await fetch(API_ENDPOINT + `volunteers`);
		const volunteers = await res.json();
		return volunteers as Volunteer[];
	}

	async function getEventFormResponses(slug: string) {
		const res = await fetch(API_ENDPOINT + `responses/${slug}`);
		const responses = await res.json();
		return responses as Response[];
	}

	const [event, eventVolunteers, allVolunteers, responses] = await Promise.all([
		getEventDetails(params.slug),
		getEventVolunteers(params.slug),
		getAllVolunteers(),
		getEventFormResponses(params.slug),
	]);

	return { event, eventVolunteers, allVolunteers, responses };
};

export const actions = {
	subscribe: async ({ request }) => {
		const data = await request.formData();
		const eventSlug = data.get("eventSlug") as string;
		const googleFormURL = data.get("url") as string;
		const googleFormID = parseGoogleFormID(googleFormURL);

		if (!googleFormID) {
			return fail(400, {
				status: "Could not parse the Google Form ID from URL!",
			});
		}

		// update the Event.google_form_url field
		const event_req = await fetch(API_ENDPOINT + `events/${eventSlug}`, {
			method: "POST",
			body: JSON.stringify({
				google_form_url: googleFormURL,
			}),
		});

		if (!event_req.ok) {
			return fail(400, {
				status: "Failed to update Event with the Google Form URL",
			});
		}

		// call to get process the google form
		const ai_req = await fetch(
			API_ENDPOINT + `forms/ai/${eventSlug}/${googleFormID}`
		);

		if (!ai_req.ok) {
			return fail(400, {
				status: "AI Processing failed",
			});
		}

		return { status: "success" };
	},

	add: async ({ request }) => {
		const data = await request.formData();
		const eventSlug = data.get("eventSlug") as string;
		const volunteerId = data.get("volunteer") as string;

		const resp = await fetch(
			API_ENDPOINT +
				`events/${eventSlug}/volunteers?volunteer_id=${volunteerId}`,
			{
				method: "POST",
			}
		);

		if (!resp.ok) {
			return fail(400, {
				status: "Failed to add volunteer to event",
			});
		}
	},
};
