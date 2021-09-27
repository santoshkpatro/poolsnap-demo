<template>
    <div class="row mt-3">
        <div class="col-4" v-for="license in licenses" :key="license.id">
            <License :license="license" />
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import License from '@/components/License.vue'

export default {
    name: 'Licenses',
    components: {
        License,
    },
    data() {
        return {
            licenses: [],
        }
    },
    mounted() {
        axios
            .get(`${process.env.VUE_APP_API}/api/licenses/`)
            .then(({ data }) => {
                this.licenses = data.results
            })
            .catch((e) => console.log(e))
    },
}
</script>

<style>
</style>