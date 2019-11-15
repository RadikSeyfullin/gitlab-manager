<template>
    <div>
        <h1>GITLAB-MANAGER</h1>
        <button v-if="!auth" @click="goLogin">Login</button>
        <button v-else @click="signOut">Выход</button>
        <button v-if="auth" @click="goUser">Показать юзера</button>
    </div>
</template>

<script>

export default {
    name: "Home",
    computed: {
        auth() {
            if (sessionStorage.getItem('auth_token')) {
                return true
            }
        }
    },
    methods: {
        goLogin() {
            this.$router.push({name: "login"})
        },
        signOut() {
            sessionStorage.removeItem('auth_token')
            window.location = '/'
        },
        goUser() {
            this.$router.push({name: 'user'})
        }
    },
}
</script>