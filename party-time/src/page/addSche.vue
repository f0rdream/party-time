<template>
  <div>
    <mt-header fixed title="日程添加" class="header">
      <mt-button @click="$router.go(-1)" slot="left" icon="back"></mt-button>
    </mt-header>
    <section class="main">
    <mt-navbar v-model="selected" class="outer">
      <div class="flex">
      <mt-tab-item id="1" class="change" >导入课表</mt-tab-item>
      <mt-tab-item id="2" class="change" >自由添加</mt-tab-item>
      </div>
      <mt-tab-container v-model="selected">
        <mt-tab-container-item id="1">
          <section>
          <mt-field label="系统账号" placeholder="请输入系统账号"></mt-field>
          <mt-field label="登录密码" placeholder="请输入登录密码"></mt-field>
          </section>
          <section>
          <mt-button type="default">登录</mt-button>
          </section>
        </mt-tab-container-item>
        <mt-tab-container-item id="2">
          <section>
            <mt-field label="名称" placeholder="请输入事件名称" v-model="affair.title"></mt-field>
            <mt-field label="地点" placeholder="请输入事件地点" v-model="affair.detail"></mt-field>
            <a class="mint-cell mint-field"><!---->
              <div class="mint-cell-left"></div>
              <div class="mint-cell-wrapper">
                <div class="mint-cell-title">
                  <!----> <span class="mint-cell-text">开始时间</span> <!---->
                </div>
                <div class="mint-cell-value">
                  <input type="datetime-local" class="mint-field-core" v-model="affair.start_time">
                  <div class="mint-field-clear" style="display: none;">
                    <i class="mintui mintui-field-error"></i></div>
                  <span class="mint-field-state is-default">
                    <i class="mintui mintui-field-default"></i>
                  </span>
                  <div class="mint-field-other">
                  </div>
                </div>
              </div>
              <div class="mint-cell-right"></div> <!---->
            </a>
            <a class="mint-cell mint-field"><!---->
              <div class="mint-cell-left"></div>
              <div class="mint-cell-wrapper">
                <div class="mint-cell-title">
                  <!----> <span class="mint-cell-text">结束时间</span> <!---->
                </div>
                <div class="mint-cell-value">
                  <input type="datetime-local" class="mint-field-core"  v-model="affair.end_time">
                  <div class="mint-field-clear" style="display: none;">
                    <i class="mintui mintui-field-error"></i></div>
                  <span class="mint-field-state is-default">
                    <i class="mintui mintui-field-default"></i>
                  </span>
                  <div class="mint-field-other">
                  </div>
                </div>
              </div>
              <div class="mint-cell-right"></div> <!---->
            </a>
          </section>

          <section class="button_section">
          <mt-button type="default" @click="submit">确认</mt-button>
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
        selected: '1',
        affair: {
          title: '',
          detail: '',
          start_time: '',
          end_time: ''
        }
      }
    },
    methods: {
      submit () {
        this.affair.start_time = this.affair.start_time + ':00Z'
        this.affair.end_time = this.affair.end_time + ':00Z'
        this.$http.post('tasks/create', this.affair).then(res => {
          if (res.title) {
            Toast('你已经创建任务' + res.title)
          }
        })
      }
    }
  }
</script>
<style>
.main{
  margin-top:40px;
}
.outer{
  flex-direction:column;
}
.flex{
  display: flex;
}
.button_section{
   margin-top:20px;
}
</style>
