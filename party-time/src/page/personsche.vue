<template>
  <div class="app-wrapper">
    <mt-header title="第4周" class="header">
      <mt-button slot="right" @click="$router.push('addsche')">
        <i class="iconm--plus" slot="icon"></i>
      </mt-button>
      <mt-button slot="right" @click="$router.push('person')">
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
        <div v-for="(eventI, index) in day" :style="getPosition(eventI.start_time, eventI.end_time)" class="day-cell" @click="togglePopup(key, index, $event)">
        </div>
      </div>
    </section>
    <mt-popup v-model="popupVisible" class="modal-pop">
      <h3 class="modal-title">{{popupContent.title}}</h3>
      <p class="modal-detail">{{popupContent.detail}}</p>
      <p class="modal-detail">{{popupContent.start_time}}</p>
      <p class="modal-detail">{{popupContent.end_time}}</p>
      <div class="modal-btn">
        <mt-button @click.native="deleteTask(popupContent.id)" type="danger">删除任务</mt-button>
      </div>
    </mt-popup>
  </div>
</template>

<script>
  import { Toast } from 'mint-ui'

  export default {
    data () {
      return {
        groupId: '',
        popupVisible: false,
        popupContent: {},
        timeData: ['6:00-8:00', '8:00-10:00', '10:00-12:00', '12:00-14:00', '14:00-16:00', '16:00-18:00', '18:00-20:00', '20:00-22:00'],
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
    computed: {
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
        this.$http.get('tasks/week-list/').then(res => {
          // res.body.forEach(day => {
          //   day.forEach(event => {
          //     event.toggle = false
          //   })
          // })
          this.responseData = res.body
          // for (let day in this.responseData) {
          //   if (this.responseData.hasOwnProperty(day)) {
          //     day = this.responseData[day]
          //     for (let index in day) {
          //       // console.log(day[index])
          //       day[index].togglePop = false
          //     }
          //   }
          // }
          // this.responseData.forEach(day => {
          //   day.forEach(event => {
          //     event.toggle = false
          //   })
          // })
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
        const START = 6
        const END = 22
        const totalMin = (END - START) * 60
        let length, startPos, lengthLevel
        function getJSTime (time) {
          let newDate = ''
          time.split(/-|T|Z/).forEach(item => { newDate += `${item} ` })
          return new Date(newDate)
        }
        startTime = getJSTime(startTime)
        endTime = getJSTime(endTime)
        if (startTime.getHours < 6 || endTime.getHours > 22) {
          return {
            display: 'none'
          }
        }
        length = (endTime.getTime() - startTime.getTime()) / 1000 / 60 / totalMin * 100
        startPos = ((startTime.getHours() - START) * 60 + startTime.getMinutes()) / totalMin * 100
        lengthLevel = parseInt(length * 2 / 25)
        if (length > 100) {
          return {
            display: 'none'
          }
        }
        return {
          top: `${startPos}%`,
          height: `${length}%`,
          background: `rgb(${254 - lengthLevel * 5}, ${185 - lengthLevel * 18}, ${185 - lengthLevel * 18})`
        }
      },
      togglePopup (key, index, event) {
        let startArr, endArr
        this.popupContent = Object.assign({}, this.responseData[key][index])
        this.popupVisible = !this.popupVisible
        function getTime (timeString) {
          return timeString.split(/-|Z|T/)
        }
        startArr = getTime(this.popupContent.start_time)
        endArr = getTime(this.popupContent.end_time)
        this.popupContent.start_time = startArr[1] + '月' + startArr[2] + '日' + startArr[3]
        this.popupContent.end_time = endArr[1] + '月' + endArr[2] + '日' + endArr[3]
      },
      deleteTask (id) {
        this.$http.delete(`tasks/${id}/delete`).then(res => {
          this.popupVisible = false
        }, res => { this.popupVisible = false })
        this.init()
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
    background: #e8e8e8;
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

  .col-time .tbl-time {
    display: inline-block;
    margin: 0.5rem 0;
  }
  .main-part .tbl-label {
    flex: 0 1 3rem;
    border-top: none;
    font-size: 1.2rem;
    color: #000;
    background: #dcdcdc;
    height: 3rem;
    text-align: center;
  }
  .col-day .day-cell {
    position: absolute;
    width: 100%;
  }
  .col-day {
    position: relative;
  }

  .col-time .tbl-cell:nth-child(2) {
    border-top: none;
  }
  .col-time .tbl-cell:last-child {
    display: inline-flex;
    flex-direction: column;
    justify-content: space-between;
  }

  .iconm--plus {
    transform: scale(0.8, 0.8);
  }

  .modal-pop {
    padding: 1rem;
  }
  .modal-btn {
    text-align: center;
  }
  .person-icon {
    vertical-align: middle;
    box-sizing: border-box;
    padding: 0.2rem;
  }
</style>
