<script lang="ts">
	import DateRangePicker from "$lib/components/DateRangePicker.svelte";
	import AnalyticsGraph from "$lib/components/AnalyticsGraph.svelte";
	import AnalyticsCards from "$lib/components/AnalyticsCards.svelte";

	export let data;
	const { users } = data;
</script>

<div
	class="flex flex-col md:flex-row md:items-center md:justify-between space-y-2"
>
	<h2 class="text-3xl font-bold tracking-tight">Dashboard</h2>
	<div class="flex flex-col md:flex-row md:items-center md:space-x-2 space-y-2">
		<DateRangePicker />
	</div>
</div>

<AnalyticsCards />
<AnalyticsGraph userData={users} />
