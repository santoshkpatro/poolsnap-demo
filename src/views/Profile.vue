<template>
    <div class="container">
        <h1>Profile of user {{ username }}</h1>
        <div class="row my-3">
            <div class="col-4" v-for="item in items" :key="item.id">
                <Item :item="item" />
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import Item from '@/components/Item.vue'

export default {
    props: ['username'],
    components: {
        Item,
    },
    data() {
        return {
            items: null,
        }
    },
    mounted() {
        axios
            .get(`${process.env.VUE_APP_API}/api/items`, {
                params: {
                    username: this.username,
                },
            })
            .then(({ data }) => (this.items = data.results))
            .catch((e) => console.log(e))
    },
}
</script>

<style>
</style>