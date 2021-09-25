<template>
    <h1>Rights</h1>
    <div class="row">
        <div class="col-4" v-for="right in rights" :key="right.id">
            <div class="card">
                <img
                    :src="right.item.resource_url"
                    class="card-img-top"
                    alt="NA"
                />
                <div class="overlay fade-overlay">
                    <div class="text">
                        <div class="top">
                            <p>By - {{ right.item.owner.name }}</p>
                        </div>
                        <div class="bottom">
                            <p>{{ right.item.category.name }}</p>
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
            rights: [],
        }
    },
    mounted() {
        axios
            .get(`${process.env.VUE_APP_API}/api/rights/user/`)
            .then(({ data }) => {
                this.rights = data.results
            })
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
    top: 10%;
    left: 10%;
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