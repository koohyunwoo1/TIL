<template>
  <div>
    <TodoListItem 
    v-for="todo in todos"
    :key="todo.id"
    :todo="todo"
    
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import TodoListItem from '@/components/TodoListItem.vue';
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const todos = store.todos


</script>

<style scoped>

</style>