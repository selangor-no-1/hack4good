<script lang="ts">
	import AnalyticsGraph from "$lib/components/AnalyticsGraph.svelte";
	import AnalyticsCards from "$lib/components/AnalyticsCards.svelte";
	import DateRangePicker from "$lib/components/DateRangePicker.svelte";
	import { reduceVolunteers } from "$lib/utils";

	export let data;
	const { volunteers, manhoursTimeseries, satisfactionTimeseries } = data;
	const uniqueVolunteers = volunteers.length;
	const volunteerTimeseries = reduceVolunteers(volunteers);
	const totalHours = manhoursTimeseries.reduce(
		(acc, cur) => acc + cur.metric,
		0
	);
	const sumSatisfaction = satisfactionTimeseries.reduce(
		(acc, cur) => acc + cur.metric,
		0
	);
	const avgSatisfaction = sumSatisfaction / satisfactionTimeseries.length;
</script>

<div
	class="flex flex-col md:flex-row md:items-center md:justify-between space-y-2"
>
	<h2 class="text-3xl font-bold tracking-tight">Dashboard</h2>
</div>

<AnalyticsCards {uniqueVolunteers} {totalHours} {avgSatisfaction} />

<div class="flex flex-col md:flex-row text-lg font-bold mt-6 gap-3">
	<h2>Overview</h2>
	<div class="md:ml-auto">
		<DateRangePicker />
	</div>
</div>

<AnalyticsGraph title="Active Volunteers" data={volunteerTimeseries} />
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">
	<AnalyticsGraph title="Volunteer Hours" data={manhoursTimeseries} />
	<AnalyticsGraph title="Average Satisfaction" data={satisfactionTimeseries} />
</div>
