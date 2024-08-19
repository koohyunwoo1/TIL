<template>
  <div class="h3">
    <h3>메인 페이지</h3>
    <MainPage
    v-for="balance in store.balances"
    :key="balance.id"
    :balance="balance"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import MainPage from '@/components/MainPage.vue';
import { useBalanceStore } from '@/stores/balance';


const store = useBalanceStore()
</script>

<style scoped>
.h3 {
  margin-left: 20px;
  margin-top: 40px;
  
}
</style>