import { superValidate } from "sveltekit-superforms/server";
import { formSchema } from "./(utils)/schema";
import { fail, redirect } from "@sveltejs/kit";
import { API_ENDPOINT } from "$env/static/private";
import { createISOString } from "$lib/utils";
import type { Event } from "$lib/types";

export const load = async () => {
	return {
		form: await superValidate(formSchema),
	};
};
export const actions = {
	default: async ({ request, fetch }) => {
		const formData = await request.formData();
		const form = await superValidate(formData, formSchema);
		if (!form.valid) {
			return fail(400, {
				form,
			});
		}

		// post-process the start and end time to actual datetime string
		const date = formData.get("date") as string;
		const startTime = formData.get("startTime") as string;
		const endTime = formData.get("endTime") as string;
		const isoStartTime = createISOString(date, startTime);
		const isoEndTime = createISOString(date, endTime);

		const data = {
			name: formData.get("eventName"),
			location: formData.get("location"),
			description: formData.get("description"),
			image: formData.get("image"),
			date: date,
			start_time: isoStartTime,
			end_time: isoEndTime,
		};

		async function createEvent() {
			const resp = await fetch(API_ENDPOINT + "events/", {
				method: "POST",
				body: JSON.stringify(data),
			});

			if (!resp.ok) {
				throw new Error("Check that the API server is running!");
			}

			const event = (await resp.json()) as Event;

			return event.slug;
		}

		const slug = await createEvent();
		redirect(303, `/events/${slug}`);
	},
};
