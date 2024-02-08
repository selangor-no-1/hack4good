<script lang="ts">
	import { marked } from "marked";
	export let md: string;
</script>

<div class="prose prose-sm">
	{@html marked(md)}
</div>
