<template>
  <div>
    <mt-header title="我的群组">
      <mt-button @click="$router.go(-1)" slot="left" icon="back"></mt-button>
    </mt-header>
    <section class="main-part">
      <div class="group" v-for="group in groups" @click="choose(group.id)">
        <img :src="group.picture" class="group-left"/>
        <div class="group-right">
          <p>{{group.name}}</p>
          <p>{{group.description}}</p>
        </div>
      </div>
    </section>
    <div>
      <img src="../img/add.png" class="add" @click="creategroup"/>
    </div>
    <tab-bar select-item="群组" :fixed-props="true"></tab-bar>
  </div>
</template>

<script>
  import TabBar from '../components/TabBar'
  export default {
    components: {
      TabBar
    },
    data () {
      return {
        groups: [{id: '001', picture: 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1493043744598&di=830b5dfaa6b0d3106c8d6064587c0a76&imgtype=0&src=http%3A%2F%2Fimg.zcool.cn%2Fcommunity%.jpg', name: 'lala', description: 'this is lala'}]
      }
    },
    methods: {
      creategroup: function () {
        console.log('click')
        this.$router.push('creategroup')
      },
      choose: function (groupId) {
        console.log(groupId)
        localStorage.group_id = groupId
        this.$router.push('sche')
      }
    },
    mounted () {
      var that = this
      this.$http.get('/group-agenda/group/').then(res => {
        console.log(res.body)
        res.body.forEach(function (val, index) {
          that.$http.get('/group-agenda/' + val.id + '/group-profile/').then(res => {
            var group = {}
            var id = val.id
            group.id = id
            group.name = res.body.group
            group.description = res.body.description.substring(0, 18)
            group.picture = res.body.picture
            console.log(group)
            that.groups.push(group)
          })
        })
      })
    }
  }
</script>
<style scoped>
.group{
  display: flex;
  background:#ffffff;
  padding-top:10px;
  padding:10px;
}
.group-left{
  width: 50px;
  height: 50px;
  border-radius: 25px;
}
.group-right{
  margin:0px;
  padding:0px;
  padding-left: 20px;
  line-height: 2rem;
}
.group-right p {
  padding:0px;
  margin:0px;
}
.group p:first-child{
  font-size:2rem;
}
.group p:nth-child(2){
  font-size:1.5rem;
}
.add{
  width:70px;
  height:70px;
  position: fixed;
  bottom:100px;
  margin-left: 50%;
  transform: translateX(-50%);
}

</style>
