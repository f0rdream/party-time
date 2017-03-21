import Vue from 'vue'
import Router from 'vue-router'

import Hello from '@/components/Hello'
import home from '@/page/home'
import group from '@/page/group/index'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: Hello
    },
    {
      path: '/group',
      name: 'group',
      component: group
    },
    {
      path: '/home',
      name: 'home',
      component: home
    }
  ]
})
