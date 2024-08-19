<template>
  <div class="main-page">
    <h1>OO이의 블로그</h1>
    <p>Welcome to my personal blog!</p>
    <hr>
    <h3>카테고리 목록</h3>
    <ul class="category-list">
      <li
        v-for="category in store.categoryList"
        :key="category.id"
        class="category-item"
      >
        {{ category.name }}
      </li>
    </ul>
  </div>
</template>

<script setup>
import { useCategoryStore } from '../stores/categories';
import { onMounted } from 'vue';
const store = useCategoryStore();
onMounted(() => {
  store.getCategoryList();
});
</script>

<style scoped>
.main-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #f7f7f7;
  padding: 20px;
  text-align: center;
}

h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: #333;
}

p {
  font-size: 1.2rem;
  color: #666;
}

h3 {
  font-size: 1.5rem;
  margin-top: 2rem;
  margin-bottom: 1rem;
  color: #333;
}

.category-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.category-item {
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
  color: #555;
  background-color: #fff;
  padding: 0.5rem 1rem;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: background-color 0.2s, color 0.2s;
}

.category-item:hover {
  background-color: #333;
  color: #fff;
}
</style>
