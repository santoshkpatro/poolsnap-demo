<template>
    <div class="card position-relative">
        <img :src="item.resource_url" class="card-img-top rounded" alt="NA" />
        <div class="overlay">
            <div class="top">
                <button class="rounded" @click="handleDelete">
                    <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="20"
                        height="20"
                        fill="currentColor"
                        class="bi bi-trash-fill"
                        viewBox="0 0 16 16"
                    >
                        <path
                            d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"
                        />
                    </svg>
                </button>
            </div>
            <div
                class="bottom d-flex justify-content-between align-items-center"
            >
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
                <a :href="item.resource_url" download>
                    <button class="rounded">
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="18"
                            height="18"
                            fill="currentColor"
                            class="bi bi-arrow-down-short"
                            viewBox="0 0 16 16"
                        >
                            <path
                                fill-rule="evenodd"
                                d="M8 4a.5.5 0 0 1 .5.5v5.793l2.146-2.147a.5.5 0 0 1 .708.708l-3 3a.5.5 0 0 1-.708 0l-3-3a.5.5 0 1 1 .708-.708L7.5 10.293V4.5A.5.5 0 0 1 8 4z"
                            />
                        </svg>
                    </button>
                </a>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'UploadItem',
    props: ['item'],
    emits: ['itemDeleted'],
    methods: {
        handleDelete() {
            axios
                .delete(
                    `${process.env.VUE_APP_API}/api/items/${this.item.id}/detail`
                )
                .then(({ data }) => {
                    console.log('Deleted')
                    this.$emit('itemDeleted', this.item.id)
                })
                .catch((e) => console.log(e))
        },
    },
}
</script>

<style scoped>
a,
a:hover {
    text-decoration: none;
    color: white;
}

button {
    border: none;
    box-shadow: none;
    outline: none;
}
.overlay {
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    background-color: rgba(85, 79, 76, 0.4);
    width: 100%;
    height: 100%;
    transition: 0.5s ease;
    opacity: 0;
}

.card:hover .overlay {
    opacity: 1;
}

.top {
    position: absolute;
    top: 3%;
    right: 3%;
}

.bottom {
    position: absolute;
    bottom: 3%;
    left: 3%;
    right: 3%;
    color: white;
}

.profile-img {
    height: 40px;
    width: 40px;
    background: white;
    padding: 4px;
    border-radius: 50%;
}

.username {
    font-size: 0.8rem;
}
</style>