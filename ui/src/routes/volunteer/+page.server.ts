import { API_ENDPOINT } from "$lib/config"; // this should be a secret

export async function load({ fetch }) {
	const res = await fetch(API_ENDPOINT + "volunteers");
	const volunteers = await res.json();
	return {
		volunteers,
	};
}