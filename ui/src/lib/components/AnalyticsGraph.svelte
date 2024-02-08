<script lang="ts">
	import { fade } from "svelte/transition";
	import { Button } from "$lib/components/ui/button";
	import { Checkbox } from "$lib/components/ui/checkbox";
	import { Label } from "$lib/components/ui/label";
	import { Download } from "lucide-svelte";
	import type { User } from "$lib/types";
	import Chart from "chart.js/auto";
	import CrosshairPlugin from "chartjs-plugin-crosshair";
	import DateRangePicker from "$lib/components/DateRangePicker.svelte";
	import * as Select from "$lib/components/ui/select";
	import * as Card from "$lib/components/ui/card";

	export let userData: User[];
	let ctx: HTMLCanvasElement | undefined;
	let chart: Chart | undefined;
	let showAge = true;
	let showWeight = true;
	let showHeight = true;
	let chartType: "line" | "bar" = "line";

	// register plugins
	Chart.register(CrosshairPlugin);

	// only create the Chart object once ctx is not null
	// ie: component is mounted
	$: if (ctx) {
		if (chart) {
			chart.destroy();
		}

		chart = new Chart(ctx, {
			type: chartType,
			data: {
				labels: userData.map((user) => `${user.firstName} ${user.lastName}`),
				datasets: [
					{
						label: "Total Manhours",
						data: userData.map(({ age }) => age),
						borderWidth: 2,
						hidden: !showAge,
					},
					{
						label: "Total Volunteers",
						data: userData.map(({ height }) => height),
						borderWidth: 2,
						hidden: !showHeight,
					},
					{
						label: "Average Satisfaction",
						data: userData.map(({ weight }) => weight),
						borderWidth: 2,
						hidden: !showWeight,
					},
				],
			},
			options: {
				plugins: {
					tooltip: {
						enabled: true,
						intersect: false,
						mode: "index",
						titleFont: {
							family: "Manrope Variable",
						},
						bodyFont: {
							family: "Manrope Variable",
						},
					},
					legend: {
						position: "bottom",
						labels: {
							font: {
								family: "Manrope Variable",
							},
						},
					},
					// @ts-ignore
					crosshair: {
						line: {
							width: 0,
							color: "#000",
							dashPattern: [6, 4],
						},
						zoom: {
							enabled: false,
						},
						sync: {
							enabled: false,
						},
					},
				},
				scales: {
					x: {
						grid: {
							display: false,
						},
						ticks: {
							font: {
								family: "Manrope Variable",
							},
							padding: 6,
						},
					},
					y: {
						beginAtZero: true,
						grid: {
							display: true,
							drawTicks: false,
							offset: false,
						},
						border: {
							dash: [5, 5],
							width: 1,
						},
						ticks: {
							font: {
								family: "Manrope Variable",
							},
							padding: 6,
						},
					},
				},
				maintainAspectRatio: false,
				responsive: true,
				normalized: true,
			},
		});
	}
</script>

<section class="grid gap-4 mt-3 md:grid-cols-2 lg:grid-cols-12">
	<div class="col-span-8 mt-3">
		<Card.Root>
			<Card.Header>
				<div class="flex flex-col gap-4 md:flex-row items-center mt-[-6px]">
					<Card.Title>Metrics Over Time</Card.Title>
					<div class="ml-auto">
						<DateRangePicker />
					</div>
				</div>
			</Card.Header>
			<Card.Content class="h-[500px] md:h-[400px]">
				<canvas bind:this={ctx} in:fade />
			</Card.Content>
		</Card.Root>
	</div>
	<div class="md:pt-5 ms-5 col-span-4">
		<Select.Root>
			<Select.Trigger class="w-[180px]">
				<Select.Value placeholder="Chart Type" />
			</Select.Trigger>
			<Select.Content>
				<Select.Item
					value="line"
					label="Line"
					on:click={() => (chartType = "line")}>Line</Select.Item
				>
				<Select.Item
					value="bar"
					label="Bar"
					on:click={() => (chartType = "bar")}>Bar</Select.Item
				>
			</Select.Content>
		</Select.Root>
		<div class="pt-5 space-y-3">
			<div class="flex items-center space-x-2">
				<Checkbox bind:checked={showAge} id="age" />
				<Label
					for="age"
					id="age-label"
					class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
				>
					Total Manhours
				</Label>
			</div>
			<div class="flex items-center space-x-2">
				<Checkbox bind:checked={showHeight} id="height" />
				<Label
					for="height"
					id="height-label"
					class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
				>
					Total Volunteers
				</Label>
			</div>
			<div class="flex items-center space-x-2">
				<Checkbox bind:checked={showWeight} id="weight" />
				<Label
					for="weight"
					id="weight-label"
					class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
				>
					Average Satisfaction
				</Label>
			</div>
		</div>
		<div class="pt-5">
			{#if ctx}
				<a href={ctx.toDataURL()} target="_blank" download="graph.png">
					<Button variant="outline"
						><Download class="h-4 w-4 mr-3" /> Download</Button
					>
				</a>
			{/if}
		</div>
	</div>
</section>
