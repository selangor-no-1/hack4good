<script lang="ts">
	import {
		createRender,
		createTable,
		Render,
		Subscribe,
	} from "svelte-headless-table";
	import { readable } from "svelte/store";
	import * as Table from "$lib/components/ui/table";
	import type { Volunteer } from "$lib/types";
	import DataTableActions from "./data-table-actions.svelte";

	export let data: Volunteer[];

	const table = createTable(readable(data));

	const columns = table.createColumns([
		table.column({
			accessor: "name",
			header: "Name",
		}),
		table.column({
			accessor: "date_of_birth",
			header: "DoB",
		}),
		table.column({
			accessor: "email",
			header: "Email",
		}),
		table.column({
			accessor: "contact_number",
			header: "Contact No.",
		}),
		table.column({
			accessor: ({ id }) => id,
			header: "",
			cell: ({ value }) => {
				return createRender(DataTableActions, { id: value });
			},
		}),
	]);

	const { headerRows, pageRows, tableAttrs, tableBodyAttrs } =
		table.createViewModel(columns);
</script>

<div class="rounded-md border">
	<Table.Root {...$tableAttrs}>
		<Table.Header>
			{#each $headerRows as headerRow}
				<Subscribe rowAttrs={headerRow.attrs()}>
					<Table.Row>
						{#each headerRow.cells as cell (cell.id)}
							<Subscribe attrs={cell.attrs()} let:attrs props={cell.props()}>
								<Table.Head {...attrs}>
									<Render of={cell.render()} />
								</Table.Head>
							</Subscribe>
						{/each}
					</Table.Row>
				</Subscribe>
			{/each}
		</Table.Header>
		<Table.Body {...$tableBodyAttrs}>
			{#each $pageRows as row (row.id)}
				<Subscribe rowAttrs={row.attrs()} let:rowAttrs>
					<Table.Row {...rowAttrs}>
						{#each row.cells as cell (cell.id)}
							<Subscribe attrs={cell.attrs()} let:attrs>
								<Table.Cell {...attrs}>
									<Render of={cell.render()} />
								</Table.Cell>
							</Subscribe>
						{/each}
					</Table.Row>
				</Subscribe>
			{/each}
		</Table.Body>
	</Table.Root>
</div>
