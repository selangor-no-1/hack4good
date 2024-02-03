import type { User } from "$lib/types";

export async function load({ fetch }) {
	// define some helpers
	async function fetchUsers() {
		const result = await fetch(
			"https://dummyjson.com/users?select=age,firstName,lastName,weight,height&limit=10"
		);
		const { users }: { users: User[] } = await result.json();
		return users;
	}
	return {
		users: await fetchUsers(),
	};
}
