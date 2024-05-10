<template>
  <div>
    <h1>장바구니</h1>
    <div class="product-list">
      <div v-for="product in cartStore.carts" class="product-card">
        <img :src="product.image" alt="" class="product-image">
        <b>상품명 : {{ product.title }}</b>
        <p>가격 : ${{ product.price }}</p>
        <button @click="goDetailPage(product.id)">상세페이지로 이동</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCartStore } from '@/stores/counter';
import { useRouter } from 'vue-router';

const cartStore = useCartStore()

const router = useRouter()
const goDetailPage = function(productId) {
  router.push(`/${productId}`)
}
</script>

<style scoped>
.product-card {
  width: 200px;
  border: 1px solid #ccc;
  padding: 10px;
}

.product-image {
  width: 100%;

}

.product-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

</style>