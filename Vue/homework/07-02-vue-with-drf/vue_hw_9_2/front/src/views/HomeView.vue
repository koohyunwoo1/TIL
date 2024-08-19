<template>
  <div>
    <h1>게시글 목록 페이지</h1>
    <button @click="router.push({name: 'create'})">게시글 생성</button>
    <ArticleList />
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import ArticleList from '../components/ArticleList.vue';
const router = useRouter()
</script>

<style lang="scss" scoped>

</style>