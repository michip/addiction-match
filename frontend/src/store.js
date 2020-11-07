import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersist from 'vuex-persist'

Vue.use(Vuex)

const vuexPersist = new VuexPersist({
    key: 'help-me-help-you',
    storage: window.localStorage
})

const store = new Vuex.Store({
    state: {
        answeredQuestions: []
    },
    mutations: {
        addQuestion(state, question) {
            state.answeredQuestions.push(question)
        },
        clear(state) {
            state.answeredQuestions = []
        }
    },
    actions: {
        previousQuestion({state}) {
            return state.answeredQuestions.pop()
        }
    },
    plugins: [vuexPersist.plugin]
})

export default store