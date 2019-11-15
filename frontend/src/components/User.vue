<template>
    <div>
        <h4>UID: {{ user.uid }}</h4>
        <h1>{{ user.name }}</h1>
        <hr>
        <h2>All your projects:</h2>
        <div v-for="project in projects" :key="project.pid">
            <h1>{{ project.name }}</h1>
            <h3>{{ project.pid }}</h3>
            <h5>{{ project.created_at }}</h5>
            <h6>{{ project.creator.username }}</h6>
        </div>
    </div>
</template>

<script>
import $ from 'jquery'
import axios from 'axios'

export default {
    name: "User",
    data() {
        return {
            user: null,
            projects: null
        }
    },
    methods: {
        loadUser() {
            axios({
                method: 'get',
                url: 'http://127.0.0.1:8000/api/v1/user/',
                headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')}
            }).then(res => {
                this.user = res.data.data.data
            }).catch(err => {
                console.log(err)
            })
        },
        loadProjects() {
            axios({
                method: 'get',
                url: 'http://127.0.0.1:8000/api/v1/user/projects/',
                headers: {'Authorization': 'Token ' + sessionStorage.getItem('auth_token')}
            }).then(res => {
                this.projects = res.data.data.data
            }).catch(err => {
                console.log(err)
            })
        },
    },
    created() {
        this.loadUser(),
        this.loadProjects()
    }
}
</script>

<style scoped>
 
</style>