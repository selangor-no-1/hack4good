<script lang="ts">
	import { fade } from "svelte/transition";
	import { Button } from "$lib/components/ui/button";
	import { Download } from "lucide-svelte";
	import type { Timeseries } from "$lib/types";
	import Chart from "chart.js/auto";
	import CrosshairPlugin from "chartjs-plugin-crosshair";
	import * as Card from "$lib/components/ui/card";

	export let data: Timeseries[];
	export let title: string;

	let ctx: HTMLCanvasElement | undefined;
	let chart: Chart | undefined;
	let downloadReady = false;
	let b64: string | undefined;

	// register plugins
	Chart.register(CrosshairPlugin);

	// only create the Chart object once ctx is not null
	// ie: component is mounted
	$: if (ctx) {
		if (chart) {
			chart.destroy();
		}

		chart = new Chart(ctx, {
			type: "line",
			data: {
				labels: data.map((unit) => unit.date),
				datasets: [
					{
						label: "Total Manhours",
						data: data.map(({ metric }) => metric),
						borderWidth: 2,
						fill: true,
						backgroundColor: "rgb(0, 75, 255, 0.2)",
						borderColor: "rgba(15, 100, 200, 1)",
					},
				],
			},
			options: {
				animation: {
					onComplete: function () {
						downloadReady = true;
						b64 = ctx?.toDataURL();
					},
				},
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
						display: false,
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
							display: true,
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

<div class="w-full mt-3">
	<Card.Root>
		<Card.Header>
			<Card.Title class="flex justify-center items-center">
				<h1>{title}</h1>
				<div class="ml-auto flex gap-2">
					<a href={b64} target="_blank" download="graph.png">
						<Button
							variant="outline"
							class="text-xs"
							disabled={!downloadReady && ctx !== undefined}
							><Download class="h-4 w-4 md:mr-3" />
							<span class="hidden md:block">Download</span>
						</Button>
					</a>
				</div>
			</Card.Title>
		</Card.Header>
		<Card.Content class="h-[250px] w-full">
			<canvas bind:this={ctx} in:fade />
		</Card.Content>
	</Card.Root>
</div>
