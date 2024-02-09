<script lang="ts" context="module">
  import { z } from "zod";
  export const formSchema = z.object({
    volunteer: z.string(),
  });

  export type FormSchema = typeof formSchema;
</script>

<script lang="ts">
  import type { Event, Volunteer } from "$lib/types";
  import { Input } from "$lib/components/ui/input";
  import { Button, buttonVariants } from "$lib/components/ui/button";
  import { Check, LoaderIcon, UserRoundPlus } from "lucide-svelte";
  import { tick } from "svelte";
  import { VolunteerDataTable } from "$lib/components/volunteer-table";
  import { readable } from "svelte/store";
  import { Google } from "$lib/components/icons";
  import FeedbackCard from "$lib/components/FeedbackCard.svelte";
  import { enhance } from "$app/forms";
  import * as Form from "$lib/components/ui/form";
  import * as Popover from "$lib/components/ui/popover";
  import * as Command from "$lib/components/ui/command";
  import type { SuperValidated } from "sveltekit-superforms";
  import { cn } from "$lib/utils.js";
  import { page } from "$app/stores";
  import { CaretSort } from "radix-icons-svelte";
  import * as Dialog from "$lib/components/ui/dialog";

  export let data;

  let open = false;

  const {
    event,
    eventVolunteers,
    allVolunteers,
  }: {
    event: Event;
    eventVolunteers: Volunteer[];
    allVolunteers: Volunteer[];
  } = data;

  const nonEventVolunteers = allVolunteers.filter(
    (volunteer) =>
      !eventVolunteers.some(
        (eventVolunteer) => eventVolunteer.id === volunteer.id
      )
  );

  export let form: SuperValidated<FormSchema> = $page.data.combobox;

  const volunteersStore = readable(eventVolunteers);
  let subscribing = false;

  // We want to refocus the trigger button when the user selects
  // an item from the list so users can continue navigating the
  // rest of the form with the keyboard.
  function closeAndFocusTrigger(triggerId: string) {
    open = false;
    tick().then(() => {
      document.getElementById(triggerId)?.focus();
    });
  }
</script>

<div class="max-w-screen-xl mx-auto py-8">
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
    <div class="col-span-2">
      <img
        src={event.image}
        alt={event.name}
        class="w-full h-96 object-cover rounded mb-4 border-dotted shadow-lg hover:scale-[102%] transition-all duration-[400ms]"
      />
    </div>

    <div class="col-span-1">
      <h2
        class="text-3xl font-semibold mb-4 border px-4 py-3 rounded-lg text-left max-w-fit shadow-sm"
      >
        {event.name}
      </h2>
      <p class="text-sm text-muted-foreground mb-2">
        {event.date}
      </p>
      <p class="text-sm text-muted-foreground mb-2">
        from {new Date(event.start_time).toLocaleString("en-SG")} to {new Date(
          event.end_time
        ).toLocaleString("en-SG")}
      </p>
      <p class="text-sm text-muted-foreground mb-2">{event.location}</p>
      <p>{event.description}</p>
    </div>
  </div>
</div>

<section class="mx-auto py-10 space-y-4">
  <div class="flex gap-2">
    <Google />
    <h2 class="text-xl font semibold mb-3 items-center">Form URL</h2>
  </div>
  <form
    method="POST"
    action="?/subscribe"
    class="flex w-full items-center space-x-2"
    use:enhance={() => {
      subscribing = true;
      return async ({ update }) => {
        subscribing = false;
        await update();
      };
    }}
  >
    <input hidden name="eventSlug" value={event.slug} />
    <Input
      type="url"
      name="url"
      placeholder={event.google_form_url || "Google Form Link"}
    />
    <Button type="submit" disabled={subscribing}>
      {#if subscribing}
        <LoaderIcon class="animate-spin h-4 w-4" />
      {:else}
        Subscribe
      {/if}
    </Button>
  </form>
  <div class="flex mt-4 md:mt-0">
    <h2 class="text-xl font semibold mb-3">Volunteers</h2>

    <Dialog.Root>
      <Dialog.Trigger
        class={`${buttonVariants({ variant: "outline" })} ml-auto`}
        ><UserRoundPlus class="h-4 w-4 mr-3" />Add Volunteer</Dialog.Trigger
      >
      <Dialog.Content class="sm:max-w-[425px]">
        <Dialog.Header>
          <Dialog.Title>Add Volunteers</Dialog.Title>
          <Dialog.Description>Add volunteers to this event.</Dialog.Description>
        </Dialog.Header>
        <Form.Root
          {form}
          schema={formSchema}
          let:config
          method="POST"
          action="?/add"
          class="space-y-6"
        >
          <input hidden name="eventSlug" value={event.slug} />
          <Form.Field {config} name="volunteer" let:setValue let:value>
            <Form.Item class="flex flex-col">
              <Form.Label>Volunteers</Form.Label>
              <Popover.Root bind:open let:ids>
                <Popover.Trigger asChild let:builder>
                  <Form.Control id={ids.trigger} let:attrs>
                    <Button
                      {...attrs}
                      builders={[builder]}
                      variant="outline"
                      role="combobox"
                      class={cn(
                        "w-[200px] justify-between",
                        !value && "text-muted-foreground"
                      )}
                    >
                      {nonEventVolunteers.find(
                        (volunteer) => volunteer.id === value
                      )?.name ?? "Select volunteer"}
                      <CaretSort class="ml-2 h-4 w-4 shrink-0 opacity-50" />
                    </Button>
                  </Form.Control>
                </Popover.Trigger>
                <Popover.Content class="w-[200px] p-0">
                  <Command.Root>
                    <Command.Input autofocus placeholder="Search" class="h-9" />
                    <Command.Empty>No volunteers found.</Command.Empty>
                    <Command.Group>
                      {#each nonEventVolunteers as volunteer}
                        <Command.Item
                          value={volunteer.id}
                          onSelect={() => {
                            setValue(volunteer.id);
                            closeAndFocusTrigger(ids.trigger);
                          }}
                        >
                          {volunteer.name}
                          <Check
                            class={cn(
                              "ml-auto h-4 w-4",
                              volunteer.id !== value && "text-transparent"
                            )}
                          />
                        </Command.Item>
                      {/each}
                    </Command.Group>
                  </Command.Root>
                </Popover.Content>
              </Popover.Root>
              <Form.Validation />
            </Form.Item>
          </Form.Field>
          <Form.Button>Submit</Form.Button>
        </Form.Root>
      </Dialog.Content>
    </Dialog.Root>
  </div>
  {#if $volunteersStore.length > 0}
    <VolunteerDataTable data={volunteersStore} />
  {:else}
    <p>No volunteers yet... 😔</p>
  {/if}
  {#if data.responses.length > 0}
    <h2 class="text-xl font semibold">Feedback ✨</h2>
    <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-4">
      {#each data.responses as response}
        <FeedbackCard feedback={response} />
      {/each}
    </div>
  {/if}
</section>
