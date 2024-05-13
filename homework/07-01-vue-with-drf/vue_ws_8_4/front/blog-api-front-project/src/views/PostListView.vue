<template>
  <div>
    <h1>게시글 목록 페이지</h1>
    <RouterLink :to="{name:'postCreate'}"> 게시글 생성</RouterLink>
    <ul>
      <div
          v-for="post in store.postList"
          :key="post.pk"
          :post="post"
          @click="goDetail(post.pk)"
        >
        <p>{{ post.category.name }}</p>
        <h3> <span>{{ post.pk }}번 글 |</span>  {{ post.title }}</h3>
        <hr>
      </div>
    </ul>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { onMounted } from 'vue';
import { usePostStore } from '../stores/posts';
import { useRouter } from 'vue-router'
const router = useRouter()
const store = usePostStore()
onMounted(() => {
  store.getPostList()
})

const goDetail = (pk) => {
  router.push({name:'detail', params:{pk: pk}})
}

</script>

<style lang="scss" scoped>

</style>