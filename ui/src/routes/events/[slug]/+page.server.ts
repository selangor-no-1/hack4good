import { EVENTS } from "$lib/mockData";

export const load = ({ params }) => {
    return {
        events: EVENTS,
        slug: params.slug
    }
}