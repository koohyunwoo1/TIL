import axios from 'axios'
import { defineStore } from 'pinia'

export const usePostStore = defineStore('post', () => {
  const getPostList = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/posts/'
    })
    .then(res => console.log(res))
    .catch(err => console.log(err))
  }
  return { getPostList }
})
