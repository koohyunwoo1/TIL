<template>
  <div>
    <h1>학생 상세 정보 목록 입니다.</h1>
    <p v-for="student in students"
        :key="student.id"
        :student="student"
        @click="go(student.name)">
      {{ student.name }} 학생 정보 보기
    </p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router';

const students = ref([
  { id: 1, name: '김하나'},
  { id: 2, name: '김두리'},
  { id: 3, name: '김서이'},
])

const router = useRouter()
const go = function(name) {
  console.log(name)
  // router.push(`/students/${name}`)
  router.push({ name:'students-name', params : {name : name}})
}
</script>

<style scoped>

</style>
