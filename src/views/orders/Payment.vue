<template>
    <div class="container">
        <h1>Payment</h1>
        <div class="row">
            <div class="col-6">
                <div class="card" v-if="order">
                    <div class="card-body">
                        <p><strong>Order - </strong>{{ order.id }}</p>
                    </div>
                </div>
                <h3 class="mt-3">Billing Details</h3>
                <form class="row g-3">
                    <div class="col-md-6">
                        <label for="inputEmail4" class="form-label"
                            >Email</label
                        >
                        <input
                            type="email"
                            class="form-control"
                            id="inputEmail4"
                        />
                    </div>
                    <div class="col-md-6">
                        <label for="inputPassword4" class="form-label"
                            >Password</label
                        >
                        <input
                            type="password"
                            class="form-control"
                            id="inputPassword4"
                        />
                    </div>
                    <div class="col-12">
                        <label for="inputAddress" class="form-label"
                            >Address</label
                        >
                        <input
                            type="text"
                            class="form-control"
                            id="inputAddress"
                            placeholder="1234 Main St"
                        />
                    </div>
                    <div class="col-12">
                        <label for="inputAddress2" class="form-label"
                            >Address 2</label
                        >
                        <input
                            type="text"
                            class="form-control"
                            id="inputAddress2"
                            placeholder="Apartment, studio, or floor"
                        />
                    </div>
                    <div class="col-md-6">
                        <label for="inputCity" class="form-label">City</label>
                        <input
                            type="text"
                            class="form-control"
                            id="inputCity"
                        />
                    </div>
                    <div class="col-md-4">
                        <label for="inputState" class="form-label">State</label>
                        <select id="inputState" class="form-select">
                            <option selected>Choose...</option>
                            <option>...</option>
                        </select>
                    </div>
                    <div class="col-md-2">
                        <label for="inputZip" class="form-label">Zip</label>
                        <input type="text" class="form-control" id="inputZip" />
                    </div>
                </form>
            </div>
            <div class="col-6 mt-5">
                <h5>Choose a dummy payment status</h5>
                <div class="d-grid gap-2">
                    <button
                        class="btn btn-success"
                        type="button"
                        @click="handlePayment('success')"
                    >
                        Success
                    </button>
                    <button
                        class="btn btn-danger"
                        type="button"
                        @click="handlePayment('failure')"
                    >
                        Failure
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
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
    methods: {
        handlePayment(status) {
            axios
                .get(
                    `${process.env.VUE_APP_API}/api/orders/process/${this.order_id}/`,
                    {
                        params: {
                            status: status,
                        },
                    }
                )
                .then(({ data }) =>
                    this.$router.push({
                        name: 'Success',
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