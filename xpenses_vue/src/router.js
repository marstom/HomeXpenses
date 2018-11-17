import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Header from './views/Header.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      components:{
        default: Home,
        'header-top': Header
      }
    },
    {
      path: '/info',
      name: 'info',
      components: {
        default: () => import(/* webpackChunkName: "about" */ './views/Info.vue'),
        'header-top': Header
      }
    },
    {
      path: '/add',
      name: 'add',
      components: {
        default: () => import(/* webpackChunkName: "about" */ './views/AddExpense.vue'),
        'header-top': Header
      }
    },
  ]
})
