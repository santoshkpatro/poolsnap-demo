<template>
    <ul class="nav mb-3">
        <li class="nav-item">
            <a class="nav-link" href="#">Oveview</a>
        </li>
        <li class="nav-item">
            <router-link
                class="nav-link"
                :to="{
                    name: 'Uploads',
                }"
                >Uploads</router-link
            >
        </li>
        <li class="nav-item">
            <router-link
                class="nav-link"
                :to="{
                    name: 'Rights',
                }"
                >Rights</router-link
            >
        </li>
        <li class="nav-item">
            <a class="nav-link" href="#">Orders</a>
        </li>
    </ul>
</template>

<script>
export default {
    name: 'Tabs',
}
</script>

<style scoped>
li a {
    text-decoration: none;
    color: black;
}

.router-link-active {
    border-bottom: 2px solid black;
}
</style>