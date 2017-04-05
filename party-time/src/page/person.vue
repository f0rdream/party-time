<template>
  <div>
    <mt-header fixed title="个人信息">
      <mt-button @click="$router.go(-1)" slot="left" icon="back"></mt-button>
      <mt-button icon="more" slot="right"></mt-button>
    </mt-header>
    <section class="icon-part">
      <div class="icon-box">
        <img src="../assets/logo.png">
      </div>
    </section>
    <section class="main-part">
      <mt-field label="用户名" value="fordream" readonly v-model="username"></mt-field>
      <mt-field label="账号" value="fordream" readonly v-model="account"></mt-field>
      <mt-field label="真实姓名" value="fordream" readonly v-model="name"></mt-field>
      <mt-field label="自我介绍" type="textarea" rows="4" readonly v-model="description"></mt-field>
    </section>
  </div>
</template>

<script>

  export default {
    data () {
      return {
        username: '',
        account: '',
        name: '',
        description: ''
      }
    },
    mounted () {
      this.initData()
    },
    methods: {
      initData () {
        this.$http.get('/accounts/<user_stu_id>/')
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
