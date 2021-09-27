<template>
    <div class="container">
        <div class="row mt-5">
            <div class="col-6" v-if="item">
                <h3>Order Details</h3>
                <div class="card" v-if="type === 'monthly'">
                    <div class="card-body">
                        <p>Price = ${{ item.monthly_price }}</p>
                    </div>
                </div>
                <div class="card" v-if="type === 'yearly'">
                    <div class="card-body">
                        <p>Price = ${{ item.yearly_price }}</p>
                    </div>
                </div>
            </div>
            <div class="col-6 mt-5">
                <div class="d-grid gap-2 mt-2">
                    <button
                        class="btn btn-dark"
                        type="submit"
                        @click="createOrder"
                    >
                        Proceed To Pay
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Orders',
    props: ['item_id', 'type'],
    data() {
        return {
            item: null,
        }
    },
    mounted() {
        axios
            .get(`${process.env.VUE_APP_API}/api/items/${this.item_id}/`)
            .then(({ data }) => (this.item = data))
            .catch((e) => console.log(e))
    },
    methods: {
        createOrder() {
            axios
                .get(
                    `${process.env.VUE_APP_API}/api/orders/create/${this.item_id}/`,
                    {
                        params: {
                            type: this.type,
                        },
                    }
                )
                .then(({ data }) =>
                    this.$router.push({
                        name: 'Payment',
                        params: { order_id: data.id },
                    })
                )
                .catch((e) => console.log(e))
        },
    },
}
</script>

<style>
</style>