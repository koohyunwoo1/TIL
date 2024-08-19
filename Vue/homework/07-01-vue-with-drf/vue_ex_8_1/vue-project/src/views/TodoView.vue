<template>
<main>
  <h1>할 일 목록</h1>
  {{ store }}
</main>
</template>

<script setup>
import { useTodoStore } from '@/stores/todoStore';
import { onMounted } from 'vue';

const store = useTodoStore()

onMounted(() => {
  store.getTodos()
})

</script>

<style>

</style>
