<script lang="ts">
	import { fade } from "svelte/transition";
	import Chart from "chart.js/auto";
	import { Button } from "$lib/components/ui/button";
	import type { User } from "$lib/types";

	export let userData: User[];
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

<div class="grid gap-4 mt-3 md:grid-cols-2 lg:grid-cols-12">
	<div class="col-span-8 mt-3">
		<h2 class="font-bold">Overview</h2>
		<div class="h-[21rem] 2xl:h-[21rem] border rounded-lg mt-4 p-1">
			<canvas bind:this={ctx} in:fade />
		</div>
	</div>
	<div class="pt-5 ms-5 mt-8 col-span-4">
		<select bind:value={chartType}>
			<option value="line">Line</option>
			<option value="bar">Bar</option>
		</select>
		<div class="pt-5">
			<div>
				<label for="age">
					<input type="checkbox" bind:checked={showAge} id="age" />
					<span>Total Manhours</span>
				</label>
			</div>
			<div>
				<label for="height">
					<input type="checkbox" bind:checked={showHeight} id="height" />
					<span>Total Volunteers</span>
				</label>
			</div>
			<div>
				<label for="weight">
					<input type="checkbox" bind:checked={showWeight} id="weight" />
					<span>Average Satisfaction</span>
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
