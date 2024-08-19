<template>
  <div>
    <h2>Product List</h2>
    <ul>
      <ProductListItem 
      v-for="product in store.products" 
      :key="product.id"
      :product="product"
      />
    </ul>
  </div>
</template>

<script setup>
import { useProductStore } from '@/stores/product'
import ProductListItem from '@/components/ProductListItem.vue';
const store = useProductStore()
</script>
