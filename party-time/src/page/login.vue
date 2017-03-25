<template>
  <div>
    <mt-header title="登录">
      <mt-button @click="$router.go(-1)" slot="left" icon="back"></mt-button>
    </mt-header>
    <section class="icon-part">
      <div class="icon-box">
        <img src="../assets/logo.png">
      </div>
    </section>
    <section class="main-part">
      <mt-field label="用户名" placeholder="请输入用户名" v-model="form.username"></mt-field>
      <mt-field label="密码" placeholder="请输入密码" v-model="form.password"></mt-field>
      <div class="cell-box">
        <check-box checkValue="lala" label="记住登录"></check-box>
        <router-link to="/forgotten" >忘记密码</router-link>
      </div>
      <mt-button type="primary" @click.native="login">登录</mt-button>
    </section>
  </div>
</template>

<script>
import Router from '../router'
import CheckBox from '../components/common/CheckBox'

export default {
  components: {
    CheckBox
  },
  data () {
    return {
      value: [''],
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
        if (this.remembered) {
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
    }
  }

}
</script>
<style scoped>
.icon-part {
  display: flex;
  height: 30rem;
}
.icon-box {
  margin: auto;
}
.icon-box img {
  width: 10rem;
  height: 10rem;
}
</style>
