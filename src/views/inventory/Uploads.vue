<template>
    <h1>Uploads</h1>
    <div class="row">
        <div class="col-4" v-for="item in uploads" :key="item.id">
            <Item :item="item" />
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import Item from '@/components/Item.vue'

export default {
    name: 'Uploads',
    components: {
        Item,
    },
    data() {
        return {
            uploads: [],
        }
    },
    mounted() {
        axios
            .get(`${process.env.VUE_APP_API}/api/items/uploads/`)
            .then(({ data }) => (this.uploads = data.results))
            .catch((e) => console.log(e))
    },
}
</script>

<style scoped>
</style>