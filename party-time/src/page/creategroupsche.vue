<template>
  <div>
    <mt-header title="创建群组日程">
      <mt-button @click="$router.go(-1)" slot="left" >取消</mt-button>
      <mt-button @click="$router.go(-1)" slot="right" @click.native="submit" >确定</mt-button>
    </mt-header>
    <section class="main-part">
      <section>
        <mt-field label="名称" placeholder="请输入事件名称" v-model="affair.title"></mt-field>
        <mt-field label="地点" placeholder="请输入事件地点" v-model="affair.detail"></mt-field>
        <mt-field label="开始时间" placeholder="请输入开始时间" v-model="showStart" @click.native="showPickerStart"></mt-field>
        <mt-field label="结束时间" placeholder="请输入结束时间" v-model="showEnd" @click.native="showPickerEnd"></mt-field>
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
    </section>
  </div>
</template>

<script>
  import { getMap } from '../config/store'
  import { Toast } from 'mint-ui'
  export default {
    data () {
      return {
        group_id: '',
        pickerstart: new Date(),
        pickerend: new Date(),
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
        this.$http.post('/group-agenda/' + this.group_id + '/post2', this.affair).then(res => {
          if (res.title) {
            Toast('你已经创建任务' + res.title)
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
      },
      group_id: function () {
        return getMap('group_id')
      }
    }
  }
</script>
<style scoped>

</style>
