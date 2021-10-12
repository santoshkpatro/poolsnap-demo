<template>
    <div class="form-signin container mt-5">
        <form @submit.prevent="handleLogin">
            <!-- <img
                class="mb-4"
                src="../assets/brand/bootstrap-logo.svg"
                alt=""
                width="72"
                height="57"
            /> -->
            <h1 class="h3 mb-3 fw-normal">Please sign in</h1>
            <div class="form-floating">
                <input
                    type="text"
                    class="form-control"
                    id="floatingInput"
                    placeholder="name@example.com"
                    v-model="formState.username"
                />
                <label for="floatingInput">username or email</label>
            </div>
            <div class="form-floating">
                <input
                    type="password"
                    class="form-control"
                    id="floatingPassword"
                    placeholder="Password"
                    v-model="formState.password"
                />
                <label for="floatingPassword">password</label>
            </div>
            <button class="w-100 btn btn-lg btn-dark" type="submit">
                Sign in
            </button>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            formState: {
                username: null,
                password: null,
            },
            isLoading: false,
        }
    },
    methods: {
        handleLogin() {
            this.isLoading = true
            this.$store
                .dispatch('login', this.formState)
                .then(() => {
                    this.isLoading = false
                    if (this.$route.query.redirect) {
                        this.$router.push(this.$route.query.redirect)
                    } else {
                        this.$router.push({ name: 'Home' })
                    }
                })
                .catch((err) => {
                    this.isLoading = false
                })
        },
    },
}
</script>

<style scoped>
.form-signin {
    width: 100%;
    max-width: 330px;
    padding: 15px;
    margin: auto;
}

.form-signin .checkbox {
    font-weight: 400;
}

.form-signin .form-floating:focus-within {
    z-index: 2;
}

.form-signin input[type='email'] {
    margin-bottom: -1px;
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0;
}

.form-signin input[type='password'] {
    margin-bottom: 10px;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
}
</style>