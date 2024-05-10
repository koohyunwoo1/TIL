<template>
  <div>
    <h1>전체 상품 목록</h1>
    <!-- {{ cartStore.products }} -->
    <div class="product-list">
      <div v-for="product in cartStore.products" class="product-card">
        <img :src="product.image" alt="" class="product-image">
        <b>상품명 : {{ product.title }}</b>
        <p>가격 : ${{ product.price }}</p>
        <button @click="goDetailPage(product.id)">상세페이지로 이동</button>
      </div>
    </div>
  </div>
</template>


<script setup>
import { routerKey, useRoute, useRouter } from 'vue-router';
import { useCartStore } from '@/stores/counter';
import { onMounted } from 'vue';
const cartStore = useCartStore()

// onMounted: 비동기 API 호촐 코드를 많이 활용한다.
onMounted(() => {
  cartStore.getProducts()
})

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