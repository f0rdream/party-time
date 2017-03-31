import Vue from 'vue'
import Router from 'vue-router'

import Hello from '@/components/Hello'
import home from '@/page/home'
import group from '@/page/group'
import login from '@/page/login'
import person from '@/page/person'
import register from '@/page/register'
import addSche from '@/page/addSche'
import createGroup from '@/page/createGroup'

Vue.use(Router)

export default new Router({
  mode: 'history',
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
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/register',
      name: 'register',
      component: register
    },
    {
      path: '/person',
      component: person
    },
    {
      path: '/addSche',
      component: addSche
    },
    {
      path: '/createGroup',
      component: createGroup
    }

  ]
})
