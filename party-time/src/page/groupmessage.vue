<template>
  <div>
    <mt-header title="群组信息">
      <mt-button @click="$router.go(-1)" slot="left" icon="back"></mt-button>
      <mt-button slot="right" @click="$router.push('creategroupsche')">
        <i class="iconm--plus" slot="icon" height="30" width="30"></i>
      </mt-button>
    </mt-header>
    <section class="main-part">
      <section class="centerSection">
        <img class="groupImg" :src="picture"/>
      </section>
      <section class="button-sections">
        <mt-cell title="群名称" :value="group"></mt-cell>
        <mt-cell title="群简介" :value="description" class="description"></mt-cell>
      </section>
      <section class="person-block">
        <p>群成员</p>
        <div class="person-list">
          <img :src="img" v-for="img in imgList"/>
          <img src="../img/add.png" class="add" @click="navigator"/>
        </div>
      </section>
      <section>
        <mt-button type="default" class="btn-large" @click.native="quitGroup">退出群组</mt-button>
      </section>
    </section>
  </div>
</template>

<script>
  import { Toast } from 'mint-ui'
  export default {
    data () {
      return {
        groupId: '',
        picture: '',
        group: '',
        description: '',
        imgList: []
      }
    },
    methods: {
      quitGroup: function () {
        this.$http.get('accounts/' + this.group_id + '/remove-group').then(res => {
          if (res.body.groups) {
            Toast('你已经成功退出该群')
          }
        })
      },
      navigator () {
        localStorage.groupName = this.groupName
        localStorage.groupDetail = this.groupDetail
        window.location.href = '../addperson'
      }
    },
    mounted () {
      this.groupId = localStorage.groupId
      this.$http.get('group-agenda/' + this.groupId + '/group-profile/').then(res => {
        this.picture = res.picture
        this.group = res.group
      })
    }

  }
</script>
<style scoped>
  .centerSection{
    display: flex;
    align-items:center;
    justify-content:center;
    padding-bottom: 2rem;
  }
  .groupImg{
    width:10rem;
    height:10rem;
    background: #cccccc;
  }
  .description{
    height:10rem;
    margin-top:2rem;
  }
  .btn-large{
    display: block;
    margin: 20px auto 0 auto;
  }
  .person-block{
    background:white
  }
  .person-block p{
    margin-left:1rem;
    font-size:2rem;
  }
  .person-list{
    display:  flex;

  }
  .person-list img,.add{
    width: 50px;
    height: 50px;
    border-radius:25px;
    margin:2rem 1rem;
  }

  .iconm--plus {
    transform: scale(0.8, 0.8);
  }
</style>i
