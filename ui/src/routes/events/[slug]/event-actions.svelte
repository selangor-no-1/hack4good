<script lang="ts">
  import { Button } from "$lib/components/ui/button";
	import { XCircle, FileCheck, Edit } from "lucide-svelte";
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu";
  import Input from "./input_volunteer.svelte";

  import {
    createRender,
    createTable,
    Render,
    Subscribe,
  } from "svelte-headless-table";
  import * as Table from "$lib/components/ui/table";
  import { readable } from "svelte/store";

  import type { Volunteer } from "$lib/types";
  export let data: Volunteer[];
  const table = createTable(readable(data));

  let editActive = false;
  let toggleEdit = () => {editActive = !editActive};
  let handleSubmission = () => {};

  let menuOpen = false;
  let inputValue = "";
  const menuItems = data.map((volunteer) => volunteer.name);
	// const menuItems = ["About", "Base", "Blog", "Contact", "Custom", "Support", "Tools", "Boats", "Cars", "Bikes", "Sheds", "Billygoats", "Zebras", "Tennis Shoes", "New Zealand"];
	let filteredItems: string | any = [];
	
	const handleInput = () => {
		return filteredItems = menuItems.filter(item => item.toLowerCase().match(inputValue.toLowerCase()));	
	}

  
</script>

<div class="block gap-4">
  <!-- List of people to add -->
  <div class="my-4">
  {#if editActive}
    <section class="dropdown">
      <Button on:click={() => menuOpen = !menuOpen}/>
      
      <div id="myDropdown" class:show={menuOpen} class="dropdown-content">		
      <Input bind:inputValue on:input={handleInput} />		
        <!-- MENU -->
        {#if filteredItems.length > 0}
          {#each filteredItems as item}
            <div>{item}</div>
            <!-- <Link link={item} /> -->
          {/each}
        {:else}
          {#each menuItems as item}
            <div>{item}</div>
            <!-- <Link link={item} /> -->
          {/each}
        {/if}		
      </div>	
    </section>
  
  {/if}
  </div>
  <div class="flex justify-end">
  {#if editActive}
    <div class="">
      <Button class="text-xs md:text-base ml-auto h-8" on:click={toggleEdit}>
        <XCircle class="mr-2 h-4 w-4" />
        Cancel
      </Button>
      <Button class="text-xs md:text-base ml-auto h-8" on:click={handleSubmission}>
        <FileCheck class="mr-2 h-4 w-4" />
        Done
      </Button>    
    </div>
  {:else}
  <Button class="text-xs md:text-base ml-auto h-8" on:click={toggleEdit}>
    <Edit class="mr-2 h-4 w-4" />
    Edit
  </Button>    
  {/if}
  </div>
</div>

<style>		
  .dropdown {
    position: relative;
    display: inline-block;
  }
    
  .dropdown-content {
    display: none;
    position: absolute;
    background-color: #f6f6f6;
    min-width: 230px;
    border: 1px solid #ddd;
    z-index: 1;
  }
  
  /* Show the dropdown menu */	
  .show {display:block;}	
</style>