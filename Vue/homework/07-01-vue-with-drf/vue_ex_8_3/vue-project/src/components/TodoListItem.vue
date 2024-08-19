<template>
  <div>
    <p>{{ todo.work}}</p>
    <p>{{ todo.content}}</p>
    <p>{{ todo.is_completed}}</p>
    <p>{{ todo.created_at}}</p>
    <RouterLink :to="{name : 'DetailView', params: {id: todo.id}}">상세보기</RouterLink>
  </div>
  <hr/>
</template>

<script setup>
import { defineProps } from 'vue'
import { RouterView, RouterLink } from 'vue-router'


defineProps({
  todo: Object
})
</script>
