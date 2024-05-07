<template>
  <div>
    <h3>자식 페이지 입니다.</h3>
    <p>
      이름 : {{ myChild.name }}
    </p>
    <p>
      나이 :  {{ myChild.age }}
    </p>
    <p>
      용돈 : {{ myChild.balance }}
    </p>
    <button @click="giveMeAllowance">용돈 주세요.</button>
  </div>
</template>

<script setup>

defineProps({
  myChild: Object
})

const emit = defineEmits(['updateBalance'])

const giveMeAllowance = function() {
  emit('updateBalance')
}
</script>





<style scoped>

</style>
