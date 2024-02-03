<script lang="ts">
  import { page } from "$app/stores";
  import { Calendar } from "$lib/components/ui/calendar";
  import { Calendar as CalendarIcon } from "radix-icons-svelte";
  import * as Form from "$lib/components/ui/form";
  import * as Popover from "$lib/components/ui/popover";
  import { formSchema, type FormSchema } from "./schema";
  import type { SuperValidated } from "sveltekit-superforms";
  import { Button, buttonVariants } from "$lib/components/ui/button";
  import { cn } from "$lib/utils";
  import {
    DateFormatter,
    getLocalTimeZone,
    type DateValue,
    parseDate,
    CalendarDate,
    today,
  } from "@internationalized/date";
  import { superForm } from "sveltekit-superforms/client";
  export let form: SuperValidated<FormSchema> = $page.data.datePicker;

  const theForm = superForm(form, {
    validators: formSchema,
    taintedMessage: null,
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

<Form.Root method="POST" {form} schema={formSchema} let:config>
  <Form.Field {config} name="name">
    <Form.Item>
      <Form.Label>Name</Form.Label>
      <Form.Input />
      <Form.Validation />
    </Form.Item>
  </Form.Field>
  <Form.Field {config} name="date_of_birth">
    <Form.Item>
      <Form.Label>Date of Birth</Form.Label>
      <Popover.Root>
        <Form.Control id="date_of_birth" let:attrs>
          <Popover.Trigger
            id="date_of_birth"
            {...attrs}
            class={cn(
              buttonVariants({ variant: "outline" }),
              "w-[240px] pl-3 justify-start text-left font-normal",
              !value && "text-muted-foreground"
            )}
          >
            {value
              ? df.format(value.toDate(getLocalTimeZone()))
              : "Pick a date"}
            <CalendarIcon class="ml-auto opacity-50 h-4 w-4" />
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
  <Form.Field {config} name="email">
    <Form.Item>
      <Form.Label>Email</Form.Label>
      <Form.Input />
      <Form.Validation />
    </Form.Item>
  </Form.Field>
  <Form.Field {config} name="contact_number">
    <Form.Item>
      <Form.Label>Contact Number</Form.Label>
      <Form.Input />
      <Form.Validation />
    </Form.Item>
  </Form.Field>
  <Form.Button>Submit</Form.Button>
</Form.Root>
