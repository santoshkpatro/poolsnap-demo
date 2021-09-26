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
                    v-model="credentials.username"
                />
                <label for="floatingInput">Email address</label>
            </div>
            <div class="form-floating">
                <input
                    type="password"
                    class="form-control"
                    id="floatingPassword"
                    placeholder="Password"
                    v-model="credentials.password"
                />
                <label for="floatingPassword">Password</label>
            </div>
            <button class="w-100 btn btn-lg btn-primary" type="submit">
                Sign in
            </button>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            credentials: {
                username: null,
                password: null,
            },
            error: null,
        }
    },
    methods: {
        handleLogin() {
            this.$store
                .dispatch('login', this.credentials)
                .then(() => {
                    if (this.$route.query.redirect) {
                        this.$router.push(this.$route.query.redirect)
                    } else {
                        this.$router.push({ name: 'Home' })
                    }
                })
                .catch((err) => (this.error = err.response.data.error))
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