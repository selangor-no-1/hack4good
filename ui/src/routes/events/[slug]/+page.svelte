<script lang="ts">
	import { Button } from "$lib/components/ui/button";
	import type { Event, Volunteer } from "$lib/types";
	import DataTable from "./(components)/data-table.svelte";
	export let data;
	const { event, volunteers }: { event: Event; volunteers: Volunteer[] } = data;
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
					event.end_time.toLocaleString("en-SG")
				)}
			</p>
			<p class="text-sm text-muted-foreground mb-2">{event.location}</p>
			<p>{event.description}</p>
		</div>
	</div>
</div>
<div class="mx-auto py-10 space-y-4">
	<h2 class="text-xl font semibold mb-3">Volunteers</h2>
	{#if volunteers.length > 0}
		<DataTable data={volunteers} />
	{:else}
		<p>No volunteers yet... 😔</p>
		<Button>Add Volunteer</Button>
	{/if}
</div>
