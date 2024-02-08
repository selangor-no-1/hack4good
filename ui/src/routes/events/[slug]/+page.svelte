<script lang="ts">
  import DataTable from "./(components)/data-table.svelte";
  import SearchInput from "./(components)/search-input.svelte";
  import { API_ENDPOINT } from "$lib/config";
  import type { Event, Volunteer } from "$lib/types";
  import { Input } from "$lib/components/ui/input";
  import { Button } from "$lib/components/ui/button";
  import { LoaderIcon, UserRoundPlus } from "lucide-svelte";
  import { onMount } from "svelte";
  import { writable, type Writable } from "svelte/store";

  export let data;
  let isLoading = false;

  let dialog: any; // Reference to the dialog tag
  onMount(() => {
    dialog = document.getElementById("add-volunteer-dialog");
  });

  let menuOpen = false;
  let inputValue = "";

  const showDialogClick = (asModal = true) => {
    try {
      dialog[asModal ? "showModal" : "show"]();
    } catch (e: any) {
      console.log(e.message);
    }
  };

  const closeClick = () => {
    dialog.close();
  };

  const {
    event,
    eventVolunteers,
    allVolunteers,
  }: {
    event: Event;
    eventVolunteers: Volunteer[];
    allVolunteers: Volunteer[];
  } = data;

  const nonEventVolunteers = allVolunteers.filter(
    (volunteer) =>
      !eventVolunteers.some(
        (eventVolunteer) => eventVolunteer.id === volunteer.id
      )
  );

  let filteredVolunteers: Volunteer[] = [];

  const handleInput = () => {
    return (filteredVolunteers = nonEventVolunteers.filter((item) =>
      item.name.toLowerCase().match(inputValue.toLowerCase())
    ));
  };

  let selectedVolunteer: Writable<Volunteer | null> = writable(null);

  function selectVolunteer(newVolunteer: Volunteer) {
    selectedVolunteer.set(newVolunteer);
  }

  const handleSubmit = async () => {
    try {
      const value: Volunteer | null = $selectedVolunteer;

      if (value !== null) {
        const resp = await fetch(
          API_ENDPOINT +
            `events/${event.slug}/volunteers?volunteer_id=${value.id}`,
          {
            method: "POST",
          }
        );

        if (!resp.ok) {
          throw new Error("Check that the API server is running!");
        }
        dialog.close();
      } else {
        console.error("Volunteer value is null");
      }
    } catch (error) {
      console.error("Error: " + error);
      // bandaid solution since POST request is 200 in the server side
      // but since the request is sent through client-side there is CORS when reading the response (intended should be through server)
      // aint got time to figure out how tf does the POST through forms work, you dont need any info from the POST reponse anyways
      location.reload();
    }
  };
</script>

<div class="max-w-screen-xl mx-auto py-8">
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
    <div class="col-span-2">
      <img
        src={event.image}
        alt={event.name}
        class="w-full h-96 object-cover rounded mb-4 border-dotted shadow-lg hover:scale-[102%] transition-all duration-[400ms]"
      />
    </div>

    <div class="col-span-1">
      <h2
        class="text-3xl font-semibold mb-4 border px-4 py-3 rounded-lg text-left max-w-fit shadow-sm"
      >
        {event.name}
      </h2>
      <p class="text-sm text-muted-foreground mb-2">
        {event.date}
      </p>
      <p class="text-sm text-muted-foreground mb-2">
        from {new Date(event.start_time).toLocaleString("en-SG")} to {new Date(
          event.end_time
        ).toLocaleString("en-SG")}
      </p>
      <p class="text-sm text-muted-foreground mb-2">{event.location}</p>
      <p>{event.description}</p>
    </div>
  </div>
</div>
<div class="mx-auto py-10 space-y-4">
  <h2 class="text-xl font semibold mb-3">Google Form</h2>
  <form class="flex w-full max-w-sm items-center space-x-2">
    <Input type="email" placeholder="Google Form ID" />
    <Button type="submit" on:click={() => (isLoading = true)}>
      {#if isLoading}
        <LoaderIcon class="animate-spin h-4 w-4" />
      {:else}
        Subscribe
      {/if}
    </Button>
  </form>
  <dialog
    id="add-volunteer-dialog"
    class="items-center h-screen transform bg-white shadow-md rounded-lg p-6"
  >
    <h1 class="text-2xl mb-4">Add Volunteer to {event.name}</h1>
    <p class="mb-4">Volunteer: {$selectedVolunteer?.name || "None"}</p>
    <section class="dropdown">
      <div
        id="myDropdown"
        class:show={menuOpen}
        class="dropdown-content rounded-lg"
      >
        <SearchInput bind:inputValue on:input={handleInput} />
        <!-- MENU -->
        {#if filteredVolunteers.length > 0}
          {#each filteredVolunteers as volunteer}
            <h2>
              <button
                class="hover:bg-gray-300"
                on:click={() => selectVolunteer(volunteer)}
              >
                {volunteer.name}
              </button>
            </h2>
          {/each}
        {/if}
      </div>
    </section>
    <div class="justify-center">
      <Button variant="outline" class="mt-4 ml-auto" on:click={handleSubmit}
        >Add</Button
      >
      <Button variant="outline" class="mt-4 ml-auto" on:click={closeClick}
        >Close</Button
      >
    </div>
  </dialog>
  <div class="flex">
    <h2 class="text-xl font semibold mb-3">Volunteers</h2>
    <Button
      variant="outline"
      class="ml-auto"
      on:click={() => showDialogClick(true)}
      ><UserRoundPlus class="h-4 w-4 mr-3" /> Add Volunteer</Button
    >
  </div>
  {#if eventVolunteers.length > 0}
    <DataTable data={eventVolunteers} />
  {:else}
    <p>No volunteers yet... 😔</p>
  {/if}
</div>

<style>
  dialog {
    border-radius: 5px;
    border-width: 1px;
    transition: all 2s;
  }
  dialog::backdrop {
    background: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.7));
    animation: fade-in 1s;
  }
</style>
