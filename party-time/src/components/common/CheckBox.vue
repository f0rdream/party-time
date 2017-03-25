<template>
  <label class="mint-checklist-label">
    <span class="mint-checkbox">
      <input type="checkbox" class="mint-checkbox-input" :value=checkValue>
      <span class="mint-checkbox-core"></span>
    </span>
    <span class="mint-checkbox-label">{{ label }}</span>
  </label>
</template>

<script>

export default {
  props: {
    checkValue: {
      required: true
    },
    label: {
    }
  }

}

</script>
<style scoped>
.mint-checklist-label {
  display: inline-block;
}
</style>
