<template>
  <div>
    <mt-header  title="日程添加" class="header">
      <mt-button @click="$router.go(-1)" slot="left" icon="back"></mt-button>
    </mt-header>
    <section class="main-part">
      <mt-navbar v-model="selected" class="outer">
        <div class="flex">
        <mt-tab-item id="1" class="change" >导入课表</mt-tab-item>
        <mt-tab-item id="2" class="change" >自由添加</mt-tab-item>
        </div>
        <mt-tab-container v-model="selected">
          <mt-tab-container-item id="1">
            <section>
            <mt-field label="系统账号" placeholder="请输入系统账号" v-model="student.user_stu_id"></mt-field>
            <mt-field label="登录密码" placeholder="请输入登录密码" v-model="student.user_stu_pwd"></mt-field>
            <mt-field label="验证码" placeholder="请输入登录密码" v-model="student.yzm_text"></mt-field>
            <img v-bind:src="yzm_url" class="yzm">
            </section>
            <section class="button-section">
            <mt-button type="default" class="btn-large" @click.native="getYZM">得到验证码</mt-button>
            <mt-button type="default" class="btn-large" @click.native="login">登录</mt-button>
            </section>
          </mt-tab-container-item>
          <mt-tab-container-item id="2">
            <section>
              <mt-field label="名称" placeholder="请输入事件名称" v-model="affair.title"></mt-field>
              <mt-field label="地点" placeholder="请输入事件地点" v-model="affair.detail"></mt-field>
              <mt-field label="开始时间" placeholder="请输入开始时间" v-model="showStart" @click.native="showPickerStart"></mt-field>
              <mt-field label="结束时间" placeholder="请输入结束时间" v-model="showEnd" @click.native="showPickerEnd"></mt-field>
            </section>

            <section class="button-section">
            <mt-button type="default" @click="submit" class="btn-large">确认</mt-button>
            </section>
            <section>
              <mt-datetime-picker
                ref="pickerstart"
                v-model="pickerstart"
                type="datetime"
                @comfirm="closePickerStart"
              >
              </mt-datetime-picker>
                <mt-datetime-picker
                  ref="pickerend"
                  v-model="pickerend"
                  type="datetime"
                  @comfirm="closePickerEnd"
                >
                </mt-datetime-picker>
            </section>
          </mt-tab-container-item>
        </mt-tab-container>
      </mt-navbar>
    </section>

  </div>
</template>
<script>
  import { Toast } from 'mint-ui'
  export default {
    data () {
      return {
        yzm_url: '',
        pickerstart: new Date(),
        pickerend: new Date(),
        selected: '1',
        affair: {
          title: '',
          detail: '',
          start_time: '',
          end_time: ''
        },
        student: {
          yzm_cookie: '',
          yzm_text: '',
          user_stu_id: '',
          user_stu_pwd: ''
        }
      }
    },
    methods: {
      submit () {
        this.affair.start_time = this.pickerstart.getFullYear() + '-' + ((this.pickerstart.getMonth() + 1) < 10 ? '0' +
            (this.pickerstart.getMonth() + 1) : (this.pickerstart.getMonth() + 1)) +
          '-' + (this.pickerstart.getDate() < 10 ? '0' + this.pickerstart.getDate() : this.pickerstart.getDate()) + 'T' +
          (this.pickerstart.getHours() < 10 ? '0' + this.pickerstart.getHours() : this.pickerstart.getHours()) + ':' +
          (this.pickerstart.getMinutes() < 10 ? '0' + this.pickerstart.getMinutes() : this.pickerstart.getMinutes()) + ':00Z'
        this.affair.end_time = this.pickerend.getFullYear() + '-' + ((this.pickerend.getMonth() + 1) < 10 ? '0' +
            (this.pickerend.getMonth() + 1) : (this.pickerend.getMonth() + 1)) +
          '-' + (this.pickerend.getDate() < 10 ? '0' + this.pickerend.getDate() : this.pickerend.getDate()) + 'T' +
          (this.pickerend.getHours() < 10 ? '0' + this.pickerend.getHours() : this.pickerend.getHours()) + ':' +
          (this.pickerend.getMinutes() < 10 ? '0' + this.pickerend.getMinutes() : this.pickerend.getMinutes()) + ':00Z'
        this.$http.post('tasks/create/', this.affair, {headers: {
          'X-CSRFToken': localStorage.csrftoken
        }}).then(res => {
          if (res.body.title) {
            Toast('你已经创建任务' + res.body.title)
          }
        }, res => {
          Toast('创建失败' + res.body.title)
        })
      },
      login () {
        this.$http.post('/courses/', this.student, {headers: {
          'X-CSRFToken': localStorage.csrftoken
        }}).then(res => {
          if (res.ok) {
            this.$router.push('personsche')
          } else {
            Toast({
              message: '登陆失败',
              position: 'bottom',
              duration: 2000
            })
          }
        }, res => {
          Toast({
            message: '登陆失败',
            position: 'bottom',
            duration: 2000
          })
        })
      },
      getYZM () {
        this.$http.get('/courses/yzm').then(res => {
          if (res.body.yzm_cookie) {
            console.log(res.body)
            this.student.yzm_cookie = res.body.yzm_cookie
          }
          if (res.body.yzm_url) {
            this.yzm_url = res.body.yzm_url
          }
        })
      },
      showPickerStart () {
        this.$refs.pickerstart.open()
      },
      showPickerEnd () {
        this.$refs.pickerend.open()
      },
      closePickerStart () {
        this.$refs.pickerstart.close()
      },
      closePickerEnd () {
        this.$refs.pickerend.close()
      }
    },
    computed: {
      showStart: function () {
        return this.pickerstart.getFullYear() + '-' + ((this.pickerstart.getMonth() + 1) < 10 ? '0' +
            (this.pickerstart.getMonth() + 1) : (this.pickerstart.getMonth() + 1)) +
          '-' + (this.pickerstart.getDate() < 10 ? '0' + this.pickerstart.getDate() : this.pickerstart.getDate()) + '-' +
          (this.pickerstart.getHours() < 10 ? '0' + this.pickerstart.getHours() : this.pickerstart.getHours()) + '-' +
          (this.pickerstart.getMinutes() < 10 ? '0' + this.pickerstart.getMinutes() : this.pickerstart.getMinutes())
      },
      showEnd: function () {
        return this.pickerend.getFullYear() + '-' + ((this.pickerend.getMonth() + 1) < 10 ? '0' +
            (this.pickerend.getMonth() + 1) : (this.pickerend.getMonth() + 1)) +
          '-' + (this.pickerend.getDate() < 10 ? '0' + this.pickerend.getDate() : this.pickerend.getDate()) + '-' +
          (this.pickerend.getHours() < 10 ? '0' + this.pickerend.getHours() : this.pickerend.getHours()) + '-' +
          (this.pickerend.getMinutes() < 10 ? '0' + this.pickerend.getMinutes() : this.pickerend.getMinutes())
      }
    }
  }
</script>
<style scoped>

.outer{
  flex-direction:column;
}
.flex{
  display: flex;
}
.button-section{
  padding-top:2rem;
  background: rgb(232,232,232);
}
.main-part {
  background: rgb(232,232,232)
}
.yzm{
  margin-top:20px;
}


</style>
