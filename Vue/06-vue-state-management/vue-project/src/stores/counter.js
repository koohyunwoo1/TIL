import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {

  let id = 0
  const todos = ref([])

  const addTodo = function(todoText) {
    todos.value.push({
      id: id++,
      text: todoText,
      isDone: false
    })
  }

  const deleteTodo = function(todoId) {
    console.log(todoId)
    // todos 상태에서 인자로 todo(삭제 대상)를 찾아서 & 삭제를 한 새로운 배열을 반환
    const index = todos.value.findIndex((todo) => todo.id === todoId)
    console.log(index)
    todos.value.splice(index, 1)
    // 찾은 index를 활용하여 todos에서 삭제 후 
    // 새로운 todos로 교체
  }

  const updateTodo = function(todoId) {
    // 전달 받은 todoId(수정 대상)을 활용
    // todos 배열을 순회하면서 id가 일치하면 isDone을 반대로 바꾸고
    // 변경된 새로운 배열을 반환
    todos.value = todos.value.map((todo) => {
      if (todo.id === todoId ){
        todo.isDone = !todo.isDone
      } 
      return todo
    })
  }


  const doneTodosCount = computed(() => {
    const doneTodos = todos.value.filter((todo) => todo.isDone)
    return doneTodos.length
  })

  return { todos, addTodo, deleteTodo, updateTodo, doneTodosCount }

}, { persist: true})
