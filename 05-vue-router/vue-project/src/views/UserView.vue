<template>
  <div>
    <RouterLink :to="{ name: 'user-profile' }">Profile</RouterLink>
    <RouterLink :to="{ name: 'user-posts' }">Posts</RouterLink>

    <h1>UserView</h1>
    <!-- <h2>{{ $route.params.id }}번 User 페이지</h2> -->
    <h2>{{ userId }}번 User 페이지</h2>
    <button @click="goHome">홈으로 !</button>
    <button @click="routeUpdate">100번 유저 페이지</button>
    <hr>
    <RouterView />
  </div>
</template>

<script setup>

import { ref } from 'vue'
import { useRoute, useRouter, onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'

const route = useRoute()
const userId = ref(route.params.id)

const router = useRouter()
const goHome = function() {
  router.push({ name: 'home'})
  // router.replace({ name: 'home'})
  // replace : 뒤로가기가 불가능하다
}
const routeUpdate = function() {
  router.push({ name: 'user', params : { id : 100 }})
}

onBeforeRouteLeave((to, from) => {
  const answer = window.confirm('마 나가지마라')
  if (answer === false) {
    return false
  }
})

onBeforeRouteUpdate((to, from) => {
  userId.value = to.params.id
})
</script>

<style scoped>

</style>