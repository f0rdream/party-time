// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Vuex from 'vuex'
import App from './App'
import router from './router'
import Mint from 'mint-ui'
import 'mint-ui/lib/style.css'
import './style/common.css'
import './config/resource'

Vue.config.productionTip = false
Vue.use(Vuex)
Vue.use(Mint)

const vuexStore = new Vuex.Store({
  state: {
    xxx: 'lala',
    addList: []// 定义你的数据源
  },
  mutations: {
    setAddList (state, addedList) {
      state.addList = addedList
    }
  }
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store: vuexStore,
  router,
  template: '<App/>',
  components: { App }
})
