<template>
  <div>
    <mt-header title="注册">
      <mt-button @click="$router.go(-1)" slot="left" icon="back"></mt-button>
    </mt-header>
    <section class="page-part">
      <mt-field label="用户名" placeholder="请输入用户名" v-model="form.username"></mt-field>
      <mt-field label="密码" placeholder="请输入密码" v-model="form.password" type="password"></mt-field>
      <mt-field label="密码" placeholder="确认密码" type="password"></mt-field>
    </section>
    <section class="page-part">
      <mt-field label="真实姓名" placeholder="方便您的朋友找到您" v-model="form.realname"></mt-field>
      <mt-field label="手机" placeholder="请输入您的手机号" type="tel" v-model="form.phone"></mt-field>
      <mt-field label="邮箱" placeholder="请输入您的邮箱" type="email" v-model="form.email"></mt-field>
      <mt-field label="学号" placeholder="请输入您的学号" v-model="form.user_stu_id"></mt-field>
    </section>
    <section class="page-part middle-box">
      <mt-button type="primary" @click.native="register" class="btn-large">立即注册</mt-button>
      <router-link to="login" class="text-info">已有账号？点击登录</router-link>
    </section>
  </div>
</template>

<script>

  export default {
    data () {
      return {
        form: {
          username: '',
          password: '',
          realname: '',
          phone: '',
          email: '',
          user_stu_id: ''
        },
        wait: false
      }
    },
    methods: {
      register () {
        this.wait = true
        this.$http.post('accounts/register/', this.form).then(res => {
          window.console.log('It\'s OK:' + res.body)
          this.wait = false
        }, res => {
          window.console.log('Error happend:' + res.body)
          this.wait = false
        })
      }
    }

  }
</script>
<style scoped>
  .middle-box {
    margin-top: 1.5rem;
  }
  .text-info {
    margin-top: 1rem;
  }
</style>
