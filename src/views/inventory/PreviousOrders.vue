<template>
    <table class="table mt-3">
        <thead>
            <tr>
                <th scope="col">Transaction ID</th>
                <th scope="col">Date</th>
                <th scope="col">Status</th>
                <th scope="col">Type</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="order in orders" :key="order.id">
                <td>{{ order.id }}</td>
                <td>{{ order.created_at }}</td>
                <td>{{ order.type }}</td>
                <td>
                    <span
                        class="badge bg-secondary"
                        :class="{
                            'bg-success': order.status === 'complete',
                            'bg-warning': order.status === 'processing',
                        }"
                        >{{ order.status }}</span
                    >
                </td>
            </tr>
        </tbody>
    </table>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Orders',
    data() {
        return {
            orders: [],
        }
    },
    mounted() {
        axios
            .get(`${process.env.VUE_APP_API}/api/orders/`)
            .then(({ data }) => (this.orders = data.results))
            .catch((e) => console.log(e))
    },
}
</script>

<style>
</style>