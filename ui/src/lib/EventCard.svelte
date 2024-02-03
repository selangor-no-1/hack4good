<script lang="ts">
	import type { Event } from "$lib/types";
	import * as Card from "$lib/components/ui/card";
	import { truncateDescriptionIfTooLong } from "$lib/utils";

	export let event: Event;
</script>

<Card.Root
	class="shadow-sm hover:scale-[102%] transition-all duration-[400ms] cursor-pointer"
>
	<img alt="event" src={event.image} class="rounded-t-md" />
	<Card.Header>
		<Card.Title>{event.name}</Card.Title>
		<Card.Description
			>{truncateDescriptionIfTooLong(event.description)}
		</Card.Description>
	</Card.Header>
</Card.Root>
