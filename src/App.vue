<template>
    <Navbar />
    <router-view />
</template>

<script>
import axios from 'axios'
import Navbar from '@/components/Navbar.vue'

export default {
    name: 'App',
    components: {
        Navbar,
    },
    created() {
        const userString = localStorage.getItem('user')
        if (userString) {
            const userData = JSON.parse(userString)
            this.$store.commit('SET_USER_DATA', userData)
        }
        axios.interceptors.response.use(
            (response) => response,
            (error) => {
                if (error.response.status === 401) {
                    this.$store.dispatch('logout')
                }
                return Promise.reject(error)
            }
        )
    },
}
</script>

<style>
</style>
