<script lang="ts">
	import * as Card from "$lib/components/ui/card";
	import * as Popover from "$lib/components/ui/popover";
	import Markdown from "$lib/components/Markdown.svelte";
	import { Star, Info } from "lucide-svelte";
	import type { Response } from "$lib/types";
	export let feedback: Response;
</script>

<Card.Root class="w-fit">
	<Card.Header class="p-4">
		<div class="flex flex-row">
			<div class="flex flex-col">
				<Card.Title class="text-base">
					{feedback.email}
				</Card.Title>
				<Card.Description class="text-sm">
					Submitted on {feedback.submit_date}
				</Card.Description>
			</div>
			<div class="ml-auto flex items-center space-x-2">
				{#each { length: feedback.satisfaction } as _}
					<Star class="h-4 w-4 fill-green-500" />
				{/each}
				{#each { length: 5 - feedback.satisfaction } as _}
					<Star class="h-4 w-4 stroke-muted-foreground" />
				{/each}
			</div>
		</div>
	</Card.Header>
	<Card.Footer class="p-4 relative">
		<div class="grid gap-0.5">
			<div class="text-xs leading-none">Reason for satisfaction</div>
			<div class="text-sm">{feedback.reason}</div>
		</div>
		<div class="absolute bottom-0 right-0 mr-2 mb-2">
			<Popover.Root>
				<Popover.Trigger>
					<Info class="h-4 w-4" />
				</Popover.Trigger>
				<Popover.Content>
					<Markdown md={feedback.content} />
				</Popover.Content>
			</Popover.Root>
		</div>
	</Card.Footer>
</Card.Root>
