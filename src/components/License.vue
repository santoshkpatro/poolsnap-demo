<template>
    <div class="card position-relative">
        <img :src="license.item.resource_url" class="card-img-top" alt="NA" />
        <div class="overlay">
            <div class="top">
                <a href="">
                    <span
                        class="badge bg-danger"
                        v-if="valid_upto > 0 ? false : true"
                        >Expired</span
                    >
                    <span
                        class="badge bg-success"
                        v-if="valid_upto > 0 ? true : false"
                        >Valid</span
                    >
                </a>
            </div>
            <div
                class="bottom d-flex justify-content-between align-items-center"
            >
                <router-link
                    :to="{
                        name: 'Profile',
                        params: { username: license.item.owner.username },
                    }"
                >
                    <div class="d-flex align-items-center">
                        <img
                            :src="license.item.owner.profile_url"
                            alt="NA"
                            class="profile-img"
                        />
                        <div class="d-flex flex-column ms-2">
                            <span>{{ license.item.owner.name }}</span>
                            <span class="username"
                                >@{{ license.item.owner.username }}</span
                            >
                        </div>
                    </div>
                </router-link>
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
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['license'],
    computed: {
        valid_upto: function () {
            const valid = new Date(this.license.valid_upto)
            const today = new Date()
            const diffTime = valid - today
            const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24))
            return diffDays
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