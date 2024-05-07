<template>
  <div>
    <h3>또 다른 자식 페이지</h3>
    <p>{{ obj.name }}</p>
  </div>
</template>

<script setup>
  defineProps({
    obj: Object
  })
  import { ref } from 'vue'
 
</script>

<style scoped>

</style>