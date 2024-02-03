<script lang="ts">
  import type { Event } from "$lib/types";
  import DataTable from "./data-table.svelte";
  export let data;
  const { events }: { events: Event[] } = data;
  const currentEvent = events.filter(
    (event) => event.id.toString() === data.slug
  )?.[0];
</script>

<div class="max-w-screen-xl mx-auto p-8">
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
    <div class="col-span-2">
      <img
        src={currentEvent.image}
        alt={currentEvent.name}
        class="w-full h-96 object-cover rounded mb-4"
      />
    </div>

    <div class="col-span-1">
      <h2 class="text-3xl font-semibold mb-4">{currentEvent.name}</h2>
      <p class="text-sm text-gray-500 mb-2">Date: {currentEvent.date}</p>

      <p class="text-gray-700">{currentEvent.description}</p>
    </div>
  </div>
</div>
<div class="container mx-auto py-10">
  Volunteers
  <DataTable data={currentEvent.volunteers} />
</div>
