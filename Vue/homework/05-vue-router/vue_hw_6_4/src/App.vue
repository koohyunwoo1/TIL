<template>
  <div>

    <MainPage />
    <nav>
      <RouterLink :to="{ name: 'some'}">Some</RouterLink>
      |
      <RouterLink :to="{ name: 'other'}">Other</RouterLink>
      |
      <RouterLink :to="{ name: 'students'}">Students</RouterLink>
    </nav>
    
  </div>
  <RouterView/>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import MainPage from '@/components/MainPage.vue'

</script>


<style scoped>

</style>
