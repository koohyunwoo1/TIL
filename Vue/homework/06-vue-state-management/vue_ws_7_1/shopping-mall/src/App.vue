<template>
  <div>
    <nav class="nav">

      <RouterLink to="/" class="nav-text">Home</RouterLink>
      <RouterLink to="/products" class="nav-text">Products</RouterLink>
      <RouterLink to="/favorite" class="nav-text">Favorite</RouterLink>

    </nav>
    <RouterView/>
  </div>
</template>


<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>


<style scoped>
.nav {
  background-color: #333333;
  display: flex;
  justify-content: center;
}

.nav-text { 
  color: white;
  margin: 15px;
}
</style>
