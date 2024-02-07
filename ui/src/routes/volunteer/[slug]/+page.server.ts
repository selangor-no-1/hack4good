import { API_ENDPOINT } from "$lib/config"; // this should be a secret

export async function load({ params, fetch }) {
	async function fetchVolunteerEvents(slug: string) {
		const events_res = await fetch(
			API_ENDPOINT + "volunteers/" + slug + "/events"
		);
		const events = await events_res.json();
		return events;
	}
	async function fetchVolunteer(slug: string) {
		const volunteer_res = await fetch(API_ENDPOINT + "volunteers/" + slug);
		const volunteer = await volunteer_res.json();
		return volunteer;
	}

	const [events, volunteer] = await Promise.all([
		fetchVolunteerEvents(params.slug),
		fetchVolunteer(params.slug),
	]);
	const event_list = events.events;
	const hours = events.hours;
	return {
		volunteer,
		event_list,
		hours,
	};
}
