<template>
  <div>
    <mt-header fixed title="创建群组">
      <mt-button @click="$router.go(-1)" slot="left" icon="back"></mt-button>

    </mt-header>
    <section>
      <mt-field label="群名称"  v-model="groupName" class="group-name"></mt-field>
    </section>
    <section>
      <mt-button type="primary" @click.native="create" class="btn-large">创建</mt-button>
    </section>

  </div>
</template>

<script>
  export default {
    data () {
      return {
        groupName: ''
      }
    },
    methods: {
      create () {
        console.log(this.groupName)
        this.$http.post('groupagenda/group/create/', {'group name': this.groupName}).then(res => {
          if (res.name) {
            this.Toast('你已经创建群组' + res.name)
          }
        })
      }
    }
  }
</script>

<style scoped>
  section{

    margin-top:40px;

  }
  .group-name{
    padding-top:40px;
  }
  .btn-large{
    display: block;
    margin: 20px auto 0 auto;
  }
</style>
