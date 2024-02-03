<script>
	import "../app.pcss";
	import "@fontsource-variable/manrope";
	import Nav from "$lib/Nav.svelte";
</script>

<main class="flex flex-col min-h-screen bg-white">
	<Nav />
	<div class="flex-1 px-4 py-4 md:px-8 md:py-6">
		<slot />
	</div>
</main>
