import axios from 'axios'
import { defineStore } from 'pinia'
import { usePostStore } from './posts.js'
import { useRouter } from 'vue-router'

export const useCommentStore = defineStore('comment', () => {
  const router = useRouter()
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

  const commentDelete = function(postPk, commentPk) {
    axios({
      method: 'delete',
      url: `http://127.0.0.1:8000/api/v1/posts/${postPk}/comments/${commentPk}/`,
    })
    .then(res => {
      postStore.detailPost.comment_set = postStore.detailPost.comment_set.filter((comment) => {
        return comment.id != commentPk
      })
    })
  }
  return { commentCreate, commentDelete }
})
