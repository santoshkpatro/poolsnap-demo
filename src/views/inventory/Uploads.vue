<template>
    <h1>Uploads</h1>
    <div class="row">
        <div class="col-4" v-for="upload in uploads" :key="upload.id">
            <div class="card">
                <img :src="upload.resource_url" class="card-img-top" alt="NA" />
                <div class="overlay fade-overlay">
                    <div class="text">
                        <p>Text</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Uploads',
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
}
</script>

<style scoped>
.overlay {
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    background-color: rgba(85, 79, 76, 0.82);
    overflow: hidden;
    width: 100%;
    height: 100%;
    transition: 0.5s ease;
}

.fade-overlay {
    height: 100%;
    opacity: 0;
}

.card:hover .fade-overlay {
    opacity: 1;
}

.text {
    color: white;
}
</style>