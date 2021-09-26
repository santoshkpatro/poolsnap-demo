<template>
    <div class="card position-relative">
        <img :src="item.resource_url" class="card-img-top" alt="NA" />
        <div class="overlay">
            <div class="top">
                <a href="">
                    <button class="rounded">
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="20"
                            height="20"
                            fill="currentColor"
                            class="bi bi-cart-plus"
                            viewBox="0 0 16 16"
                        >
                            <path
                                d="M9 5.5a.5.5 0 0 0-1 0V7H6.5a.5.5 0 0 0 0 1H8v1.5a.5.5 0 0 0 1 0V8h1.5a.5.5 0 0 0 0-1H9V5.5z"
                            />
                            <path
                                d="M.5 1a.5.5 0 0 0 0 1h1.11l.401 1.607 1.498 7.985A.5.5 0 0 0 4 12h1a2 2 0 1 0 0 4 2 2 0 0 0 0-4h7a2 2 0 1 0 0 4 2 2 0 0 0 0-4h1a.5.5 0 0 0 .491-.408l1.5-8A.5.5 0 0 0 14.5 3H2.89l-.405-1.621A.5.5 0 0 0 2 1H.5zm3.915 10L3.102 4h10.796l-1.313 7h-8.17zM6 14a1 1 0 1 1-2 0 1 1 0 0 1 2 0zm7 0a1 1 0 1 1-2 0 1 1 0 0 1 2 0z"
                            />
                        </svg>
                    </button>
                </a>
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
    props: ['item'],
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