<template>
  <div>
    <mt-header fixed title="注册">
      <mt-button @click="$router.go(-1)" slot="left" icon="back"></mt-button>
    </mt-header>
    <section>
      <mt-field label="用户名" placeholder="请输入用户名" v-model="form.username"></mt-field>
      <mt-field label="密码" placeholder="请输入密码" v-model="form.password"></mt-field>
      <mt-button type="primary" @click.native="login">登录</mt-button>
      <mt-switch v-model="remembered">记住登录状态</mt-switch>
    </section>
  </div>
</template>

<script>
import Router from '../router'

export default {
  data () {
    return {
      remembered: true,
      form: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    login () {
      this.$http.post('auth/token/', this.form).then(res => {
        if (remembered) {
          this.$cookie.set('token', res.token, 30)
          this.$cookie.set('username', this.form.username, 30)
        } else {
          this.$cookie.set('token', res.token, -1)
          this.$cookie.set('username', this.form.username, -1)
        }
        window.console.log('login successfully')
        Router.go(-1)
      }, res => {
        window.console.log(res.body)
      })
    },
    init ()
  }

}
</script>
<style scoped>
</style>
