<script lang="ts">
	import DateRangePicker from "$lib/components/DateRangePicker.svelte";
	import AnalyticsGraph from "$lib/components/AnalyticsGraph.svelte";
	import AnalyticsCards from "$lib/components/AnalyticsCards.svelte";
	import { LoaderIcon } from "lucide-svelte";

	export let data;
	const { users, volunteers, manhoursTimeseries } = data;
	const uniqueVolunteers = volunteers.unique_volunteers;
	const totalHours = manhoursTimeseries.reduce(
		(acc, cur) => acc + cur.hours,
		0
	);
</script>

<div
	class="flex flex-col md:flex-row md:items-center md:justify-between space-y-2"
>
	<h2 class="text-3xl font-bold tracking-tight">Dashboard</h2>
	<div class="flex flex-col md:flex-row md:items-center md:space-x-2 space-y-2">
		<DateRangePicker />
	</div>
</div>

<AnalyticsCards {uniqueVolunteers} {totalHours} />

<h2 class="text-lg font-bold mt-6">Overview</h2>
{#await users}
	<div class="w-full items-center justify-center flex p-8">
		<LoaderIcon class="animate-spin" />
	</div>
{:then data}
	<AnalyticsGraph userData={data} />
{/await}
