<template>
  <div>
    <mt-header title="个人信息">
      <mt-button slot="left" @click="$router.go(-1)" icon="back"></mt-button>
      <mt-button slot="right" @click="editDone"><span>{{ editable ? '完成' : '编辑'}}</span></mt-button>
    </mt-header>
    <section class="icon-part">
      <div class="icon-box">
        <img src="../assets/logo.png">
      </div>
    </section>
    <section class="main-part">
      <mt-field label="用户名" v-model="form.user"></mt-field>
      <mt-field label="真实姓名" :readonly="!editable" v-model="form.real_name"></mt-field>
      <mt-field label="手机" :readonly="!editable" v-model="form.phone_number"></mt-field>
      <mt-field label="邮箱" :readonly="!editable" v-model="form.email"></mt-field>
      <mt-field label="学号" :readonly="!editable" v-model="form.user_stu_id"></mt-field>
      <mt-field label="自我介绍" type="textarea" :readonly="!editable" rows="4" v-model="form.description" class="description"></mt-field>
    </section>
    <tab-bar select-item="个人" :fixed-props="true"></tab-bar>
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
          user: '',
          real_name: '',
          phone_number: '',
          email: '',
          user_stu_id: '',
          description: '',
          picture: ''
        }
      }
    },
    mounted () {
      this.initData()
    },
    methods: {
      initData () {
        this.$http.get('accounts/profile-detail/').then(res => {
          this.form.user = res.body[0].user
          this.form.real_name = res.body[0].real_name
          this.form.phone_number = res.body[0].phone_number
          this.form.email = res.body[0].email
          this.form.user_stu_id = res.body[0].user_stu_id
          this.form.description = res.body[0].description
          this.form.picture = res.body[0].picture
        }, res => {
        })
      },
      editDone () {
        let cookie = window.document.cookie.match('(^|;) ?' + 'csrftoken' + '=([^;]*)(;|$)')
        let csrftoken = ''
        if (cookie) {
          csrftoken = cookie[2]
        }

        if (!this.editable) {
          this.editable = true
        } else {
          this.$http.put('accounts/profile-detail/update', this.form, {headers: {
            'X-CSRFToken': csrftoken
          }}).then(res => {
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
    height: 15rem;
  }
  .icon-box {
    margin: auto;
  }
  .icon-box img {
    width: 5rem;
    height: 5rem;
  }
  .description {
    margin-top: 1rem;
  }
</style>
