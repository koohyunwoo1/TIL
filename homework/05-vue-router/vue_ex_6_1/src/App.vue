<template>
  <header>
    <nav>
      <RouterLink :to="{ name: 'home'}">Home</RouterLink>
      |
      <RouterLink :to="{ name: 'about'}">About</RouterLink>
    </nav>
  </header>

  <RouterView/>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
</style>
