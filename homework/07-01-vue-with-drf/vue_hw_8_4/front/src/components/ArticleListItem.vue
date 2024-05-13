<template>
  <div>
    <h2>
      {{ article.id }}번 게시글
    </h2>
    <p>
      제목 : {{ article.title }}
    </p>
    <p>
      내용 : {{ article.content }}
    </p>
    <hr>
  </div>
</template>

<script setup>
import { ref } from 'vue'

defineProps({
  article : Object
})

</script>

<style scoped>

</style>