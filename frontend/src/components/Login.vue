<template>
    <div>
        <input type="text" v-model="login" placeholder="Login">
        <input type="password" v-model="password" placeholder="Password">
        <button @click="loginIn">Войти</button>
    </div>
</template>

<script>
import $ from 'jquery'

export default {
    name: "Login",
    data() {
        return {
            login: "",
            password: "",
        }
    },
    methods: {
        loginIn() {
            $.ajax({
                url: 'http://127.0.0.1:8000/auth/token/login/',
                type: 'POST',
                data: {
                    username: this.login,
                    password: this.password
                }
            }).then(res => {
                sessionStorage.setItem('auth_token', res.data.attributes.auth_token)
                this.$router.push({name: "home"})
            }).catch(err => {
                console.log(err)
            });
        },
    }
}
</script>

<style scoped>
 
</style>