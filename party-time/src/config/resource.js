import Vue from 'vue'
import VueResource from 'vue-resource'
// import Router from '../router'

Vue.use(VueResource)

Vue.http.options.credentials = true

// function clean (obj) {
//   for (let key in obj) {
//     if ((obj[key] == null) || (obj[key] === '')) {
//       delete obj[key]
//     }
//   }
// }

// emlulate json if the server don't suppot json
// Vue.http.options.emulateJSON = true

// Vue.http.interceptors.push(function (request, next) {
//   let ret = Object.assign({}, request)
//   clean(ret.data)
//   clean(ret.params)
//   return ret
// })
