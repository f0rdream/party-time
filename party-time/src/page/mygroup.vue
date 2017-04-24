<template>
  <div>
    <mt-header title="我的群组">
      <mt-button @click="$router.go(-1)" slot="left" icon="back"></mt-button>
      <mt-button @click="$router.push('creategroup')" slot="right" icon="back"></mt-button>
    </mt-header>
    <section class="main-part">
      <mt-cell v-for="group in groups" title="{group.name}" @click.native="choose(group.id)" :key="group.id"><router-link class="chooseA" to="sche"></router-link></mt-cell>
    </section>
    <tab-bar select-item="群组" :fixed-props="true"></tab-bar>
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
        groups: []
      }
    },
    methods: {
      choose: function (groupId) {
        setMap('group_id', groupId)
      }
    },
    mounted () {
      this.$http.get('group-agenda/group/').then(res => {
        this.groups = res.body
      })
    }

  }
</script>
<style scoped>
.chooseA{
  display: block;
}
</style>
