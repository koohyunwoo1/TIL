<template>
  <div>
    <li>
      {{ product.id }} - {{ product.title }} - {{ product.body }}
      <button @click="store.deleteProduct(product.id)">Delete</button>
    </li>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useProductStore } from '@/stores/product';

const store = useProductStore()

defineProps({
  product: Object
})

</script>

<style scoped>

</style>