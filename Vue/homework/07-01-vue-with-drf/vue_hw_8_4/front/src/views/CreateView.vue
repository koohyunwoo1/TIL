<!-- CreateView.vue -->

<template>
  <div>
    <h1>게시글 생성 페이지</h1>
    <form @submit.prevent="submitForm">
      제목 : <input type="text" v-model.trim="title">
      내용 : <textarea v-model.trim="content"> </textarea>
      <input type="submit" value="create">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useArticleStore } from '@/stores/articles'

const store = useArticleStore()
const router = useRouter()
const title = ref('')
const content = ref('')

const submitForm = () => {
  store.createArticle(title.value, content.value, router)
}

</script>

<style scoped>
</style>
