import { superValidate } from "sveltekit-superforms/server";
import { formSchema } from "./(utils)/schema.js";
import { fail, redirect } from "@sveltejs/kit";
import { API_ENDPOINT } from "$lib/config";
import type { Volunteer } from "$lib/types";

export const load = async () => {
	return {
		form: await superValidate(formSchema),
	};
};
export const actions = {
	default: async ({ request, fetch }) => {
		const formData = await request.formData();
		const form = await superValidate(formData, formSchema);
		if (!form.valid) {
			return fail(400, {
				form,
			});
		}

		const date_of_birth = formData.get("date_of_birth") as string;

		const data = {
			name: formData.get("name"),
			email: formData.get("email"),
			contact_number: formData.get("contact_number"),
			date_of_birth: date_of_birth,
		};

		async function createEvent() {
			const resp = await fetch(API_ENDPOINT + "volunteers/", {
				method: "POST",
				body: JSON.stringify(data),
			});

			if (!resp.ok) {
				throw new Error("Check that the API server is running!");
			}

			const volunteer = (await resp.json()) as Volunteer;

			return volunteer.id;
		}

		const id = await createEvent();
		redirect(303, `/volunteer`);
	},
};
