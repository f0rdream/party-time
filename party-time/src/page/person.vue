<template>
  <div>
    <mt-header fixed title="个人信息">
      <mt-button slot="right" @click="editDone"><span>{{ editable ? '完成' : '编辑'}}</span></mt-button>
    </mt-header>
    <section class="icon-part">
      <div class="icon-box">
        <img src="../assets/logo.png">
      </div>
    </section>
    <section class="main-part">
      <mt-field label="用户名" :readonly="!editable" v-model="form.username"></mt-field>
      <mt-field label="真实姓名" :readonly="!editable" v-model="form.realname"></mt-field>
      <mt-field label="手机" :readonly="!editable" v-model="form.phone"></mt-field>
      <mt-field label="邮箱" :readonly="!editable" v-model="form.email"></mt-field>
      <mt-field label="学号" :readonly="!editable" v-model="form.stuId"></mt-field>
      <mt-field label="自我介绍" type="textarea" :readonly="!editable" rows="4" v-model="form.description"></mt-field>
    </section>
    <tab-bar select-item="个人" fixed-props="true"></tab-bar>
  </div>
</template>

<script>
  import { Toast } from 'mint-ui'
  import TabBar from '../components/TabBar'
  export default {
    components: {
      TabBar
    },
    data () {
      return {
        editable: false,
        form: {
          username: '',
          realname: '',
          phone: '',
          email: '',
          stuId: '',
          description: ''
        }
      }
    },
    mounted () {
      this.initData()
    },
    methods: {
      initData () {
        this.$http.get('accounts/').then(res => {
          this.form.username = res.body.username
          this.form.realname = res.body.realname
          this.form.phone = res.body.phone
          this.form.email = res.body.email
          this.form.stuId = res.body.user_stu_id
          this.form.description = res.body.description
        }, res => {
        })
      },
      editDone () {
        if (!this.editable) {
          this.editable = true
        } else {
          this.$http.post('/accounts/', this.form).then(res => {
            Toast({
              message: '更新成功',
              position: 'bottom',
              duration: 1500
            })
            this.editable = false
          }, res => {
            Toast({
              message: '更新失败',
              position: 'bottom',
              duration: 1500
            })
          })
        }
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
