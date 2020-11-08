import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersist from 'vuex-persist'

const axios = require("axios").default;

Vue.use(Vuex)

const vuexPersist = new VuexPersist({
    key: 'help-me-help-you',
    storage: window.localStorage
})

const store = new Vuex.Store({
    state: {
        answeredQuestions: [],
        profileInfo: null,
        accessToken: null
    },
    mutations: {
        addQuestion(state, question) {
            state.answeredQuestions.push(question)
        },
        clear(state) {
            state.answeredQuestions = []
        },
        addProfileInfo(state, profileInfo) {
            state.profileInfo = profileInfo
        },
        logout(state) {
            state.accessToken = null;
        },
        saveToken(state, token) {
            state.accessToken = token
        }
    },
    actions: {
        async login({commit, state}, credentials) {
            try {
                let response = await axios.post('http://40.115.33.104:8000/api/token/', {
                    'username': credentials.name,
                    'password': credentials.password
                })
                if (response.status === 200) {
                    commit('saveToken', response.data.access)
                    return true
                }
                return false
            } catch (e) {
                return false
            }
        }
    },
    plugins: [vuexPersist.plugin]
})

export default store