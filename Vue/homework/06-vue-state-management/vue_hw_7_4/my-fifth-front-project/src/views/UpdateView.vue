<template>
  <div>
    <h1>데이터 수정 페이지</h1>
    <p>이름 : {{ Info.name }}</p>
    <p>잔고 : {{ Info.balance }}</p>
    <button @click="store.updateBalance(route.params.name)">+</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useBalanceStore } from '@/stores/balance';
import { useRoute } from 'vue-router';


const store = useBalanceStore()
const route = useRoute()

const Info = store.Info(route.params.name)
</script>

<style scoped>

</style>