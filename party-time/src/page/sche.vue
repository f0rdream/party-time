<template>
  <div class="app-wrapper">
    <mt-header title="群组日程" class="header">
      <mt-button @click="$router.push('mygroup')" slot="left" icon="back">群组</mt-button>
      <mt-button slot="right" @click="$router.push('creategroupsche')">
        <i class="iconm--plus" slot="icon"></i>
      </mt-button>
      <mt-button slot="right" @click="$router.push('groupmessage')">
        <img src="../assets/personal.svg" height="30" width="30" slot="icon" class="person-icon">
      </mt-button>
    </mt-header>
    <section class="main-part">
      <div class="col-day col-time">
        <div class="tbl-label"></div>
        <div v-for="time in timeData" class="tbl-cell">
          <span class="tbl-time">{{time.split('-')[0]}}</span>
          <span class="tbl-time" v-if="time==='20:00-22:00'">{{time.split('-')[1]}}</span>
        </div>
      </div>
      <div class="col-day" v-for="(day, key, index) in responseData">
        <div class="tbl-label">{{dayLabel[index]}}</div>
        <div v-for="time in day" :style="getStyle(time)" class="day-cell">
          {{ time===0 ? '': time}}
        </div>
      </div>
    </section>
  </div>
</template>

<script>
  import { Toast } from 'mint-ui'

  export default {
    data () {
      return {
        groupId: '',
//        timeData: ['6:00-8:00', '8:00-10:00', '10:00-12:00', '12:00-14:00', '14:00-16:00', '16:00-18:00', '18:00-20:00', '20:00-22:00'],
//        dayLabel: ['2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
        responseData: {
          'first_day': {
            '6:00-8:00': 0,
            '8:00-10:00': 0,
            '16:00-18:00': 2,
            '10:00-12:00': 4,
            '12:00-14:00': 0,
            '14:00-16:00': 5,
            '18:00-20:00': 0,
            '20:00-22:00': 0
          },
          'second_day': {
            '6:00-8:00': 0,
            '8:00-10:00': 0,
            '16:00-18:00': 2,
            '10:00-12:00': 4,
            '12:00-14:00': 0,
            '14:00-16:00': 5,
            '18:00-20:00': 0,
            '20:00-22:00': 0
          },
          'third_day': {
            '6:00-8:00': 0,
            '8:00-10:00': 0,
            '16:00-18:00': 2,
            '10:00-12:00': 4,
            '12:00-14:00': 3,
            '14:00-16:00': 5,
            '18:00-20:00': 0,
            '20:00-22:00': 8
          },
          'fourth_day': {
            '6:00-8:00': 0,
            '8:00-10:00': 0,
            '16:00-18:00': 2,
            '10:00-12:00': 4,
            '12:00-14:00': 1,
            '14:00-16:00': 5,
            '18:00-20:00': 0,
            '20:00-22:00': 0
          },
          'fifth_day': {
            '6:00-8:00': 0,
            '8:00-10:00': 0,
            '16:00-18:00': 2,
            '10:00-12:00': 4,
            '12:00-14:00': 0,
            '14:00-16:00': 5,
            '18:00-20:00': 0,
            '20:00-22:00': 0
          },
          'sixth_day': {
            '6:00-8:00': 0,
            '8:00-10:00': 0,
            '16:00-18:00': 2,
            '10:00-12:00': 4,
            '12:00-14:00': 0,
            '14:00-16:00': 5,
            '18:00-20:00': 0,
            '20:00-22:00': 0
          },
          'seventh_day': {
            '6:00-8:00': 0,
            '8:00-10:00': 0,
            '16:00-18:00': 2,
            '10:00-12:00': 4,
            '12:00-14:00': 0,
            '14:00-16:00': 5,
            '18:00-20:00': 0,
            '20:00-22:00': 0
          }
        }           /* Add default responseData data in case get failed */
      }
    },
    computed: {
      timeData: function () {
        let timeData = []
        for (let time in this.responseData.first_day) {
          if (this.responseData.first_day.hasOwnProperty(time)) {
            timeData.push(time)
          }
        }
        return timeData
      },
      dayLabel: function () {
        let now = new Date()
        let count = 0
        let dayLabel = []
        for (let day in this.responseData) {
          if (this.responseData.hasOwnProperty(day)) {
            let day = new Date(now.getTime() + 24 * 60 * 60 * 1000 * count)
            dayLabel.push(day.getMonth() + '-' + day.getDate())
          }
          count++
        }
        return dayLabel
      }
    },
    methods: {
      init () {
        this.groupId = localStorage.group_id
        if (this.groupId) {
          this.$http.get(`group-agenda/${this.groupId}/number`).then(res => {
            delete res.body.name
            this.responseData = res.body
          }, res => {
            Toast({
              message: '获取信息失败',
              position: 'bottom',
              duration: 2000
            })
          })
        } else {
          Toast({
            message: 'Oops! There\'s something wrong',
            position: 'bottom',
            duration: 2000
          })
        }
      },
      getStyle (num) {
        if (num === 0) {
          return {
            background: 'rgb(232, 232, 232)'
          }
        }
        return {
          background: `rgb(${254 - num * 5}, ${185 - num * 18}, ${185 - num * 18})`
        }
      }
    },
    mounted () {
      this.init()
    }
  }

</script>

<style scoped>
  .app-wrapper {
    display: flex;
    flex-direction: column;
  }
  .header {
    flex: 0 1 40px;
  }
  .main-part {
    display: flex;
    -webkit-flex-wrap: wrap;
    -ms-flex-wrap: wrap;
    flex-wrap: wrap;
    height: 100%;
  }
  .main-part>div {
    flex: 1 1 10%;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
  }
  .main-part .col-time {
    width: 5rem;
    flex: 0 1 auto;
    font-size: 1.2rem;
    color: #afafbf;
  }
  .col-day {
    display: flex;
    flex-direction: column;
  }
  .col-day>div {
    flex: 1 1 8%;
    border-top: 1px solid #a2a2a2;
    box-sizing: border-box;
  }
  .main-part .tbl-label {
    flex: 0 1 3rem;
    border-top: none;
    font-size: 1.2rem;
    color: #afafbf;
    background: #dcdcdc;
  }
  .tbl-cell {
    display: inline-flex;
    flex-direction: column;
    text-align: center;
    justify-content: space-between;
  }
  .col-time .tbl-cell:nth-child(2) {
    border-top: none;
  }
  .day-cell {
    color: #fff;
  }

</style>
