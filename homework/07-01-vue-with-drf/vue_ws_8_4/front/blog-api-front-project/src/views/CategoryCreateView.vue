<template>
  <form class="category-form" @submit.prevent="createCategory">
    <label for="name" class="form-label">Category 종류:</label>
    <input type="text" name="name" id="name" v-model="name" class="form-input">
    <button type="submit" class="submit-button">카테고리 생성</button>
  </form>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue';
import { useRouter } from 'vue-router';
const router = useRouter()
const name = ref('')

const createCategory = function () {
  axios({
    method: 'post',
    url: 'http://127.0.0.1:8000/api/v1/category/',
    data: {
      name: name.value
    }
  })
  .then(res => {router.push({name: 'main'})})
}

</script>


<style  scoped>
.category-form {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  background-color: #fff;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.form-label {
  font-size: 16px;
  display: block;
  margin-bottom: 8px;
}

.form-input {
  width: calc(100% - 20px);
  padding: 10px;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 5px;
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