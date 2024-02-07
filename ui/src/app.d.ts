// See https://kit.svelte.dev/docs/types#app

import type { Volunteer, Event } from "$lib/types";

// for information about these interfaces
declare global {
	namespace App {
		// interface Error {}
		// interface Locals {}
		// interface PageData {}
		interface PageState {
			profileData: {
				volunteer: Volunteer;
				// blasphemy!
				event_list: any;
				hours: number;
			};
		}
		// interface Platform {}
	}
}

export {};
