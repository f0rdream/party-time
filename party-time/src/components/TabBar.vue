<template>
  <div class="tabbar-outer">
    <mt-tabbar v-model="selected">
      <mt-tab-item id="日期">
        <img slot="icon" src="../assets/logo.png">
        日期
      </mt-tab-item>
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
    components: {
      Tabbar, TabItem
    },
    data () {
      return {
      }
    }
  }
</script>

<style scoped>

</style>
