<script lang="ts">
  import type { PageData } from "./$types";
  import RegistrationForm from "./registration-form.svelte";
  export let data: PageData;
</script>

<div class="mx-auto max-w-screen-sm">
  Registration
  <RegistrationForm form={data.form} />
</div>
