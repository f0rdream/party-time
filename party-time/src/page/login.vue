<template>
  <div>
    <mt-header title="登录">
      <mt-button @click="$router.push('personsche')" slot="left" icon="back"></mt-button>
    </mt-header>
    <section class="icon-part">
      <div class="icon-box">
        <img :src="picURI">
      </div>
    </section>
    <section class="main-part">
      <mt-field label="用户名" placeholder="请输入用户名" v-model="form.username" @blur="getPic"></mt-field>
      <mt-field label="密码" placeholder="请输入密码" v-model="form.password" type="password"></mt-field>
      <div class="cell-box">
        <check-box checkValue="remembered" label="记住登录" v-model="form.remembered"></check-box>
        <router-link to="/forgotten" class="" hidden>忘记密码</router-link>
      </div>
      <div class="middle-box cell-part">
        <mt-button type="primary" @click.native="login" class="btn-large">登录</mt-button>
        <router-link to="register" class="text-info">没有账号?注册</router-link>
      </div>
      <mt-button type="primary" @click.native="login" class="btn-large">登录</mt-button>
    </section>
  </div>
</template>

<script>
  import { Indicator, Toast } from 'mint-ui'
  import Router from '../router'
  import CheckBox from '../components/common/CheckBox'

  export default {
    components: {
      CheckBox
    },
    data () {
      return {
        picURI: '../assets/logo.png',
        form: {
          username: '',
          password: '',
          remembered: true
        }
      }
    },
    methods: {
      login () {
        Indicator.open('正在登陆...')
        this.$http.post('accounts/login/', this.form).then(res => {
          Indicator.close()
          Router.go(-1)
        }, res => {
          Indicator.close()
          Toast({
            message: '登陆失败',
            position: 'bottom',
            duration: 2000
          })
          window.console.log(res)
        })
      },
      getPic () {
        this.$http.get(`accounts/${this.form.username}/load-picture/`).then(res => {
          this.picURI = res.body.picture
        })
      }
    }

  }
</script>
<style scoped>
  .icon-part {
    display: flex;
    height: 24rem;
  }
  .icon-box {
    margin: auto;
  }
  .icon-box img {
    width: 10rem;
    height: 10rem;
  }
  .cell-part {
    margin-top: 5rem;
  }t
  .text-info {
    margin-top: 1rem;
    color: #9c9c9c;
    font-size: 1.2rem;
  }
</style>
