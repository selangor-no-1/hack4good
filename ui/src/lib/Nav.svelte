<script lang="ts">
	import { page } from "$app/stores";
	import { cn } from "$lib/utils";
	import { AreaChart } from "lucide-svelte";
	import { Button } from "$lib/components/ui/button";
	import * as Avatar from "$lib/components/ui/avatar";
	import * as DropdownMenu from "$lib/components/ui/dropdown-menu";

	$: curRoute = $page.route.id;
	$: isAnalytics = curRoute === "/";
	$: isEvents = curRoute === "/events";
</script>

<header class="px-4 lg:px-6 h-14 flex items-center border-b">
	<a href="/" class="flex items-center justify-center">
		<AreaChart class="md:h-8 md:w-8 w-6 h-6" />
		<span class="ml-2 font-xl font-bold tracking-tight">GUI Analytics</span>
		<span class="sr-only">VMS</span>
	</a>
	<nav class="ml-auto flex gap-4 sm:gap-6 items-center">
		<a
			class={cn(
				"text-sm font-medium hover:underline underline-offset-4",
				isAnalytics ? "" : "text-muted-foreground"
			)}
			href="/"
		>
			Analytics
		</a>
		<a
			class={cn(
				"text-sm font-medium hover:underline underline-offset-4",
				isEvents ? "" : "text-muted-foreground"
			)}
			href="/events"
		>
			Events
		</a>
		<DropdownMenu.Root>
			<DropdownMenu.Trigger asChild let:builder>
				<Button
					builders={[builder]}
					variant="outline"
					class="relative h-8 w-8 rounded-full"
				>
					<Avatar.Root class="md:h-8 md:w-8 w-6 h-6">
						<Avatar.Image
							src="https://avatars.githubusercontent.com/u/88436113?v=4"
							alt="@hewliyang"
						/>
						<Avatar.Fallback>SC</Avatar.Fallback>
					</Avatar.Root>
				</Button>
			</DropdownMenu.Trigger>
			<DropdownMenu.Content class="w-56" align="end">
				<DropdownMenu.Label class="font-normal">
					<div class="flex flex-col space-y-1">
						<p class="text-sm font-medium leading-none">Brexton Ong Weng Qi</p>
						<p class="text-xs leading-none text-muted-foreground">
							chriswengqi@tiktok.cn
						</p>
					</div>
				</DropdownMenu.Label>
				<DropdownMenu.Separator />
				<DropdownMenu.Group>
					<DropdownMenu.Item href="/volunteer/create">
						New Volunteer
						<DropdownMenu.Shortcut>⇧⌘P</DropdownMenu.Shortcut>
					</DropdownMenu.Item>
					<DropdownMenu.Item href="/events/create">
						New Event
						<DropdownMenu.Shortcut>⌘B</DropdownMenu.Shortcut>
					</DropdownMenu.Item>
					<DropdownMenu.Item>
						Events
						<DropdownMenu.Shortcut>⌘S</DropdownMenu.Shortcut>
					</DropdownMenu.Item>
					<DropdownMenu.Item>New Team</DropdownMenu.Item>
				</DropdownMenu.Group>
				<DropdownMenu.Separator />
				<DropdownMenu.Item>
					Log out
					<DropdownMenu.Shortcut>⇧⌘Q</DropdownMenu.Shortcut>
				</DropdownMenu.Item>
			</DropdownMenu.Content>
		</DropdownMenu.Root>
	</nav>
</header>
