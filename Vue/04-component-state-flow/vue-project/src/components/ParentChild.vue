<template>
  <div>
    <p>
      {{ myMsg }}
      {{ dynamicProps }}
    </p>
    <ParentGrandChild
     :myMsg="myMsg"
     @update-name="updateName"
     />

    <button @click="$emit('someEvent')">클릭</button>
    <button @click="buttonClick">버튼2</button>
    <button @click="emitArgs">추가 인자 전달</button>

  </div>
</template>

<script setup>
import ParentGrandChild from '@/components/ParentGrandChild.vue';
// 내려받은 props를 선언
// defineProps(['myMsg'])

// 권장
const props = defineProps({
  myMsg: String,
  // myMsg : {
  //   type: String,
  //   required: true
  // },

  dynamicProps: String
})

console.log(props)
console.log(props.myMsg)

const emit = defineEmits(['myFocus', 'emitArgs', 'updateName'])

const buttonClick = function() {
  emit('myFocus')
}

const emitArgs = function() {
  emit('emitArgs', 1, 2)
}

const updateName = function() {
  emit('updateName')
}
</script>

<style scoped>

</style>