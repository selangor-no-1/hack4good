<script lang="ts">
  import EventCard from "$lib/components/EventCard.svelte";
  import type { Volunteer, Event } from "$lib/types";
  import * as Card from "$lib/components/ui/card";
  import * as Avatar from "$lib/components/ui/avatar";
  import * as Dialog from "$lib/components/ui/dialog";
  import { Button } from "$lib/components/ui/button/index.js";
  import { MinusCircle } from "lucide-svelte";

  export let data;

  const { volunteer }: { volunteer: Volunteer } = data;
  const { event_list }: { event_list: Event[] } = data;
  const { hours } = data;
</script>

<div class="flex flex-col container items-center justify-center">
  <Card.Root>
    <Card.Header class="flex justify-between items-center">
      <Card.Title class="text-lg">{volunteer.name}</Card.Title>
      <Dialog.Root>
        <Dialog.Trigger
          ><Button class="text-xs md:text-base h-9">
            <MinusCircle class="mr-2 h-4 w-4" />
            Delete Volunteer
          </Button></Dialog.Trigger
        >
        <Dialog.Content class="sm:max-w-[425px]">
          <Dialog.Header>
            <Dialog.Title>Delete Volunteer</Dialog.Title>
            <Dialog.Description
              >Are you sure you want to delete {volunteer.name}? This action
              cannot be undo-ed.</Dialog.Description
            >
          </Dialog.Header>
          <form action="?/delete" method="POST">
            <input type="hidden" name="id" value={volunteer.id} />
            <button
              class="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded"
            >
              Delete
            </button>
          </form>
        </Dialog.Content>
      </Dialog.Root>
    </Card.Header>
    <Card.Content
      class="flex flex-col md:flex-row gap-2 md:gap-8 items-center justify-center"
    >
      <Avatar.Root class="h-12 w-12">
        <Avatar.Image src="https://xsgames.co/randomusers/avatar.php?g=male" />
        <Avatar.Fallback>{volunteer.name}</Avatar.Fallback>
      </Avatar.Root>
      <div class="mt-4 text-center">
        <div class="text-sm text-muted-foreground text-center">Email</div>
        <div class="text-sm">{volunteer.email}</div>
      </div>
      <div class="mt-4 text-center">
        <div class="text-sm text-muted-foreground">Contact</div>
        <div class="text-sm">{volunteer.contact_number}</div>
      </div>
      <div class="mt-4 text-center">
        <div class="text-sm text-muted-foreground">DoB</div>
        <div class="text-sm">{volunteer.date_of_birth}</div>
      </div>
      <div class="mt-4 text-center">
        <div class="text-sm text-muted-foreground">Hours Volunteered</div>
        <div class="text-sm">{hours}</div>
      </div>
    </Card.Content>
  </Card.Root>
  <h4 class="text-3xl font-bold tracking-tight mt-6">Past Events</h4>
  {#if event_list.length > 0}
    <div
      class="grid grid-flow-col auto-rows-max gap-4 mt-8 items-center justify-center"
    >
      {#each event_list as event}
        <a href="/events/{event.slug}">
          <EventCard {event} />
        </a>
      {/each}
    </div>
  {:else}
    <p>No events yet... 😔</p>
  {/if}
</div>
