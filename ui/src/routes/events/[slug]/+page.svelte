<script lang="ts">
	import { Input } from "$lib/components/ui/input";
	import { Button } from "$lib/components/ui/button";
	import { LoaderIcon, UserRoundPlus } from "lucide-svelte";
	import { VolunteerDataTable } from "$lib/components/volunteer-table";
	import { readable } from "svelte/store";
	import { Google } from "$lib/components/icons";
	import FeedbackCard from "$lib/components/FeedbackCard.svelte";
	import { enhance } from "$app/forms";

	export let data;

	const { event, volunteers } = data;
	const volunteersStore = readable(volunteers);
	let subscribing = false;
</script>

<section class="max-w-screen-xl mx-auto py-8">
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
</section>
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
		<Button variant="outline" class="ml-auto"
			><UserRoundPlus class="h-4 w-4 mr-3" /> Add Volunteer</Button
		>
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
