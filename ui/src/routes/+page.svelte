<script lang="ts">
	import { Activity, CreditCard, Users } from "lucide-svelte";
	import { fade } from "svelte/transition";
	import Chart from "chart.js/auto";
	import { Button } from "$lib/components/ui/button";
	import * as Card from "$lib/components/ui/card";
	import DateRangePicker from "$lib/DateRangePicker.svelte";;

	export let data;
	let ctx: HTMLCanvasElement | undefined;
	let chart: Chart | undefined;
	let showAge = true;
	let showWeight = true;
	let showHeight = true;
	let chartType: "line" | "bar" = "line";
	$: if (ctx) {
		if (chart) {
			chart.destroy();
		}

		chart = new Chart(ctx, {
			type: chartType,
			data: {
				labels: data.users.map((user) => `${user.firstName} ${user.lastName}`),
				datasets: [
					{
						label: "User's age",
						data: data.users.map(({ age }) => age),
						borderWidth: 2,
						hidden: !showAge,
					},
					{
						label: "User's height",
						data: data.users.map(({ height }) => height),
						borderWidth: 2,
						hidden: !showHeight,
					},
					{
						label: "User's weight",
						data: data.users.map(({ weight }) => weight),
						borderWidth: 2,
						hidden: !showWeight,
						indexAxis: "x",
					},
				],
			},
			options: {
				animation: false,
				scales: {
					y: {
						beginAtZero: true,
					},
				},
				maintainAspectRatio: false,
			},
		});
	}
</script>


<div class="flex items-center justify-between space-y-2">
	<h2 class="text-3xl font-bold tracking-tight">Dashboard</h2>
	<div class="flex items-center space-x-2">
		<DateRangePicker />

	</div>
</div>

<div class="grid gap-4 md:grid-cols-2 pt-5 lg:grid-cols-4">
	<Card.Root>
		<Card.Header
			class="flex flex-row items-center justify-between space-y-0 pb-2"
		>
			<Card.Title class="text-sm font-medium">Total Manhours</Card.Title>
			<Users class="h-4 w-4 text-muted-foreground" />
		</Card.Header>
		<Card.Content>
			<div class="text-2xl font-bold">+1,350</div>
			<p class="text-xs text-muted-foreground">+180.1% from last month</p>
		</Card.Content>
	</Card.Root>
	<Card.Root>
		<Card.Header
			class="flex flex-row items-center justify-between space-y-0 pb-2"
		>
			<Card.Title class="text-sm font-medium">Total Volunteers</Card.Title>
			<Users class="h-4 w-4 text-muted-foreground" />
		</Card.Header>
		<Card.Content>
			<div class="text-2xl font-bold">+234</div>
			<p class="text-xs text-muted-foreground">+19% from last month</p>
		</Card.Content>
	</Card.Root>
	<Card.Root>
		<Card.Header
			class="flex flex-row items-center justify-between space-y-0 pb-2"
		>
			<Card.Title class="text-sm font-medium">Average Satisfaction</Card.Title>
			<Activity class="h-4 w-4 text-muted-foreground" />
		</Card.Header>
		<Card.Content>
			<div class="text-2xl font-bold">4.73</div>
			<p class="text-xs text-muted-foreground">+0.12 since last week</p>
		</Card.Content>
	</Card.Root>
</div>

<div class="grid gap-4 mt-3 md:grid-cols-2 lg:grid-cols-7">
	<Card.Root class="col-span-5">
		<Card.Header>
			<Card.Title>Overview</Card.Title>
		</Card.Header>
		<Card.Content>
			<div class="w-[600px] h-[400px] border rounded-lg mt-5 p-3">
				<canvas bind:this={ctx} width="100" height="50" in:fade />
			</div>
		</Card.Content>
	</Card.Root>
	<div class="pt-5 ms-2 col-span-2">
		<select bind:value={chartType}>
			<option value="line">Line</option>
			<option value="bar">Bar</option>
		</select>

		<div class="pt-5">
			<div>
				<label for="age">
					<input type="checkbox" bind:checked={showAge} id="age" />
					<span>Show age</span>
				</label>
			</div>
		
			<div>
				<label for="height">
					<input type="checkbox" bind:checked={showHeight} id="height" />
					<span>Show height</span>
				</label>
			</div>
		
			<div>
				<label for="weight">
					<input type="checkbox" bind:checked={showWeight} id="weight" />
					<span>Show Weight</span>
				</label>
			</div>
		</div>
		
		<div class="pt-5">
		{#if ctx}
			<a href={ctx.toDataURL()} target="_blank" download="graph.png">
				<Button>Download Chart</Button>
			</a>
		{/if}
		</div>
	</div>
</div>





