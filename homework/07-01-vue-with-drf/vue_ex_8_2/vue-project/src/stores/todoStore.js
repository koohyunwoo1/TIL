import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from "axios";

export const useTodoStore = defineStore('todo', () => {
  const todos = ref([])
  const BASE_URL = 'http://localhost:8000'
  const getTodos = () => {
    axios({
        method: 'get',
        url: `${BASE_URL}/api/v1/todos/`,
    }).then((response) => {
        todos.value = response.data
    }).catch((error) => {
        console.log(error)
    })
  }

  return {
    todos,
    getTodos,
  }
}, { persist: true })
