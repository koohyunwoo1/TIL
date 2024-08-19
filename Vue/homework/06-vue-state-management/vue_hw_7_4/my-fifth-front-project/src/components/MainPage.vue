<template>
  <div>
    <p>이름 : {{ balance.name }}</p>
    <p>잔고 : {{ balance.balance }}</p>
    <button @click="update" class="button">updateBalance</button>
    <hr>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { ref } from 'vue'

const router = useRouter()
const props = defineProps({
  balance: Object
})

const update = function() {
  router.push({name:'update', params:{name: props.balance.name}})
}

</script>

<style scoped>

.button {
  background-color: #007BFF;
  border: 1px solid #007BFF;
  border-radius: 10%;
  color: white;
}
</style>