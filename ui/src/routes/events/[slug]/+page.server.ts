import { API_ENDPOINT } from "$lib/config";
import { EVENTS } from "$lib/mockData";

export const load = async ({ params, fetch }) => {
	const res = await fetch(API_ENDPOINT + "volunteers");
  const volunteers = await res.json();
	const currentEvent = EVENTS.filter(
		(event) => event.id.toString() === params.slug
	)?.[0];
	return {
		event: currentEvent,
		volunteers: volunteers
	};
};
