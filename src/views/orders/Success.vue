<template>
    <div class="container">
        <h1>Success</h1>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Success',
    props: ['order_id'],
    data() {
        return {
            order: null,
        }
    },
    mounted() {
        axios
            .get(`${process.env.VUE_APP_API}/api/orders/${this.order_id}/`)
            .then(({ data }) => (this.order = data))
            .catch((e) => console.log(e))
    },
}
</script>

<style>
</style>