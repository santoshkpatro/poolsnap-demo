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
                            :to="{ name: 'Uploads' }"
                            :class="{
                                active: this.$route.matched.some(
                                    (match) => match.name === 'Inventory'
                                ),
                            }"
                            >Inventory</router-link
                        >
                    </li>
                </ul>
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <router-link
                            class="nav-link mx-3"
                            :to="{ name: 'Upload' }"
                        >
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                width="20"
                                height="20"
                                fill="currentColor"
                                class="bi bi-cloud-upload"
                                viewBox="0 0 16 16"
                            >
                                <path
                                    fill-rule="evenodd"
                                    d="M4.406 1.342A5.53 5.53 0 0 1 8 0c2.69 0 4.923 2 5.166 4.579C14.758 4.804 16 6.137 16 7.773 16 9.569 14.502 11 12.687 11H10a.5.5 0 0 1 0-1h2.688C13.979 10 15 8.988 15 7.773c0-1.216-1.02-2.228-2.313-2.228h-.5v-.5C12.188 2.825 10.328 1 8 1a4.53 4.53 0 0 0-2.941 1.1c-.757.652-1.153 1.438-1.153 2.055v.448l-.445.049C2.064 4.805 1 5.952 1 7.318 1 8.785 2.23 10 3.781 10H6a.5.5 0 0 1 0 1H3.781C1.708 11 0 9.366 0 7.318c0-1.763 1.266-3.223 2.942-3.593.143-.863.698-1.723 1.464-2.383z"
                                />
                                <path
                                    fill-rule="evenodd"
                                    d="M7.646 4.146a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708L8.5 5.707V14.5a.5.5 0 0 1-1 0V5.707L5.354 7.854a.5.5 0 1 1-.708-.708l3-3z"
                                />
                            </svg>
                        </router-link>
                    </li>
                    <li class="nav-item" v-if="!loggedIn">
                        <router-link :to="{ name: 'Login' }">
                            <button class="btn btn-sm btn-light">Login</button>
                        </router-link>
                    </li>
                    <li class="nav-item" v-if="loggedIn">
                        <button
                            class="btn btn-sm btn-light mt-1"
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