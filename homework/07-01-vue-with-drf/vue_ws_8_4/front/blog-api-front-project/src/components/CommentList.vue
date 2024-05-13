<template>
  <li>
    <span class="comment-id">{{ comment.id }}</span>
    <span class="comment-content">{{ comment.content }}</span>
  </li>
</template>

<script setup>
defineProps({
  comment: Object
})
</script>

<style lang="scss" scoped>

</style>