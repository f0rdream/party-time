// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VueResource from 'vue-resource'
import Mint from 'mint-ui'
import 'mint-ui/lib/style.css'
import './style/common.css'
import baseUrl from './config/env'

Vue.config.productionTip = false
Vue.use(VueResource)
Vue.use(Mint)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
  // http: {
  //   root: '//125.01.01.0'
  // }
})

Vue.http.options.root = baseUrl.baseUrl
