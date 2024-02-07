<script lang="ts">
	import * as DropdownMenu from "$lib/components/ui/dropdown-menu";
	import { Button } from "$lib/components/ui/button";
	import { MoreHorizontal } from "lucide-svelte";
	import { goto, preloadData, pushState } from "$app/navigation";
	import { builderActions } from "bits-ui";

	export let id: string;

	const rickRoll = () => {
		window.location.href = "https://www.youtube.com/watch?v=dQw4w9WgXcQ";
	};

	async function onProfileLinkClick(
		e: MouseEvent & { currentTarget: HTMLAnchorElement }
	) {
		if (e.metaKey || e.ctrlKey) return;
		e.preventDefault();

		const { href } = e.currentTarget;
		const result = await preloadData(href);

		if (result.type === "loaded" && result.status == 200) {
			pushState(href, {
				profileData: {
					volunteer: result.data.volunteer,
					event_list: result.data.event_list,
					hours: result.data.hours,
				},
			});
		} else {
			goto(href);
		}
	}
</script>

<DropdownMenu.Root>
	<DropdownMenu.Trigger asChild let:builder>
		<Button
			variant="ghost"
			builders={[builder]}
			size="icon"
			class="relative w-8 h-8 p-0"
		>
			<span class="sr-only">Open menu</span>
			<MoreHorizontal class="w-4 h-4" />
		</Button>
	</DropdownMenu.Trigger>
	<DropdownMenu.Content>
		<DropdownMenu.Group>
			<DropdownMenu.Label>Actions</DropdownMenu.Label>
		</DropdownMenu.Group>
		<a href="/volunteer/{id}" on:click={onProfileLinkClick}>
			<DropdownMenu.Item>View Volunteer Details</DropdownMenu.Item>
		</a>
	</DropdownMenu.Content>
</DropdownMenu.Root>
