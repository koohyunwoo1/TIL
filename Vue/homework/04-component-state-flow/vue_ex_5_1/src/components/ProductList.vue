<template>
  <div>
    <li>
      {{ myProduct.name }} - {{ myProduct.price }}원
    </li>
  </div>
</template>

<script setup>
import { ref } from 'vue'

defineProps({
  myProduct: Object
})
</script>

<style scoped>

</style>