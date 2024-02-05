import { API_ENDPOINT } from "$lib/config"; // this should be a secret

export async function load({ params, fetch }) {
	const volunteer_res = await fetch(API_ENDPOINT + "volunteers/" + params.slug);
	const events_res = await fetch(API_ENDPOINT + "volunteers/" + params.slug + "/events");
	const volunteer = await volunteer_res.json();
	const events = await events_res.json();
	const event_list = events.events;
	const hours = events.hours;
	return {
		volunteer,
		event_list,
		hours
	};
}
