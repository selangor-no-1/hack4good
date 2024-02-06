<script lang="ts">
	import type { Event } from "$lib/types";
	import * as Card from "$lib/components/ui/card";
	import { truncateDescriptionIfTooLong } from "$lib/utils";

	export let event: Event;
</script>

<Card.Root
	class="shadow-lg hover:scale-[101%] transition-all duration-[400ms] cursor-pointer"
>
	<img alt="event" loading="lazy" src={event.image} class="rounded-t-md" />
	<Card.Header>
		<Card.Title>{event.name}</Card.Title>
		<Card.Description
			>{truncateDescriptionIfTooLong(event.date)}
		</Card.Description>
	</Card.Header>
</Card.Root>
