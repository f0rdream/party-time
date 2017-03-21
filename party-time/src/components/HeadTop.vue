<template>
  <header id="head_top">
    <section class="head-goback" v-if="goBack" @click="$router.go(-1)">
      <svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg" version="1.1">
        <polyline points="12,18 4,9 12,0" style="fill:none;stroke:rgb(255,255,255);stroke-width:2"/>
      </svg>
    </section>
    <section class="head-title ellipsis" v-if="headTitle">
      <span class="title-text">{{headTitle}}</span>
    </section>
    <slot name="head-right"></slot>
  </header>
</template>

<script>

export default {
  props: {
    goBack: {
      default: true
    },
    headTitle: { }
  }

}

</script>
<style scoped>

</style>
