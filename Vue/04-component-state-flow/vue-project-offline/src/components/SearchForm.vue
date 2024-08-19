<template>
  <form 
  @submit.prevent="$emit('changeWord', ownText)">
    <input 
      type="text" 
      :placeholder="onlyMyText"
      v-model="ownText"
    >
    <input type="submit" value="search">
  </form>
</template>

<script setup>
  import { ref } from 'vue'
  defineProps({
    onlyMyText: String
  })
  const ownText = ref('')
</script>

<style scoped>

</style>