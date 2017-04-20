<template>
  <div class="tabbar-outer">
    <mt-tabbar v-model="selected">
      <mt-tab-item id="群组">
        <img slot="icon" src="../assets/logo.png">
        群组
      </mt-tab-item>
      <mt-tab-item id="个人">
        <img slot="icon" src="../assets/logo.png">
        个人
      </mt-tab-item>
    </mt-tabbar>
  </div>
</template>

<script>
  import { Tabbar, TabItem } from 'mint-ui'

  export default {
    name: 'TabBar',
    props: ['selectItem'],
    components: {
      Tabbar, TabItem
    },
    data () {
      return {
        selected: this.selectItem
      }
    }
  }
</script>

<style scoped>
  .mint-tabbar {
    position: relative;
  }
</style>
