import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Landing Page',
        component: Home
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
