<template>
  <div class="create-post-page">
    <h1 v-if="route.name === 'postCreate'">게시글 생성 페이지</h1>
    <h1 v-else-if="route.name === 'postUpdate'">게시글 수정 페이지</h1>
    <form @submit.prevent="route.name === 'postCreate'? createPost() : updatePost()" class="post-form">
      <label for="category" class="form-label">카테고리 선택:</label>
      <select name="category" id="category" v-model="category" class="form-select">
        <option
          v-for="category in categoryStore.categoryList"
          :key="category.id"
          :value="category.id"
        >
          {{ category.name }}
        </option>
      </select>

      <label for="title" class="form-label">제목:</label>
      <input type="text" name="title" v-model="title" class="form-input">

      <label for="content" class="form-label">내용:</label>
      <textarea name="content" id="content" cols="30" rows="10" v-model="content" class="form-textarea"></textarea>
      <button v-if="route.name === 'postCreate'" class="submit-button">게시글 생성</button>
      <button v-if="route.name === 'postUpdate'" class="submit-button">게시글 수정</button>
    </form>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import { useCategoryStore } from '@/stores/categories'
import { usePostStore } from '@/stores/posts'
import { onMounted } from 'vue';
import { useRouter, useRoute, createWebHistory } from 'vue-router';

const router = useRouter()
const route = useRoute()

const pk = ref(1)
const title = ref('')
const content = ref('')
const category = ref(1)
const postStore = usePostStore()
const categoryStore = useCategoryStore()

watch(() => postStore.detailPost, (val) => {
  pk.value = val.id
  title.value = val.title
  content.value = val.content
  category.value = val.category.id
})

onMounted(() => {
  categoryStore.getCategoryList()
  if (route.name === 'postUpdate') {
    postStore.getDetailPost(route.params.pk)
  }
})


const createPost = function () {
  const post = {
    title: title.value,
    content: content.value,
    category: category.value
  }
  postStore.createPost(post)
  router.push({name: 'posts'})
}

const updatePost = function () {
  console.log('test')
  const post = {
    pk: pk.value,
    title: title.value,
    content: content.value,
    category: category.value,
  }
  postStore.updatePost(post)
  router.push({name: 'posts'})
}
</script>

<style scoped>
.create-post-page {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

h1 {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.post-form {
  background-color: #fff;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 20px;
}

.form-label {
  font-size: 16px;
  display: block;
  margin-bottom: 8px;
}

.form-select,
.form-input,
.form-textarea {
  width: 100%;
  padding: 10px;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-bottom: 10px;
}

.submit-button {
  display: block;
  width: 100%;
  padding: 10px;
  font-size: 16px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.submit-button:hover {
  background-color: #0056b3;
}
</style>