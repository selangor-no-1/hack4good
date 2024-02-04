<script lang="ts">
	import type { PageData } from "./$types";
	import RegistrationForm from "./registration-form.svelte";
	export let data: PageData;
</script>

<div class="mx-auto max-w-screen-sm">
	<h1 class="text-2xl font-bold mb-3">Registration</h1>
	<RegistrationForm form={data.form} />
</div>
