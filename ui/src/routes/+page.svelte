<script lang="ts">
	import { BarChart3, Users, Hourglass } from "lucide-svelte";
	import * as Card from "$lib/components/ui/card";
	import DateRangePicker from "$lib/DateRangePicker.svelte";
	import AnalyticsGraph from "$lib/AnalyticsGraph.svelte";
	import AnalyticsCards from "$lib/AnalyticsCards.svelte";

	export let data;
	const { users } = data
</script>


<div class="flex items-center justify-between space-y-2">
	<h2 class="text-3xl font-bold tracking-tight">Dashboard</h2>
	<div class="flex items-center space-x-2">
		<p class="me-2">Dates: </p>
		<DateRangePicker />
	</div>
</div>

<AnalyticsCards />
<AnalyticsGraph userData={users} />