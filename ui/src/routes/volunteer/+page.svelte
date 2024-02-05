<script lang="ts">
  import { Button } from "$lib/components/ui/button";
  import type { Volunteer } from "$lib/types";
  import DataTable from "./(components)/data-table.svelte";
  import { PlusCircle } from "lucide-svelte";
  export let data;
  const { volunteers }: { volunteers: Volunteer[] } = data;
</script>

<div class="flex">
  <h1 class="text-xl md:text-2xl font-bold mb-4">Volunteers</h1>

  <a href="/events/create" class="ml-auto">
    <Button class="text-xs md:text-base h-9">
      <PlusCircle class="mr-2 h-4 w-4" />
      Add Volunteer
    </Button>
  </a>
</div>
<div class="mx-auto py-10 space-y-4">
  <h2 class="text-xl font semibold mb-3">Volunteers</h2>
  {#if volunteers.length > 0}
    <DataTable data={volunteers} />
  {:else}
    <p>No volunteers yet... 😔</p>
  {/if}
</div>
