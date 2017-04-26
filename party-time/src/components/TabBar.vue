<template>
  <div class="tabbar-outer">
    <mt-tabbar v-model="selected" :fixed="fixed">
      <mt-tab-item id="个人" @click.native="$router.push('personsche')">
        <img slot="icon" src="../assets/logo.png">
        个人
      </mt-tab-item>
      <mt-tab-item id="群组" @click.native="$router.push('mygroup')">
        <img slot="icon" src="../assets/logo.png">
        群组
      </mt-tab-item>
    </mt-tabbar>
  </div>
</template>

<script>
  import { Tabbar, TabItem } from 'mint-ui'

  export default {
    name: 'TabBar',
    props: ['selectItem', 'fixedProps'],
    components: {
      Tabbar, TabItem
    },
    data () {
      return {
        selected: this.selectItem,
        fixed: this.fixedProps
      }
    }
  }
</script>

<style scoped>
  .mint-tabbar {
    position: relative;
  }
</style>
