import { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
    state: {
        user: null,
    },
    mutations: {
        SET_USER_DATA(state, userData) {
            localStorage.setItem('user', JSON.stringify(userData))
            axios.defaults.headers.common[
                'Authorization'
            ] = `Bearer ${userData.token}`
            state.user = userData
        },
        CLEAR_USER_DATA() {
            localStorage.removeItem('user')
            location.reload()
        },
        SET_CLASSROOM(state, classroom) {
            state.selectedClassroom = classroom
        },
    },
    actions: {
        register({ commit }, credentials) {
            return axios
                .post('//localhost:3000/register', credentials)
                .then(({ data }) => {
                    commit('SET_USER_DATA', data)
                })
        },
        login({ commit }, credentials) {
            return axios
                .post(`${process.env.VUE_APP_API}/api/auth/login/`, credentials)
                .then(({ data }) => {
                    commit('SET_USER_DATA', data)
                })
        },
        logout({ commit }) {
            commit('CLEAR_USER_DATA')
        },
    },
    modules: {},
    getters: {
        loggedIn(state) {
            return !!state.user
        },
        getUser(state) {
            return state.user
        },
    },
})
