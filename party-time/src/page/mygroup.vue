<template>
  <div>
    <mt-header title="我的群组">
      <mt-button @click="$router.go(-1)" slot="left" icon="back"></mt-button>
      <mt-button @click="$router.push('creategroup')" slot="right" icon="back"></mt-button>
    </mt-header>
    <section class="main-part">
      <div class="group" v-for="group in groups" @click.native="choose(group.id)">
        <img :src="group.picture" class="group-left"/>
        <div class="group-right">
          <p>{{group.name}}</p>
          <p>{{group.description}}</p>
        </div>
      </div>
    </section>
    <img src="../img/add.png" class="add" @click="creategroup"/>
    <tab-bar select-item="群组" fixed-props="true"></tab-bar>
  </div>
</template>

<script>
  import { setMap } from '../config/store'
  import TabBar from '../components/TabBar'
  export default {
    components: {
      TabBar
    },
    data () {
      return {
        groupId: [],
        groups: [{id: '001', picture: 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1493043744598&di=830b5dfaa6b0d3106c8d6064587c0a76&imgtype=0&src=http%3A%2F%2Fimg.zcool.cn%2Fcommunity%2F010af65688bc4532f8759f04ff06e8.jpg', name: 'lala', description: 'this is lala'}]
      }
    },
    methods: {
      creategroup: function () {
        console.log('click')
        window.location.href = '../creategroup'
      },
      choose: function (groupId) {
        setMap('group_id', groupId)
      }
    },
    mounted () {
      this.$http.get('group-agenda/group/').then(res => {
        res.body.forEach(function (val, index) {
          this.groupId.push(val.id)
        })
      })
      for (let groupId in groupId) {
        this.$http.get('/group-agenda/' + groupId + '/group-profile/').then(res => {
          let group
          group.id = groupId
          group.name = res.body.group
          group.descirption = res.body.description.substring(0, 18)
          group.picture = res.body.picture
          this.groups.push(group)
        })
      }
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
  font-size:20px;
}
.group p:nth-child(2){
  font-size:15px;
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
