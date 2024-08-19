<template>
  <div>
    <h1>Product List</h1>
    <li
     v-for="product in store.products"
     :key="product.id"
     >
      {{ product.id }} - {{ product.title }} - {{ product.content }}
    </li>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useProductStore } from '@/stores/product'

const store = useProductStore()
</script>

<style scoped>

</style>