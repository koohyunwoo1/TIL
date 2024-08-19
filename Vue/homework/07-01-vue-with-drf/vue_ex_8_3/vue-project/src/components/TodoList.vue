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
import TodoListItem from '@/components/TodoListItem.vue'
const props = defineProps({
  todos:Object
})
</script>
