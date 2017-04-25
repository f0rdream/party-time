<template>
  <div>
  <mt-header  title="邀请好友">
    <mt-button @click="$router.go(-1)" slot="left" icon="back"></mt-button>
  </mt-header >
  <section class="main-part">
    <section class="search-box">
      <img src="../img/search.png" class="search"/>
      <input type="text" placeholder="你可以输入用户名，真实名称，电话号码" @submit="search"/>
    </section>
  </section>
  </div>
</template>
<script>
</script>
<style>
.search-box{
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
</style>
