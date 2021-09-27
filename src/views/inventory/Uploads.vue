<template>
    <div class="row mt-3">
        <div class="col-4" v-for="item in uploads" :key="item.id">
            <UploadItem @itemDeleted="handleUpdate" :item="item" />
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import Item from '@/components/Item.vue'
import UploadItem from '@/components/UploadItem.vue'

export default {
    name: 'Uploads',
    components: {
        Item,
        UploadItem,
    },
    data() {
        return {
            uploads: [],
        }
    },
    mounted() {
        axios
            .get(`${process.env.VUE_APP_API}/api/items/uploads/`)
            .then(({ data }) => (this.uploads = data.results))
            .catch((e) => console.log(e))
    },
    methods: {
        handleUpdate(id) {
            this.uploads = this.uploads.filter((upload) => upload.id !== id)
        },
    },
}
</script>

<style scoped>
</style>