import { z } from "zod";

export const formSchema = z.object({
	name: z
		.string()
		.refine((v) => v, { message: "Name is required!" }),
	date_of_birth: z.string().refine((v) => v, { message: "Date Of Birth is required" }),
	email: z.string().email("This is not a valid email!"),
	contact_number: z.string().length(8, { message: 'Contact number must be 8 characters long' })
});

export type FormSchema = typeof formSchema;