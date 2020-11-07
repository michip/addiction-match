import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Questionnaire from "@/views/Questionnaire"
import Matches from "@/views/Matches"
import SignUp from "@/views/SignUp";
import Login from "@/views/Login";
import Dashboard from "@/views/Dashboard";
import ChatWindow from "@/views/ChatWindow";

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'home',
        component: Home
    },
    {
        path: '/matches',
        name: 'matches',
        component: Matches
    },
    {
        path: '/questions',
        name: 'questions',
        component: Questionnaire
    },
    {
        path: '/signup',
        name: 'signup',
        component: SignUp
    },
    {
        path: '/login',
        name: 'login',
        component: Login
    },
    {
        path: '/chat',
        name: 'chat',
        component: ChatWindow
    },
    {
        path: '/dashboard',
        name: 'dashboard',
        component: Dashboard
    },
    {
        path: '/app',
        name: 'About',
        children: [
            {
                // UserProfile will be rendered inside User's <router-view>
                // when /user/:id/profile is matched
                path: 'about',
                component: import(/* webpackChunkName: "about" */ '../views/About.vue')
            },
        ],
        component: () => import(/* webpackChunkName: "about" */ '../App.vue')
    }
]

const router = new VueRouter({
    routes
})

export default router
