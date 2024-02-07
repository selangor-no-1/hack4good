<script lang="ts">
	import EventCard from "$lib/components/EventCard.svelte";
	import type { Volunteer, Event } from "$lib/types";
	import * as Card from "$lib/components/ui/card";
	import * as Avatar from "$lib/components/ui/avatar";

	export let data;

	const { volunteer }: { volunteer: Volunteer } = data;
	const { event_list }: { event_list: Event[] } = data;
	const { hours } = data;
</script>

<div class="flex flex-col container items-center justify-center">
	<Card.Root class="border-none">
		<Card.Header class="flex justify-center">
			<Card.Title class="text-lg text-center">{volunteer.name}</Card.Title>
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
