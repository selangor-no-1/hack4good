<script lang="ts">
	import type { Event } from "$lib/types";
	import EventCard from "$lib/EventCard.svelte";
	import { Button } from "$lib/components/ui/button";
	import { PlusCircle } from "lucide-svelte";

	export let data;

	const { events }: { events: Event[] } = data;
</script>

<div class="flex">
	<h1 class="text-xl md:text-2xl font-bold mb-4">Events</h1>
	<Button class="text-xs md:text-base ml-auto h-9">
		<PlusCircle class="mr-2 h-4 w-4" />
		New Event
	</Button>
</div>

<div class="grid grid-cols-2 md:grid-cols-4 gap-4 mt-8 w-full">
	{#each events as event}
		<a href="events/{event.id}">
			<EventCard {event} />
		</a>
	{/each}
</div>
