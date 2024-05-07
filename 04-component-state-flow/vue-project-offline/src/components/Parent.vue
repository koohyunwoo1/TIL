<template>
  <div>
    <h1>부모 페이지 입니다.</h1>
    <p>여러개의 자식들을 가질 수 있습니다.</p>
    <hr>
    <!-- 자식 컴포넌트를 import -->
    <Child 
      v-for="item in items"
      :key="item"
      :attr="item"
      :obj="obj"
    />
    <OtherChild 
      :obj="obj"
    />
  </div>
</template>

<script setup>
  import Child from './Child.vue';
  import OtherChild from './OtherChild.vue';
  import { ref } from 'vue'
  const items = ['first', 'second', 'third']
  const obj = ref({
    name: 'Alice',
    age: 30
  })
 
</script>

<style scoped>

</style>