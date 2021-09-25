<template>
    <div class="container mt-3">
        <Tabs />
        <router-view></router-view>
    </div>
</template>

<script>
import Tabs from '@/components/Tabs.vue'

export default {
    name: 'Inventory',
    components: {
        Tabs,
    },
}
</script>

<style>
</style>