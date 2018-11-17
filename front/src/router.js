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
        Home,
        'header-top': Header
      } 
    },
    {
      path: '/about',
      name: 'about',
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    }
  ]
})
