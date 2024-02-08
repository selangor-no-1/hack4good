<script lang="ts">
	import { Button } from "$lib/components/ui/button";
	import { derived, writable } from "svelte/store";
	import { ChevronLeft, ChevronRight, PlusCircle } from "lucide-svelte";
	import { onMount } from "svelte";
	import { VolunteerDataTable } from "$lib/components/volunteer-table";
	import type { Volunteer } from "$lib/types";
	import * as Pagination from "$lib/components/ui/pagination";

	export let data;
	const { volunteers }: { volunteers: Volunteer[] } = data;

	const perPage = 10;
	const siblingCount = 1;

	const currentPage = writable(1);

	let count = data.volunteers.length;

	const visibleVolunteers = derived([currentPage], ([$currentPage]) => {
		const start = ($currentPage - 1) * perPage;
		const end = start + perPage;
		return data.volunteers.slice(start, end);
	});

	function handlePageChange(newPage: any) {
		currentPage.set(newPage);
	}

	// Ensure that the current page is valid on component mount
	onMount(() => {
		currentPage.subscribe(($currentPage) => {
			if ($currentPage < 1) currentPage.set(1);
			if ($currentPage > Math.ceil(data.volunteers.length / perPage)) {
				currentPage.set(Math.ceil(data.volunteers.length / perPage));
			}
		});
	});
</script>

<div class="flex">
	<h1 class="text-xl md:text-2xl font-bold mb-4">Volunteers</h1>

	<a href="/volunteer/create" class="ml-auto">
		<Button class="text-xs md:text-base h-9">
			<PlusCircle class="mr-2 h-4 w-4" />
			Add Volunteer
		</Button>
	</a>
</div>
<div class="mx-auto py-10 space-y-4">
	<h2 class="text-xl font semibold mb-3">Volunteers</h2>
	{#if volunteers.length > 0}
		<VolunteerDataTable data={visibleVolunteers} />
	{:else}
		<p>No volunteers yet... 😔</p>
	{/if}
</div>

<Pagination.Root {count} {perPage} {siblingCount} let:pages let:currentPage>
	<Pagination.Content>
		<Pagination.Item>
			<Pagination.PrevButton
				on:click={() => handlePageChange(currentPage ?? 1 - 1)}
			>
				<ChevronLeft class="h-4 w-4" />
				<span class="hidden sm:block">Previous</span>
			</Pagination.PrevButton>
		</Pagination.Item>
		{#each pages as page (page.key)}
			{#if page.type === "ellipsis"}
				<Pagination.Item>
					<Pagination.Ellipsis />
				</Pagination.Item>
			{:else}
				<Pagination.Item>
					<Pagination.Link
						{page}
						isActive={currentPage == page.value}
						on:click={() => handlePageChange(page.value)}
					>
						{page.value}
					</Pagination.Link>
				</Pagination.Item>
			{/if}
		{/each}
		<Pagination.Item>
			<Pagination.NextButton
				on:click={() => handlePageChange(currentPage ?? 1 + 1)}
			>
				<span class="hidden sm:block">Next</span>
				<ChevronRight class="h-4 w-4" />
			</Pagination.NextButton>
		</Pagination.Item>
	</Pagination.Content>
</Pagination.Root>
