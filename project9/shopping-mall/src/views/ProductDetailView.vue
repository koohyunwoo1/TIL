<template>
  <div v-if="product.id">
    <h1>
      상품명 : {{ product.title }}
    </h1>
    <img :src="product.image" alt="" width="200">
    <p>
      가격 : {{ product.price }}
    </p>
    <p>
      카테고리 : {{ product.category }}
    </p>
    <button @click="cartStore.addCart(product)">장바구니에 추가</button>
  </div>
  <p v-else>Loading 중...</p>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router';
import axios from 'axios';
import { useCartStore } from '@/stores/counter'

// 1. product Id를 URL, params 로 부터 가져온다.
const route = useRoute()
const productId = route.params.product_id
const cartStore = useCartStore()
// 2. product Id 를 이용해서 데이터를 가져온다.
// 2.1 store에서 데이터를 가져오는 경우

// 2.2 axios로 상세 페이지를 호출하기
// 상품 디테일 페이지부터 접근하면 사용자가 데이터를 가져올 수 없다.

const product = ref([])
const carts = ref([])


axios({
  method: 'get',
  url: `https://fakestoreapi.com/products/${productId}`
}) .then((response) => {
  product.value = response.data
}) .catch((error) => {
  console.log(error)
})

// 3. 화면에 그려준다.

</script>

<style scoped>

</style>