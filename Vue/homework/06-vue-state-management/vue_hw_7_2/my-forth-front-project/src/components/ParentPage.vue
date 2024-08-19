<template>
  <div class="container">
    <h2>부모 컴포넌트</h2>
    <p>
    {{ family.father }}
  </p>
    <p>
      {{ family.mother }}
    </p>
    <ChildPage :children="family.children"/>
      
  </div>
</template>

<script setup>
import { ref } from 'vue'
import ChildPage from '@/components/ChildPage.vue';
import { defineProps  } from 'vue';

defineProps({
  family: Object
})
</script>

<style scoped>
.container {
  background-color: #F9F9F9;
  text-align: center;
  padding: 15px;
  border: 1px solid #CCCCCC;
  margin-bottom: 20px;
  margin-left: 40px;
  margin-right: 40px;
}
</style>