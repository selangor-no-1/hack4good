import { API_ENDPOINT } from "$lib/config"; // this should be a secret

export async function load({ params, fetch }) {
	const res = await fetch(API_ENDPOINT + "volunteers/" + params.slug);
	console.log(params.slug);
	const volunteer = await res.json();
	return {
		volunteer,
	};
}
