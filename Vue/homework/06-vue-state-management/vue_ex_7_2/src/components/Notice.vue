<template>
  <div>
      <p>남은 제품 개수 : {{ store.productCount }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

import { useProductStore } from '@/stores/product';

const store = useProductStore()
</script>

<style scoped>

</style>