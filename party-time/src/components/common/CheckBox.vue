<template>
  <label class="mint-checklist-label">
    <span class="mint-checkbox">
      <input type="checkbox" class="mint-checkbox-input" @change="$emit('change', currentValue)" v-model="currentValue">
      <span class="mint-checkbox-core"></span>
    </span>
    <span class="mint-checkbox-label">{{ label }}</span>
  </label>
</template>

<script>

  export default {
    props: {
      value: Boolean,
      label: {}
    },
    computed: {
      currentValue: {
        get () {
          return this.value
        },
        set (val) {
          this.$emit('input', val)
        }
      }
    }
  }

</script>
<style scoped>
  .mint-checklist-label {
    display: inline-block;
  }
</style>
