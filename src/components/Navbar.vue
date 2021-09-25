<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <router-link :to="{ name: 'Home' }" class="navbar-brand"
                >PoolSnap</router-link
            >
            <button
                class="navbar-toggler"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent"
                aria-controls="navbarSupportedContent"
                aria-expanded="false"
                aria-label="Toggle navigation"
            >
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <router-link
                            class="nav-link"
                            :to="{ name: 'About' }"
                            :class="{ active: this.$route.name === 'About' }"
                            >About</router-link
                        >
                    </li>
                    <li class="nav-item">
                        <router-link
                            class="nav-link"
                            :to="{ name: 'Inventory' }"
                            :class="{
                                active: this.$route.name === 'Inventory',
                            }"
                            >Inventory</router-link
                        >
                    </li>
                </ul>
                <ul class="navbar-nav">
                    <li class="nav-item" v-if="!loggedIn">
                        <router-link :to="{ name: 'Login' }">
                            <button class="btn btn-sm btn-light">Login</button>
                        </router-link>
                    </li>
                    <li class="nav-item" v-if="loggedIn">
                        <button
                            class="btn btn-sm btn-light"
                            @click="handleLogout"
                        >
                            Logout
                        </button>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
    name: 'Navbar',
    computed: {
        ...mapGetters(['loggedIn']),
    },
    methods: {
        handleLogout() {
            this.$store.dispatch('logout')
        },
    },
}
</script>

<style>
</style>