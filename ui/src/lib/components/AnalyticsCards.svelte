<script lang="ts">
	import * as Card from "$lib/components/ui/card";
	import { BarChart3, Users, Hourglass } from "lucide-svelte";

	export let uniqueVolunteers: number;
	export let totalHours: number;
	export let avgSatisfaction: number;
</script>

<div class="grid gap-4 md:grid-cols-2 pt-5 lg:grid-cols-3">
	<Card.Root>
		<Card.Header
			class="flex flex-row items-center justify-between space-y-0 pb-2"
		>
			<Card.Title class="text-sm font-medium">Total Manhours</Card.Title>
			<Hourglass class="h-4 w-4 text-muted-foreground" />
		</Card.Header>
		<Card.Content>
			<div class="text-2xl font-bold">+{totalHours}</div>
			<p class="text-xs text-muted-foreground">+180.1% from last month</p>
		</Card.Content>
	</Card.Root>
	<Card.Root>
		<Card.Header
			class="flex flex-row items-center justify-between space-y-0 pb-2"
		>
			<Card.Title class="text-sm font-medium"
				>Total Active Volunteers</Card.Title
			>
			<Users class="h-4 w-4 text-muted-foreground" />
		</Card.Header>
		<Card.Content>
			<div class="text-2xl font-bold">+{uniqueVolunteers}</div>
			<p class="text-xs text-muted-foreground">+19% from last month</p>
		</Card.Content>
	</Card.Root>
	<Card.Root>
		<Card.Header
			class="flex flex-row items-center justify-between space-y-0 pb-2"
		>
			<Card.Title class="text-sm font-medium">Average Satisfaction</Card.Title>
			<BarChart3 class="h-4 w-4 text-muted-foreground" />
		</Card.Header>
		<Card.Content>
			<div class="text-2xl font-bold">{avgSatisfaction.toFixed(2)}</div>
			<p class="text-xs text-muted-foreground">+0.12 since last week</p>
		</Card.Content>
	</Card.Root>
</div>
