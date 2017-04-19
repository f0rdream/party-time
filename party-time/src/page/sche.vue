<template>
  <div class="app-wrapper">
    <mt-header title="第4周" class="header">
      <mt-button @click="$router.push('person')" slot="left" icon="back"></mt-button>
      <mt-button icon="more" slot="right"></mt-button>
    </mt-header>
    <section class="main-part">
      <div class="col-day col-time">
        <div class="tbl-label"></div>
        <div v-for="(value , time) in response.first_day" class="tbl-cell">
          <span class="tbl-time">{{time.split('-')[0]}}</span>
          <span class="tbl-time" v-if="time==='20:00-22:00'">{{time.split('-')[1]}}</span>
        </div>
      </div>
      <div class="col-day" v-for="(day, key, index) in response">
        <div class="tbl-label">{{dayLabel[index]}}</div>
        <div v-for="time in day" :style="getStyle(time)" class="day-cell">
          {{time}}
        </div>
      </div>
    </section>
    <tab-bar></tab-bar>
  </div>
</template>

<script>
  import { getMap } from '../config/store'
  import { Toast } from 'mint-ui'
  import TabBar from '@/components/TabBar'

  export default {
    components: {
      TabBar
    },
    data () {
      return {
        groupId: '',
        timeData: ['6:00-8:00', '8:00-10:00', '10:00-12:00', '12:00-14:00', '14:00-16:00', '16:00-18:00', '18:00-20:00', '20:00-22:00'],
        dayLabel: ['2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
        response: {
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
        }
      }
    },
    methods: {
      init () {
        let now = new Date()
        let nowYear = now.getFullYear()
        let nowMonth = now.getMonth()
        let nowDate = now.getDate()
        this.groupId = getMap('groupId')
        this.$http.get(`group-agenda/${this.groupId}/number/`).then(res => {
          delete res.body.name
          this.response = res.body
          let count = 0
          for (let day in res.body) {
            this.dayLabel.push(new Date(`${nowYear}-${nowMonth}-${nowDate + count}`))
            for (let time in day) {
              this.timeData.push(time)
            }
          }
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
  }
  .tbl-cell {
    display: inline-flex;
    flex-direction: column;
    text-align: center;
    justify-content: space-between;
  }
</style>
