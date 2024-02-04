<script lang="ts">
	import RegistrationForm from "./(components)/registration-form.svelte";
	export let data;
</script>

<div class="mx-auto container">
	<h1 class="text-2xl font-semibold mb-3">Create a New Volunteer</h1>
	<RegistrationForm form={data.form} />
</div>
