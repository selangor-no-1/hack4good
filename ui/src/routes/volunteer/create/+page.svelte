<script lang="ts">
  import { page } from "$app/stores";
  import { formSchema, type FormSchema } from "./(utils)/schema";
  import type { SuperValidated } from "sveltekit-superforms";
  import { Calendar as CalendarIcon } from "lucide-svelte";
  import {
    type DateValue,
    DateFormatter,
    getLocalTimeZone,
    parseDate,
    CalendarDate,
    today,
  } from "@internationalized/date";
  import { cn } from "$lib/utils";
  import { buttonVariants } from "$lib/components/ui/button";
  import { Calendar } from "$lib/components/ui/calendar";
  import { superForm } from "sveltekit-superforms/client";
  import * as Popover from "$lib/components/ui/popover";
  import * as Form from "$lib/components/ui/form";

  export let form: SuperValidated<FormSchema> = $page.data.datePicker;

  const theForm = superForm(form, {
    validators: formSchema,
  });
  const { form: formStore } = theForm;

  const df = new DateFormatter("en-US", {
    dateStyle: "long",
  });

  let value: DateValue | undefined = $formStore.date_of_birth
    ? parseDate($formStore.date_of_birth)
    : undefined;

  let placeholder: DateValue = today(getLocalTimeZone());
</script>

<div class="container">
  <h1 class="text-2xl font-semibold mb-3">Volunteer Registration</h1>
  <Form.Root
    method="POST"
    schema={formSchema}
    controlled
    form={theForm}
    let:config
  >
    <Form.Field {config} name="name">
      <Form.Item>
        <Form.Label>Name</Form.Label>
        <Form.Input
          type="text"
          id="name"
          name="name"
          bind:value={$formStore.name}
        />
        <Form.Validation />
      </Form.Item>
    </Form.Field>
    <Form.Field {config} name="email">
      <Form.Item>
        <Form.Label>Email</Form.Label>
        <Form.Input
          type="text"
          id="email"
          name="email"
          bind:value={$formStore.email}
        />
        <Form.Validation />
      </Form.Item>
    </Form.Field>
    <Form.Field {config} name="contact_number">
      <Form.Item>
        <Form.Label>Contact number</Form.Label>
        <Form.Input
          type="text"
          id="contact_number"
          name="contact_number"
          bind:value={$formStore.contact_number}
        />
        <Form.Validation />
      </Form.Item>
    </Form.Field>
    <!-- Add profile image link in database -->
    <!-- <Form.Field {config} name="image">
			<Form.Item>
				<Form.Label>Image Link</Form.Label>
				<Form.Input
					type="text"
					id="image"
					name="image"
					bind:value={$formStore.image}
				/>
				<Form.Validation />
			</Form.Item>
		</Form.Field> -->
    <Form.Field {config} name="date_of_birth">
      <Form.Item class="flex flex-col">
        <Form.Label for="date_of_birth" class="mb-2">Date Of Birth</Form.Label>
        <Popover.Root>
          <Form.Control id="date_of_birth" let:attrs>
            <Popover.Trigger
              id="date_of_birth"
              {...attrs}
              class={cn(
                buttonVariants({ variant: "outline" }),
                "w-[280px] pl-4 justify-start text-left font-normal",
                !value && "text-muted-foreground"
              )}
            >
              {value
                ? df.format(value.toDate(getLocalTimeZone()))
                : "Pick a date"}
              <CalendarIcon class="ml-auto h-4 w-4 opacity-50" />
            </Popover.Trigger>
          </Form.Control>
          <Popover.Content class="w-auto p-0" side="top">
            <Calendar
              bind:value
              bind:placeholder
              minValue={new CalendarDate(1900, 1, 1)}
              maxValue={today(getLocalTimeZone())}
              calendarLabel="Date of birth"
              initialFocus
              onValueChange={(v) => {
                if (v) {
                  $formStore.date_of_birth = v.toString();
                } else {
                  $formStore.date_of_birth = "";
                }
              }}
            />
          </Popover.Content>
        </Popover.Root>
        <Form.Validation />
      </Form.Item>
    </Form.Field>
    <Form.Button>Submit</Form.Button>
  </Form.Root>
</div>
