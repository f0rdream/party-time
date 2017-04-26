<template>
  <div>
  <mt-header  title="邀请好友">
    <mt-button @click="$router.go(-1)" slot="left" icon="back"></mt-button>
    <mt-button @click="ready" slot="right">确认</mt-button>
  </mt-header >
  <section class="main-part">
    <section class="search-box">
      <img src="../img/search.png" class="search"/>
      <form action="#" @submit="search">
      <input type="text" placeholder="你可以输入用户名，真实名称，电话号码"  v-model="searchValue"/>
      </form>
    </section>
    <section class="person-item" v-for="user in userList">
      <img :src="user.picture" class="avator"/>
      <span>{{user.name}}</span>
      <img  v-if="user.isChecked" src="../img/added_people.png" class="added_people" @click ="notChecked(user)"/>
      <img  v-else="user.isChecked" src="../img/add_people.png" class="add_people" @click ="checked(user)"/>
    </section>
  </section>
  </div>
</template>
<script>
  import { Toast } from 'mint-ui'
  export default {
    data () {
      return {
        searchValue: '',
        userList: [{picture: 'http://img0.imgtn.bdimg.com/it/u=998639688,3452677906&fm=23&gp=0.jpg', name: '康娜', isChecked: false, id: '001'}],
        addList: []
      }
    },
    methods: {
      search: function () {
        console.log(this.searchValue)
        this.$http.get('/accounts/list/?search=' + this.searchValue).then(res => {
          if (res.body) {
            res.body.forEach(function (val, index) {
              val.isChecked = false
            })
            this.userList = res.body
          } else {
            Toast({
              message: '没有找到结果',
              position: 'bottom',
              duration: 2000
            })
          }
        }, res => {

        })
      },
      notChecked: function (user) {
        user.isChecked = false
        this.addList.splice(this.addList.indexOf(user.username), 1)
        console.log(this.addList)
      },
      checked: function (user) {
        user.isChecked = true
        this.addList.push(user.username)
        console.log(this.addList)
      },
      ready: function () {
        groupId = localStorage.group_id
        this.$http.get('http://127.0.0.1:8000/accounts/add-group/' + this.addList[0] + '/' + groupId + '/').then(res =>{
          Toast({
            message: '成功添加',
            position: 'bottom',
            duration: 2000
          })
        })
      }
    },
    mounted () {
    }

  }
</script>
<style>
.search-box{
  display: flex;
  height:4rem;
  line-height:4rem;
  margin-bottom:20px;
  background: #ffffff;
}
.search-box input{
  border: 0px transparent;
  width:20rem;
  height:3rem;
  margin-top:5px;
}
.search-box input:focus{
  outline:none;
}
.search{
  width:2rem;
  height:2rem;
  margin:1rem;
}
.person-item{
  display: flex;
  position:relative;
  background:#ffffff;
  height:5rem;
  line-height: 5rem;
  border-bottom:1px solid #cccccc;
}
.avator{
  width: 50px;
  height:50px;
  border-radius:25px;
  margin-left:20px;
  margin-top:5px;
  background: #cccccc;
}
.person-item span{
  margin-left: 1rem;
}
.add_people{
  position:absolute;
  right:16px;
  top:16px;
  width: 20px;
}
.added_people{
    position:absolute;
    right:9px;
    top:9px;
    width: 30px;
}
</style>
