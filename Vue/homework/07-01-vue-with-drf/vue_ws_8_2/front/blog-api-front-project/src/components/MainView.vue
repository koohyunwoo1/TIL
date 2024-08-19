<template>
  <div>
<nav>
  Home
</nav>
  </div>
<div class="name">
  <h2>
    OO이의 블로그
  </h2>
  <p>
    Welcome to my personal blog!
  </p>
</div>
</template>

<script setup>
import { ref } from 'vue'


</script>

<style scoped>
nav {
  background-color: #333333;
  padding : 1rem;
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
  font-weight: bold;
  color: white;
  }

.name {
  text-align: center;
  margin-top: 300px;
}
</style>