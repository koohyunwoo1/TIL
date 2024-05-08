<template>
  <div>
    <h1>User Profile</h1>
    <h3>username: {{ username }}</h3>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const username = ref(route.params.username)
</script>

<style scoped>

</style>