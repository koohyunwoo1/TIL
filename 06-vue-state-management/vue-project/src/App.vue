<template>
  <div>
    <h1>Todo Project</h1>
    <h2>완료된 Todo : {{ store.doneTodosCount }}</h2>
    <TodoForm />
    <TodoList />


    <!-- 
    <p>
      {{ newNubmer }}
    </p>

    <p>
      {{ store.count }}
    </p>

    <p>
      {{ store.doubleCount }}
    </p>

    <button @click="store.increment()">+++</button> -->


  </div>
</template>

<script setup>
// import { ref, watchEffect } from 'vue'
// import { useCounterStore } from '@/stores/counter'

import TodoForm from '@/components/TodoForm.vue';
import TodoList from '@/components/TodoList.vue';
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

// const store = useCounterStore()

// // state
// console.log(store.count)
// const newNubmer = store.count + 
// // const newNubmer = ref(store.count + 1)

// // getters
// console.log(store.doubleCount)


// // watchEffect(() => {
// //   newNubmer.value = store.count + 1
// // })


</script>


<style scoped>

</style>
