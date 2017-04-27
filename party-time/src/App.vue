<template>
  <div id="app">
    <transition name="router-fade" mode="out-in">
      <router-view></router-view>
    </transition>
  </div>
</template>

<script>
  export default {
    name: 'app',
    methods: {
      isLogin () {
        this.$http.get('accounts/is-login/').then(res => {
          if (!res.data) {
            this.$router.push('login')
          }
        }, res => {
          this.$router.push('login')
          window.console.log('Failed for some reasons')
        })
      },
      getCsrf () {
        let cookie = window.document.cookie.match('(^|;) ?' + 'csrftoken' + '=([^;]*)(;|$)')
        let csrftoken = ''
        if (cookie) {
          csrftoken = cookie[2]
        }
        localStorage.csrftoken = csrftoken
      }
    },
    mounted () {
      this.isLogin()
      this.getCsrf()
    }
  }
</script>


<style>
  #app {
    font-size: 1.6rem;
    height: 100%;
  }
</style>
