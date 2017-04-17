<template>
  <div>
    <mt-header title="群组信息">
      <mt-button @click="$router.go(-1)" slot="left" icon="back"></mt-button>
    </mt-header>
    <section class="main-part">
      <section class="centerSection">
        <img class="groupImg" :src="picture"/>
      </section>
      <section class="button-sections">
        <mt-cell title="群名称" :value="group"></mt-cell>
        <mt-cell title="群简介" :value="description" class="description"></mt-cell>
      </section>
      <section>
        <mt-button type="default" class="btn-large" @click.native="quitGroup">退出群组</mt-button>
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
        groupId: '',
        picture: '',
        group: '',
        description: ''
      }
    },
    methods: {
      quitGroup: function () {
        this.$http.get('/accounts/' + this.group_id + '/remove-group').then(res => {
          if (res.groups) {
            Toast('你已经成功退出该群')
          }
        })
      }
    },
    mounted () {
      this.groupId = getMap('group_id')
      this.$http.get('/group-agenda/' + this.groupId + '/group-profile/').then(res => {
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
</style>i
