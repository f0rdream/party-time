<template>
  <div id="app">
    <transition name="router-fade" mode="out-in">
      <router-view></router-view>
    </transition>
  </div>
</template>

<script>
  import { setMap } from './config/store'
  export default {
    name: 'app',
    mounted () {
      this.isLogin()
    },
    methods: {
      isLogin () {
        this.$http.get('isLogin').then(res => {
          console.log(res)
          if (res.data) {
            setMap('isLogin', true)
          } else {
            this.$router.go('/login')
          }
        }, res => {
          window.console.log('Failed for some reasons')
        })
      }
    }
  }
</script>


<style>
  #app {
    font-size: 1.6rem;
  }
</style>
