<script lang="ts">
    import * as Card from "$lib/components/ui/card";
    import DateRangePicker from "$lib/DateRangePicker.svelte";
    import { BarChart3, Users, Hourglass } from "lucide-svelte";
  
    // export let data;
    // const { users } = data;
  </script>
  
<div class="grid gap-4 md:grid-cols-2 pt-5 lg:grid-cols-3">
    <Card.Root>
        <Card.Header class="flex flex-row items-center justify-between space-y-0 pb-2">
        <Card.Title class="text-sm font-medium">Total Manhours</Card.Title>
        <Hourglass class="h-4 w-4 text-muted-foreground" />
        </Card.Header>
        <Card.Content>
        <div class="text-2xl font-bold">+1,350</div>
        <p class="text-xs text-muted-foreground">+180.1% from last month</p>
        </Card.Content>
    </Card.Root>
    <Card.Root>
        <Card.Header class="flex flex-row items-center justify-between space-y-0 pb-2">
        <Card.Title class="text-sm font-medium">Total Volunteers</Card.Title>
        <Users class="h-4 w-4 text-muted-foreground" />
        </Card.Header>
        <Card.Content>
        <div class="text-2xl font-bold">+234</div>
        <p class="text-xs text-muted-foreground">+19% from last month</p>
        </Card.Content>
    </Card.Root>
    <Card.Root>
        <Card.Header class="flex flex-row items-center justify-between space-y-0 pb-2">
        <Card.Title class="text-sm font-medium">Average Satisfaction</Card.Title>
        <BarChart3 class="h-4 w-4 text-muted-foreground" />
        </Card.Header>
        <Card.Content>
        <div class="text-2xl font-bold">4.73</div>
        <p class="text-xs text-muted-foreground">+0.12 since last week</p>
        </Card.Content>
    </Card.Root>
</div>
  