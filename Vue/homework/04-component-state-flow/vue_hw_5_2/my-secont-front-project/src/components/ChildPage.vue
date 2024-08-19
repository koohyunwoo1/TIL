<template>
  <div class="p">
    <h3>자식 페이지입니다.</h3>
    <p>
      이름 : {{ myChild.name }}
    </p>
    <p>
      나이 : {{ myChild.age }}
    </p>
  </div>
</template>

<script setup>
defineProps({
  myChild: Object
})
</script>

<style scoped>
  .p {
    border:1px solid gray;
    margin:10px;
    padding:20px;
  }

</style>