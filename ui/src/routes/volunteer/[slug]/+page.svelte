<script lang="ts">
	import type { Volunteer } from "$lib/types";

	export let data;

	const { volunteer }: { volunteer: Volunteer } = data;
</script>

<main class="flex justify-center items-center min-h-screen">
	<div class="flex flex-col items-center">
		<div class="rounded-full overflow-hidden w-32 h-32 border-4 border-white">
			<img src="https://avatars.githubusercontent.com/u/88436113?v=4" alt="" />
		</div>
		<div class="mt-4 text-center">
			<h2 class="text-2xl font-semibold text-gray-800">{volunteer.name}</h2>
			<p class="my-2 text-gray-600">Volunteer</p>
			<p class="my-2 text-gray-600">Email: {volunteer.email}</p>
			<p class="my-2 text-gray-600">
				Contact Number: {volunteer.contact_number}
			</p>
			<p class="my-2 text-gray-600">Date of Birth: {volunteer.date_of_birth}</p>
		</div>
	</div>
</main>
