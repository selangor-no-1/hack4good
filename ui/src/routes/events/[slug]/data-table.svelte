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

  //   const data: Volunteers[] = [
  //     {
  //       id: "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  //       name: "Anderson Leong",
  //       date_of_birth: "2021-02-03",
  //       email: "andersonleong@gmail.com",
  //       contact_number: "91239138",
  //     },
  //     {
  //       id: "9a2a4189-2e37-4475-93b9-108f44087a43",
  //       name: "Brexton Ho Jia Jinn",
  //       date_of_birth: "2020-01-01",
  //       email: "brextonho@gmail.com",
  //       contact_number: "98371848",
  //     },
  //   ];

  const table = createTable(readable(data));

  const columns = table.createColumns([
    table.column({
      accessor: "name",
      header: "Name",
    }),
    table.column({
      accessor: "date_of_birth",
      header: "Date Of Birth",
    }),
    table.column({
      accessor: "email",
      header: "Email",
    }),
    table.column({
      accessor: "contact_number",
      header: "Contact Number",
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
