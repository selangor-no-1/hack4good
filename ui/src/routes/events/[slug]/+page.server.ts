import { EVENTS } from "$lib/mockData";

export const load = ({ params }) => {
	const currentEvent = EVENTS.filter(
		(event) => event.id.toString() === params.slug
	)?.[0];
	return {
		event: currentEvent,
	};
};
