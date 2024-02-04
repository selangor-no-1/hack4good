import { API_ENDPOINT } from "$lib/config";

export const load = async ({ fetch, params }) => {
	async function getEventDetails(slug: string) {
		const res = await fetch(API_ENDPOINT + `events/${slug}`);
		const event = await res.json();
		return event;
	}

	async function getEventVolunteers(slug: string) {
		const res = await fetch(API_ENDPOINT + `events/${slug}/volunteers`);
		const volunteers = await res.json();
		return volunteers;
	}

	const [event, volunteers] = await Promise.all([
		getEventDetails(params.slug),
		getEventVolunteers(params.slug),
	]);

	return { event, volunteers };
};
