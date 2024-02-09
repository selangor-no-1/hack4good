<script lang="ts" context="module">
  import { z } from "zod";
  export const formSchema = z.object({
    volunteer: z.string(),
  });
  export type FormSchema = typeof formSchema;
</script>
