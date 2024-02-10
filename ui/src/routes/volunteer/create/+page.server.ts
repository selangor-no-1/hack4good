import { superValidate } from "sveltekit-superforms/server";
import { formSchema } from "./(utils)/schema.js";
import { fail, redirect } from "@sveltejs/kit";
import { API_ENDPOINT } from "$env/static/private";
import type { Volunteer } from "$lib/types";
import axios from "axios";

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
			try {
				const resp = await axios.post(API_ENDPOINT + "volunteers/", data);
				const volunteer = resp.data as Volunteer;
				return volunteer.id;
			} catch (err) {
				throw new Error("Check that the API server is running!");
			}
		}

		const _ = await createEvent();
		redirect(303, `/volunteer`);
	},
};
