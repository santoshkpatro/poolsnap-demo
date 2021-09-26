<template>
    <div class="container">
        <h1>Upload Your Photo</h1>
        <div class="row">
            <div class="col-8">
                <form class="row" @submit.prevent="handleUpload">
                    <div class="col-md-4">
                        <label for="inputEmail4" class="form-label"
                            >Monthly Pricing</label
                        >
                        <input
                            type="number"
                            class="form-control"
                            id="inputEmail4"
                            v-model="monthly_price"
                            required
                        />
                    </div>
                    <div class="col-md-4">
                        <label for="inputEmail4" class="form-label"
                            >Yearly Pricing</label
                        >
                        <input
                            type="number"
                            class="form-control"
                            id="inputEmail4"
                            v-model="yearly_price"
                            required
                        />
                    </div>
                    <div class="col-md-4">
                        <label class="form-label">Select Category</label>
                        <select
                            class="form-select"
                            aria-label="Default select example"
                            v-model="selectedCategory"
                        >
                            <option value="" disabled>Please select one</option>
                            <option
                                v-for="category in categories"
                                :key="category.id"
                                :value="category"
                            >
                                {{ category.name }}
                            </option>
                        </select>
                    </div>
                    <div class="col-12">
                        <label for="inputAddress" class="form-label"
                            >Description</label
                        >
                        <input
                            type="text"
                            class="form-control"
                            id="inputAddress"
                            placeholder="Short description"
                            v-model="description"
                        />
                    </div>
                    <div class="d-grid gap-2 mt-5">
                        <button
                            class="btn btn-dark"
                            type="submit"
                            v-if="!server"
                        >
                            Start Upload
                        </button>
                    </div>
                </form>
            </div>
            <div class="col-4" v-if="upload">
                <FilePond
                    ref="pond"
                    name="file"
                    class="my-3"
                    accepted-file-types="image/jpeg, image/png"
                    v-bind:file="file"
                    v-on:init="handleFilePondInit"
                    :server="server"
                />
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
import axios from 'axios'
import vueFilePond from 'vue-filepond'
import FilePondPluginImagePreview from 'filepond-plugin-image-preview'
import 'filepond/dist/filepond.min.css'
import 'filepond-plugin-image-preview/dist/filepond-plugin-image-preview.min.css'

export default {
    components: {
        FilePond: vueFilePond(FilePondPluginImagePreview),
    },
    data() {
        return {
            categories: [],
            monthly_price: null,
            yearly_price: null,
            selectedCategory: null,
            description: null,
            upload: false,
            server: null,
            file: null,
        }
    },
    computed: {
        ...mapGetters(['getUser']),
    },
    mounted() {
        axios
            .get(`${process.env.VUE_APP_API}/api/categories/`)
            .then(({ data }) => {
                this.categories = data.results
                this.selectedCategory = data.results[0]
            })
            .catch((e) => console.log(e))
    },
    methods: {
        handleUpload() {
            axios
                .post(`${process.env.VUE_APP_API}/api/items/`, {
                    monthly_price: this.monthly_price,
                    yearly_price: this.yearly_price,
                    description: this.description,
                    category_id: this.selectedCategory.id,
                })
                .then(({ data }) => {
                    this.server = {
                        url: `${process.env.VUE_APP_API}/api/items/${data.id}/upload/`,
                        process: {
                            method: 'POST',
                            withCredentials: false,
                            headers: {
                                Authorization: `Bearer ${this.getUser.token}`,
                            },
                            onload: null,
                            onerror: null,
                            ondata: null,
                        },
                    }
                    this.upload = true
                })
                .catch((e) => console.log(e))
        },
        handleFilePondInit: function () {
            console.log('FilePond has initialized')
        },
    },
}
</script>

<style>
</style>