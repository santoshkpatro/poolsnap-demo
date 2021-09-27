<template>
    <div class="container mt-5">
        <div class="row" v-if="item">
            <div class="col-8">
                <img
                    :src="item.resource_url"
                    alt="NA"
                    height="500"
                    class="rounded"
                />
            </div>
            <div class="col-4 my-4">
                <router-link
                    :to="{
                        name: 'Profile',
                        params: { username: item.owner.username },
                    }"
                >
                    <div class="d-flex align-items-center">
                        <img
                            :src="item.owner.profile_url"
                            alt="NA"
                            class="profile-img"
                        />
                        <div class="d-flex flex-column ms-2">
                            <span>{{ item.owner.name }}</span>
                            <span class="username"
                                >@{{ item.owner.username }}</span
                            >
                        </div>
                    </div>
                </router-link>

                <div class="d-grid gap-2 mt-2">
                    <button
                        class="btn btn-dark"
                        type="submit"
                        @click="
                            this.$router.push({
                                name: 'Orders',
                                params: {
                                    item_id: item.id,
                                    type: 'monthly_purchase',
                                },
                            })
                        "
                    >
                        Monthly - ${{ item.monthly_price }}
                    </button>
                </div>
                <div class="d-grid gap-2 mt-2">
                    <button
                        class="btn btn-dark"
                        type="submit"
                        @click="
                            this.$router.push({
                                name: 'Orders',
                                params: {
                                    item_id: item.id,
                                    type: 'yearly_purchase',
                                },
                            })
                        "
                    >
                        Yearly - ${{ item.yearly_price }}
                    </button>
                </div>
                <div class="mt-4">
                    <p>{{ item.description }}</p>
                </div>
            </div>
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
            })
            .catch((e) => console.log(e))
    },
}
</script>

<style scoped>
a,
a:hover {
    text-decoration: none;
    color: rgb(0, 0, 0);
}

.profile-img {
    height: 40px;
    width: 40px;
    background: rgb(0, 0, 0);
    padding: 4px;
    border-radius: 50%;
}

.username {
    font-size: 0.8rem;
}
</style>