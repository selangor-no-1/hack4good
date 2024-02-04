import { API_ENDPOINT } from "$lib/config"; // this should be a secret

export async function load({ fetch }) {
	const res = await fetch(API_ENDPOINT + "events");
	const events = await res.json();
	return {
		events,
	};
}
