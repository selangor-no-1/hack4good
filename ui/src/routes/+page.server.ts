import type { Timeseries, User } from "$lib/types";
import { API_ENDPOINT } from "$lib/config";

export async function load({ fetch }) {
	async function fetchUsers() {
		const result = await fetch(
			"https://dummyjson.com/users?select=age,firstName,lastName,weight,height&limit=10"
		);
		const { users }: { users: User[] } = await result.json();
		return users;
	}

	async function fetchManhours() {
		const result = await fetch(API_ENDPOINT + "analytics/manhours");
		return (await result.json()) as Timeseries[];
	}

	async function fetchUniqueVolunteers() {
		const result = await fetch(API_ENDPOINT + "analytics/volunteers");
		return (await result.json()) as { unique_volunteers: number };
	}

	const [manhours, volunteers] = await Promise.all([
		fetchManhours(),
		fetchUniqueVolunteers(),
	]);

	return {
		users: fetchUsers(),
		volunteers: volunteers,
		manhoursTimeseries: manhours,
	};
}
