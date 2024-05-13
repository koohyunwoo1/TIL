<template>
<main>
  <h1>할 일 목록</h1>
  <TodoList :todos="store.todos" />
</main>
</template>

<script setup>
import TodoList from '@/components/TodoList.vue'
import { onMounted } from 'vue'
import {useTodoStore} from "@/stores/todoStore.js";
const store = useTodoStore()
onMounted(() => {
  store.getTodos()
})

</script>

<style>

</style>
