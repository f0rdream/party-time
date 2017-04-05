import Vue from 'vue'
import VueResource from 'vue-resource'
import Router from '../router'
import baseUrl from './env'

Vue.use(VueResource)

Vue.http.options.root = baseUrl

function clean (obj) {
  for (let key in obj) {
    if ((obj[key] == null) || (obj[key] === '')) {
      delete obj[key]
    }
  }
}

// emlulate json if the server don't suppot json
// Vue.http.options.emulateJSON = true

Vue.http.interceptors.push({
  request: (request) => {
    let ret = Object.assign({}, request)
    clean(ret.data)
    clean(ret.params)
    return ret
  },
  response: (response) => {
    let res = Object.assign({}, response)
    if (res.ok) {
      if (res.data.status && Number(res.data.status) !== 0) {
        res.ok = false
      } else if (res.status === 403) {
        Router.replace('/login')
      }
    }
    return res
  }
})
