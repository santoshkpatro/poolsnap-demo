<template>
    <h1>Uploads</h1>
    <div class="row">
        <div class="col-4" v-for="upload in uploads" :key="upload.id">
            <div class="card">
                <img :src="upload.resource_url" class="card-img-top" alt="NA" />
                <div class="overlay fade-overlay">
                    <div class="text">
                        <div class="top">
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                width="30"
                                height="30"
                                fill="currentColor"
                                class="bi bi-trash"
                                viewBox="0 0 16 16"
                            >
                                <path
                                    d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"
                                />
                                <path
                                    fill-rule="evenodd"
                                    d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"
                                />
                            </svg>
                        </div>
                        <div class="bottom">
                            <p>{{ upload.created_at }}</p>
                        </div>
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

.text .top {
    color: white;
    font-size: 1.2vw;
    position: absolute;
    top: 7%;
    left: 90%;
    -webkit-transform: translate(-50%, -50%);
    -ms-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
    text-align: center;
}

.text .bottom {
    color: white;
    /* font-size: 1.2vw; */
    position: absolute;
    top: 95%;
    left: 15%;
    -webkit-transform: translate(-50%, -50%);
    -ms-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
    text-align: center;
}
</style>