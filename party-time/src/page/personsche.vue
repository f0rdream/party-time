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
        <div v-for="event in day" :style="getPosition(event.start_time, event.end_time)" class="day-cell">

        </div>
      </div>
    </section>
  </div>
</template>

<script>
  // import { getMap } from '../config/store'
  import { Toast } from 'mint-ui'

  export default {
    data () {
      return {
        groupId: '',
        timeData: ['6:00-8:00', '8:00-10:00', '10:00-12:00', '12:00-14:00', '14:00-16:00', '16:00-18:00', '18:00-20:00', '20:00-22:00'],
//        dayLabel: ['2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
        responseData: {
          'second_day': [
            {
              'url': 'http://127.0.0.1:8000/tasks/15/',
              'delete_url': 'http://127.0.0.1:8000/tasks/15/delete',
              'id': 15,
              'user': 'djangotest',
              'title': 'abcabcabc',
              'start_time': '2017-04-25T08:02:00Z',
              'end_time': '2017-04-25T12:59:00Z',
              'is_past': false
            },
            {
              'url': 'http://127.0.0.1:8000/tasks/16/',
              'delete_url': 'http://127.0.0.1:8000/tasks/16/delete',
              'id': 16,
              'user': 'djangotest',
              'title': 'gdsfgdsgdf',
              'start_time': '2017-04-25T08:02:00Z',
              'end_time': '2017-04-25T12:59:00Z',
              'is_past': false
            }
          ],
          'seventh_day': [
            {
              'url': 'http://127.0.0.1:8000/tasks/15/',
              'delete_url': 'http://127.0.0.1:8000/tasks/15/delete',
              'id': 15,
              'user': 'djangotest',
              'title': 'abcabcabc',
              'start_time': '2017-04-25T08:02:00Z',
              'end_time': '2017-04-25T12:59:00Z',
              'is_past': false
            },
            {
              'url': 'http://127.0.0.1:8000/tasks/16/',
              'delete_url': 'http://127.0.0.1:8000/tasks/16/delete',
              'id': 16,
              'user': 'djangotest',
              'title': 'gdsfgdsgdf',
              'start_time': '2017-04-25T08:02:00Z',
              'end_time': '2017-04-25T12:59:00Z',
              'is_past': false
            }
          ],
          'third_day': [
            {
              'url': 'http://127.0.0.1:8000/tasks/15/',
              'delete_url': 'http://127.0.0.1:8000/tasks/15/delete',
              'id': 15,
              'user': 'djangotest',
              'title': 'abcabcabc',
              'start_time': '2017-04-25T08:02:00Z',
              'end_time': '2017-04-25T12:59:00Z',
              'is_past': false
            },
            {
              'url': 'http://127.0.0.1:8000/tasks/16/',
              'delete_url': 'http://127.0.0.1:8000/tasks/16/delete',
              'id': 16,
              'user': 'djangotest',
              'title': 'gdsfgdsgdf',
              'start_time': '2017-04-25T08:02:00Z',
              'end_time': '2017-04-25T12:59:00Z',
              'is_past': false
            }
          ],
          'sixth_day': [
            {
              'url': 'http://127.0.0.1:8000/tasks/15/',
              'delete_url': 'http://127.0.0.1:8000/tasks/15/delete',
              'id': 15,
              'user': 'djangotest',
              'title': 'abcabcabc',
              'start_time': '2017-04-25T08:02:00Z',
              'end_time': '2017-04-25T12:59:00Z',
              'is_past': false
            },
            {
              'url': 'http://127.0.0.1:8000/tasks/16/',
              'delete_url': 'http://127.0.0.1:8000/tasks/16/delete',
              'id': 16,
              'user': 'djangotest',
              'title': 'gdsfgdsgdf',
              'start_time': '2017-04-25T08:02:00Z',
              'end_time': '2017-04-25T12:59:00Z',
              'is_past': false
            }
          ],
          'fifth_day': [
            {
              'url': 'http://127.0.0.1:8000/tasks/15/',
              'delete_url': 'http://127.0.0.1:8000/tasks/15/delete',
              'id': 15,
              'user': 'djangotest',
              'title': 'abcabcabc',
              'start_time': '2017-04-25T08:02:00Z',
              'end_time': '2017-04-25T12:59:00Z',
              'is_past': false
            },
            {
              'url': 'http://127.0.0.1:8000/tasks/16/',
              'delete_url': 'http://127.0.0.1:8000/tasks/16/delete',
              'id': 16,
              'user': 'djangotest',
              'title': 'gdsfgdsgdf',
              'start_time': '2017-04-25T08:02:00Z',
              'end_time': '2017-04-25T12:59:00Z',
              'is_past': false
            }
          ],
          'first_day': [
            {
              'url': 'http://127.0.0.1:8000/tasks/15/',
              'delete_url': 'http://127.0.0.1:8000/tasks/15/delete',
              'id': 15,
              'user': 'djangotest',
              'title': 'abcabcabc',
              'start_time': '2017-04-25T08:02:00Z',
              'end_time': '2017-04-25T12:59:00Z',
              'is_past': false
            },
            {
              'url': 'http://127.0.0.1:8000/tasks/16/',
              'delete_url': 'http://127.0.0.1:8000/tasks/16/delete',
              'id': 16,
              'user': 'djangotest',
              'title': 'gdsfgdsgdf',
              'start_time': '2017-04-25T08:02:00Z',
              'end_time': '2017-04-25T12:59:00Z',
              'is_past': false
            }
          ],
          'fourth_day': [
            {
              'url': 'http://127.0.0.1:8000/tasks/15/',
              'delete_url': 'http://127.0.0.1:8000/tasks/15/delete',
              'id': 15,
              'user': 'djangotest',
              'title': 'abcabcabc',
              'start_time': '2017-04-25T08:02:00Z',
              'end_time': '2017-04-25T12:59:00Z',
              'is_past': false
            },
            {
              'url': 'http://127.0.0.1:8000/tasks/16/',
              'delete_url': 'http://127.0.0.1:8000/tasks/16/delete',
              'id': 16,
              'user': 'djangotest',
              'title': 'gdsfgdsgdf',
              'start_time': '2017-04-25T08:02:00Z',
              'end_time': '2017-04-25T12:59:00Z',
              'is_past': false
            }
          ]
        }
      }
    },
    mounted () {
      this.init()
    },
    computed: {
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
        this.$http.get('tasks/week-list/').then(res => {
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
      getPosition (startTime, endTime) {
        // let style = {}
        const START = 6
        const END = 22
        const totalMin = (END - START) * 60
        function getJSTime (time) {
          let newDate = ''
          time.split(/-|T|Z/).forEach(item => { newDate += `${item} ` })
          return new Date(newDate)
        }
        startTime = getJSTime(startTime)
        endTime = getJSTime(endTime)
        // if (startTime.getHours < 6 || endTime.getHours > 22) {
        //   return {
        //     display: 'none'
        //   }
        // }
        let length = (endTime.getTime() - startTime.getTime()) / 1000 / 60 / totalMin * 100
        let startPos = ((startTime.getHours() - START) * 60 + startTime.getMinutes()) / totalMin * 100
        console.log(length)
        console.log(startPos)
        // style.length = `${length}%`
        // style.top =
        return {
          top: `${startPos}%`,
          height: `${length}%`
        }
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
    flex-direction: column;
    text-align: center;
    display: flex;
  }
  .col-time .tbl-cell {
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
</style>
