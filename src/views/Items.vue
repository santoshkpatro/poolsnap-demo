<template>
    <div class="container">
        <h1>Item</h1>
        <div class="row">
            <div class="col-8">
                <img
                    :src="item.resource_url"
                    alt="NA"
                    height="500"
                    class="rounded"
                />
            </div>
            <div class="col-8"></div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Item',
    props: ['item_id'],
    data() {
        return {
            item: null,
        }
    },
    mounted() {
        axios
            .get(`${process.env.VUE_APP_API}/api/items/${this.item_id}/`)
            .then(({ data }) => {
                this.item = data
                console.log(this.item)
            })
            .catch((e) => console.log(e))
    },
}
</script>

<style>
</style>