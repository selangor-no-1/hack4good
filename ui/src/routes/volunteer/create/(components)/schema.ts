import { z } from "zod";
export const formSchema = z.object({
  name: z.string().min(2).max(50),

  email: z.string().email(),

  date_of_birth: z.string()
  .refine((v) => v, { message: "A date of birth is required." }),

  contact_number: z.string().refine((value) => /^\d{8}$/.test(value), {
    message: "Mobile number must be 8 digits.",
  }),
});
export type FormSchema = typeof formSchema;