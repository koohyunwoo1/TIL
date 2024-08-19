import axios from 'axios'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { defineStore } from 'pinia'

export const useArticleStore = defineStore('article', () => {
  const articles = ref([])

  const getArticles = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/articles/'
    })
    .then(res => {
      console.log(res.data)
      articles.value = res.data
    })
    .catch(err => {
      console.log(err)
    })

  }

  const createArticle = function(title, content, router) {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/v1/articles/',
      data: {
        title: title,
        content: content,
      }
    })
    .then((res) => {
      console.log(res.data)
      router.push({ name: 'home'})
    })
    .catch((err) => {
      console.log(err)
    })
  }

  return { articles, getArticles, createArticle }
})
