<template>
  <div class="app-wrapper">
    <mt-header title="第4周" class="header">
      <mt-button @click="$router.push('mygroup')" slot="left" icon="back">群组</mt-button>
      <mt-button icon="more" slot="right" @click="$router.push('groupmessage')"></mt-button>
    </mt-header>
    <section class="main-part">
      <div class="col-day col-time">
        <div class="tbl-label"></div>
        <div v-for="time in timeData" class="tbl-cell">
          <span class="tbl-time">{{time.split('-')[0]}}</span>

        </div>
      </div>
      <div class="col-day" v-for="(day, key, index) in responseData">
        <div class="tbl-label">{{dayLabel[index]}}</div>
        <div v-for="time in day" :style="getStyle(time)" class="day-cell">
          {{time}}
        </div>
      </div>
    </section>
  </div>
</template>

<script>
  import { getMap } from '../config/store'
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
    mounted () {
      this.init()
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
        let nowYear = now.getFullYear()
        let nowMonth = now.getMonth()
        let nowDate = now.getDate()
        let count = 0
        let dayLabel = []
        for (let day in this.responseData) {
          if (this.responseData.hasOwnProperty(day)) {
            let day = new Date(`${nowYear}-${nowMonth}-${nowDate + count}`)
            dayLabel.push(day.getMonth() + '-' + day.getDate())
          }
          count++
        }
        return dayLabel
      }
    },
    methods: {
      init () {
        this.$http.get('tasks/').then(res => {
          this.responseData = res.body
        }, res => {
          Toast({
            message: '获取信息失败',
            position: 'bottom',
            duration: 2000
          })
        })
      },
      getStyle (num) {
        let style = {}
        switch (num) {
          case 0:
            style.borderTop = '1px solid #000'
            break
          default:
            style.background = `hsl(${num * 36}, 100%, 50%)`
            style.borderTop = 'none'
        }
        return style
      },
      getPosition () {
        let endHour = 22
        let startHour = 6
        let total = (endHour - startHour) * 60

      }
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
    border-top: 1px solid #494351;
    box-sizing: border-box;
  }
  .main-part .tbl-label {
    flex: 0 1 3rem;
    border-top: none;
    font-size: 1.2rem;
    color: #afafbf;
  }
  .tbl-cell {
    display: inline-flex;
    flex-direction: column;
    text-align: center;
    justify-content: space-between;
  }

</style>
