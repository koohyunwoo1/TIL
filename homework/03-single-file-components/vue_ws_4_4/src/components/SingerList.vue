<template>
  <div class="card">
    <h1 class="h1">가수 목록</h1>
    <SingerDetail />
    <SingerDetail />
  </div>
</template>

<script setup>
import SingerDetail from '@/components/SingerDetail.vue';
</script>

<style scoped>
.card {
  display: inline-block;
  width: 40%;
  margin: 20px;
  text-align: center;
}

/* .container {
  text-align: center;
} */

.h1 {
  color: orangered;
  text-align: center;
}

</style>
