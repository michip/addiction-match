import Vue from 'vue'
import Main from './Main.vue'
import vuetify from './plugins/vuetify';
import router from './router'
import store from './store'

Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  store: store,
  render: h => h(Main)
}).$mount('#app')
