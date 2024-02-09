import type { Timeseries, Volunteer } from "$lib/types";
import { API_ENDPOINT } from "$env/static/private";

export async function load({ fetch }) {
	async function fetchVolunteers() {
		const result = await fetch(API_ENDPOINT + "volunteers");
		return (await result.json()) as Volunteer[];
	}

	async function fetchManhours() {
		const result = await fetch(API_ENDPOINT + "analytics/manhours");
		return (await result.json()) as Timeseries[];
	}

	async function fetchAvgSatisfaction() {
		const result = await fetch(API_ENDPOINT + "analytics/satisfaction");
		return (await result.json()) as Timeseries[];
	}

	const [manhours, volunteers, satisfaction] = await Promise.all([
		fetchManhours(),
		fetchVolunteers(),
		fetchAvgSatisfaction(),
	]);

	return {
		volunteers: volunteers,
		manhoursTimeseries: manhours,
		satisfactionTimeseries: satisfaction,
	};
}
