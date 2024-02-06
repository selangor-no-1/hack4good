<script lang="ts">
	import EventCard from "$lib/components/EventCard.svelte";
	import type { Volunteer, Event } from "$lib/types";

	export let data;

	const { volunteer }: { volunteer: Volunteer } = data;
	const { event_list }: { event_list: Event[] } = data;
	const { hours } = data;
</script>

<div class="flex justify-center items-center min-h-screen">
	<div class="flex flex-col items-center">
		<div class="rounded-full overflow-hidden w-32 h-32 border-4 border-white">
			<img src="https://avatars.githubusercontent.com/u/88436113?v=4" alt="" />
		</div>
		<div class="mt-4 text-center">
			<h2 class="text-2xl font-semibold text-gray-800">{volunteer.name}</h2>
			<p class="my-2 text-gray-600">Volunteer</p>
			<p class="my-2 text-gray-600">Email: {volunteer.email}</p>
			<p class="my-2 text-gray-600">
				Contact Number: {volunteer.contact_number}
			</p>
			<p class="my-2 text-gray-600">Date of Birth: {volunteer.date_of_birth}</p>
			<p class="my-2 text-gray-600">Total Volunteer Hours: {hours}</p>
		</div>
	</div>
</div>
<h4 class="text-3xl font-bold tracking-tight">Past Events</h4>
{#if event_list.length > 0}
	<div class="grid grid-cols-2 md:grid-cols-4 gap-4 mt-8 w-full">
		{#each event_list as event}
			<a href="/events/{event.slug}">
				<EventCard {event} />
			</a>
		{/each}
	</div>
{:else}
	<p>No events yet... 😔</p>
{/if}
