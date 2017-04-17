import Vue from 'vue'
import Router from 'vue-router'

import Hello from '@/components/Hello'
import home from '@/page/home'
import group from '@/page/group'
import login from '@/page/login'
import person from '@/page/person'
import register from '@/page/register'
import addsche from '@/page/addsche'
import creategroupsche from '@/page/creategroupsche'
import creategroup from '@/page/creategroup'
import mygroup from '@/page/mygroup'
import groupmessage from '@/page/groupmessage'
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
      path: '/addsche',
      component: addsche
    },
    {
      path: '/creategroup',
      component: creategroup
    },
    {
      path: '/creategroupsche',
      component: creategroupsche
    },
    {
      path: '/mygroup',
      component: mygroup
    },
    {
      path: '/groupmessage',
      component: groupmessage
    }

  ]
})
