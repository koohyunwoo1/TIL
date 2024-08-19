<!-- ProductList.vue -->
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
import ProductListItem from '@/components/ProductListItem.vue'
import { useProductStore } from '@/stores/product'
import { onMounted } from 'vue';


const store = useProductStore()

onMounted(() => {
  store.goAxios()
})

</script>
