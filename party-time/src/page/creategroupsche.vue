<template>
  <div>
    <mt-header title="创建群组日程">
      <mt-button @click="$router.go(-1)" slot="left" >取消</mt-button>
      <mt-button @click="$router.go(-1)" slot="left" >取消</mt-button>
    </mt-header>
    <section class="icon-part">
      <div class="icon-box">
        <img src="../assets/logo.png">
      </div>
    </section>
    <section class="main-part">
      <mt-field label="用户名" placeholder="请输入用户名" v-model="form.username"></mt-field>
      <mt-field label="密码" placeholder="请输入密码" v-model="form.password" type="password"></mt-field>
      <div class="cell-box">
        <check-box checkValue="remembered" label="记住登录" v-model="form.remembered"></check-box>
        <router-link to="/forgotten" class="">忘记密码</router-link>
      </div>
      <mt-button type="primary" @click.native="login">登录</mt-button>
    </section>
  </div>
</template>

<script>
  import { Indicator, Toast } from 'mint-ui'
  import Router from '../router'
  import CheckBox from '../components/common/CheckBox'
  import { setMap } from '../config/store'

  export default {
    components: {
      CheckBox
    },
    data () {
      return {
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
        this.$http.post('auth/token/', this.form).then(res => {
          Indicator.close()
          setMap('isLogin', true)
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
