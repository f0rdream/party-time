<template>
  <div>
    <mt-header title="我的群组">
      <mt-button @click="$router.go(-1)" slot="left" icon="back"></mt-button>
    </mt-header>
    <section class="main-part">
      <mt-cell v-for="group in groups" title="{group.name}" @click.native="choose(group.id)" :key="group.id"><a class="chooseA" href="/schedetail"></a></mt-cell>
    </section>
  </div>
</template>

<script>
  import { setMap } from '../config/store'

  export default {
    data () {
      return {
        groups: []
      }
    },
    methods: {
      choose: function (groupId) {
        setMap('group_id', groupId)
      }
    },
    mounted () {
      this.$http.get('/group-agenda/group/').then(res => {
        this.groups = res
      })
    }

  }
</script>
<style scoped>
.chooseA{
  display: block;
}
</style>
