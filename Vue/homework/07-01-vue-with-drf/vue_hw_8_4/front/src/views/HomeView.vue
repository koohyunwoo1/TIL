<template>
  <div>
    <h1>게시글 목록 페이지</h1>
    <RouterLink :to="{name : 'create'}">게시글 생성</RouterLink>
    <ArticleList />
  </div>
</template>

<script setup>
import ArticleList from '@/components/ArticleList.vue';
import { RouterLink } from 'vue-router';
</script>

<style scoped>

</style>