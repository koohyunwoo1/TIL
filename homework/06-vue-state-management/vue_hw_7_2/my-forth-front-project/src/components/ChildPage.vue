<template>
  <div v-for="child in children" class="container">
    <h3>자식 페이지</h3>
    <p>{{ child.name }}</p>
  </div>
</template>

<script setup>
import { ref, defineProps} from 'vue'
import { useFamilyStore } from '@/stores/family'

const store = useFamilyStore()

defineProps({
  children: Object
})

</script>

<style scoped>
.container {
  background-color: #FFFFFF;
  text-align: center;
  padding: 15px;
  border: 1px solid #CCCCCC;
  margin-bottom: 20px;
  margin-left: 40px;
  margin-right: 40px;
}
</style>