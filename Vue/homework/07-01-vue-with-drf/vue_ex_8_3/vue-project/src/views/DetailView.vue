<template>
  <div>
    <h1>할 일 상세</h1>
    <p>할 일 번호 : {{ todo.id }}</p>
    <p>할 일 제목 : {{ todo.work }}</p>
    <p>할 일 내용 : {{ todo.content }}</p>
    <p>할 일 상태 : {{ todo.is_completed }}</p>
    <p>할 일 생성일 : {{ todo.created_at }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useTodoStore } from '@/stores/todoStore';
import { useRoute } from 'vue-router'

const store = useTodoStore()
const route = useRoute()
const todo = ref('')

onMounted(() => {
  axios({
    method: 'get',
    url : `${store.BASE_URL}/api/v1/todos/${route.params.id}/`
  })
  .then((res) => {
    todo.value = res.data
    console.log(todo.value)
    // console.log(res)
  })
  .catch((err) => {
    console.log(err)
  })
})
</script>

<style scoped>

</style>