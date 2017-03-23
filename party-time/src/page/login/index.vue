<template>
  <div>
    <mt-field label="用户名" placeholder="请输入用户名" v-model="form.username"></mt-field>
    <mt-field label="密码" placeholder="请输入密码" v-model="form.password"></mt-field>
    <mt-button type="primary" @click.native="login">登录</mt-button>
  </div>
</template>

<script>
export default {
  data () {
    return {
      form: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    login () {
      return this.$http.post('accounts/login/', this.form).then(({data}) => {
        window.console.log(data)
      })
    }
  }

}
</script>
