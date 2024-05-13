import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'
import { usePostStore } from './posts.js'

export const useCommentStore = defineStore('comment', () => {
  const postStore = usePostStore()
  const commentCreate = function (pk, content) {
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/api/v1/posts/${pk}/comments/`,
      data: {
        content
      }
    })
    .then(res => postStore.detailPost.comment_set.push(res.data))
    .catch(err => console.log(err))
  }
  return { commentCreate }
})
