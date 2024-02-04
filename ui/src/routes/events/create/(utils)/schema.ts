import { z } from "zod";

function isTimeString(value: string): boolean {
	const regex = /^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$/;
	return regex.test(value);
}

export const formSchema = z.object({
	eventName: z
		.string()
		.refine((v) => v, { message: "Event Name is required!" }),
	description: z.string(),
	location: z.string(),
	image: z.string(),
	date: z.string().refine((v) => v, { message: "A date is required" }),
	startTime: z.string().refine((value) => isTimeString(value), {
		message: "Time must be HH:MM",
	}),
	endTime: z.string().refine((value) => isTimeString(value), {
		message: "Time must be HH:MM",
	}),
});

export type FormSchema = typeof formSchema;
