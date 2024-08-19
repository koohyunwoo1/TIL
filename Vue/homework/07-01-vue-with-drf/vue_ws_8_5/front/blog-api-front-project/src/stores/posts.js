import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'

export const usePostStore = defineStore('post', () => {
  const router = useRouter()
  const postList = ref([])
  const getPostList = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/posts/'
    })
    .then(res => postList.value = res.data)
    .catch(err => console.log(err))
  }
  const detailPost = ref([])
  const getDetailPost = function (pk) {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/api/v1/posts/${pk}`
    })
    .then(res => detailPost.value = res.data)
    .catch(err => console.log(err))
  }

  const createPost = function ({category, title, content}) {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/v1/posts/',
      data: {
        category,
        title,
        content
      }
    })
  }

  const updatePost = function ({pk, category, title, content}) {
    axios({
      method: 'put',
      url: `http://127.0.0.1:8000/api/v1/posts/${pk}/`,
      data: {
        category,
        title,
        content
      }
    })
  }

  const deletePost = function (pk) {
    axios({
      method: 'delete',
      url: `http://127.0.0.1:8000/api/v1/posts/${pk}/`,
    })
    .then(res => router.push({name:'posts'}))
  }
  return { postList, getPostList, detailPost, getDetailPost, createPost, deletePost, updatePost }
})
