<script lang="ts">
	import type { Event } from "$lib/types";
	import EventCard from "$lib/EventCard.svelte";

	export let data;

	const { events }: { events: Event[] } = data;
</script>

<h1 class="text-xl md:text-2xl font-bold mb-4">Events</h1>

<div class="grid grid-cols-2 md:grid-cols-4 gap-4 mt-8 w-full">
	{#each events as event}
		<a href="/">
			<EventCard {event} />
		</a>
	{/each}
</div>
