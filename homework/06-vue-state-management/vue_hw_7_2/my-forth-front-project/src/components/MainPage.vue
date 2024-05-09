<template>
  <div>
    <h1>pinia 연습하기</h1>
    <ParentPage 
      v-for="family in store.familyInfo"
      :key="family.id"
      :family="family"
    />
  </div>
</template>

<script setup>
import ParentPage from '@/components/ParentPage.vue'
import { useFamilyStore } from '@/stores/family'

const store = useFamilyStore()

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
