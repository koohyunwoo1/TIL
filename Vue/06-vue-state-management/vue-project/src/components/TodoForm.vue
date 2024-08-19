<template>
  <div>
    <form @submit.prevent="createTodo(todoText)" ref="formElem">
      <input type="text" v-model="todoText">
      <input type="submit" value="작성">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()
const todoText = ref('')
const formElem = ref(null)

const createTodo = function(todoText) {
  store.addTodo(todoText)
  formElem.value.reset()
  // form에 있는 모든 값 초기화
}

</script>

<style scoped>

</style>