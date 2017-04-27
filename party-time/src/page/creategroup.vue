<template>
  <div>
    <mt-header  title="创建群组">
      <mt-button @click="$router.go(-1)" slot="left" icon="back"></mt-button>
    </mt-header >
    <section class="main-part">
    <section>
      <mt-field label="群名称"  v-model="groupName" class="group-name"></mt-field>
      <mt-field label="群简介" type="textarea" v-model="groupDetail" class="group-detail" rows="4"></mt-field>
    </section>
      <section class="add-people-block">
        <div class="add-people" @click="navigator">
          <img src="../img/search.png" class="search"/>
          <span>从搜索中添加</span>
          <img src="../img/right.png" class="right"/>
        </div>
      </section>
    <section class="button-section">
      <mt-button type="primary" @click.native="create" class="btn-large">创建</mt-button>
    </section>
    </section>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        groupName: '',
        groupDetail: '',
        addPerson: []
      }
    },
    methods: {
      create () {
        this.$http.post('groupagenda/group/create/', {'group name': this.groupName, 'description': this.groupDetail}).then(res => {
          if (res.body.name) {
            this.Toast('你已经创建群组' + res.body.name)
          }
        }, res => {
        })
      }
    },
    mounted () {
      this.groupName = localStorage.groupName || ''
      this.groupDetail = localStorage.groupDetail || ''
      this.addPerson = localStorage.addList || []
      localStorage.removeItem('groupName')
      localStorage.removeItem('groupDetail')
      localStorage.removeItem('addList')
    }
  }
</script>

<style scoped>
.add-people-block{
  margin-top:20px;
}
.add-people{
  position:relative;
  display: flex;
  height:4rem;
  line-height:4rem;
  background: #ffffff;
}
.search{
  width:2rem;
  height:2rem;
  margin:1rem;
}
.right{
  position:absolute;
  right:1rem;
  top:1rem;
  height:2rem;
}
.btn-large{
   margin-top:10rem;
  }
</style>
