<template>
    <div class="container">
        <!-- <img alt="Vue logo" src="../assets/logo.png" /> -->
        <div class="row mt-5">
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
    name: 'Home',
    components: {
        Item,
    },
    data() {
        return {
            items: [],
        }
    },
    mounted() {
        axios
            .get(`${process.env.VUE_APP_API}/api/items/`)
            .then(({ data }) => (this.items = data.results))
            .catch((e) => console.log(e))
    },
}
</script>
