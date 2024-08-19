<template>
  <form @submit.prevent="createComment">
    <label for="content">내용 : </label>
    <input type="text" name="content" id="content" v-model="content">
    <button>댓글 작성</button>
  </form>
</template>

<script setup>
import { useCommentStore } from '@/stores/comments.js'
import { ref } from 'vue';
const store = useCommentStore()
const props = defineProps({
  postPk: Number
})
const content = ref('')
const createComment = function () {
  console.log(props)
  store.commentCreate(props.postPk, content.value)
}
</script>

<style lang="scss" scoped>

</style>