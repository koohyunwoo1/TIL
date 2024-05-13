<template>
  <header>
    <nav>
    </nav>
  </header>
  <RouterLink :to="{name : 'TodoView'}">할 일 목록</RouterLink>
  <RouterView />
</template>

<script setup>
import { RouterView } from 'vue-router'
</script>

<style scoped>
</style>
