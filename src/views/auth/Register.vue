<template>
    <div class="container mt-5">
        <a-input v-model:value="formData.email" placeholder="Enter Email" />
        <a-button type="primary" @click="onSubmit">Submit</a-button>
    </div>
</template>

<script>
export default {
    name: 'Register',
    data() {
        return {
            formData: {
                email: null,
                password: null,
                confirmPassword: null,
            },
        }
    },
    methods: {
        onSubmit() {
            console.log(this.formData)
        },
    },
}
</script>

<style>
</style>