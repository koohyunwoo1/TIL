<template>
  <div>
    <h3>자식 페이지 입니다.</h3>
    <p>{{ attr }}</p>
    <p>{{ onlyMyText }}</p>
    <SearchForm 
      :only-my-text="onlyMyText"
      @change-word="onChageWord"
    />
    <p>{{ obj.name }}</p>
    <p>{{ name }}</p>
  </div>
</template>

<script setup>
  import SearchForm from './SearchForm.vue';
  import { ref } from 'vue'
  const onlyMyText = ref('child')
  // prop 받은 데이터가 복잡한 객체 형태여서,
  // 그 객체가 가지고 있는 구조 내의 특정 값만 별도로 활용해야 한다면,
  // 변수에 담아서 쓸 수도 있다.
  // 단, 절대, 하위 컴포넌트에서 함부로 데이터를 변경하지 말자.
  const props = defineProps({
    attr: String,
    obj: Object
  })
  // 이렇게 하면 안된다.
  // 하위 컴포넌트에서 prop받은 데이터 변경 안한다.
  // props.obj.name = '홍길동'
  const { name } = props.obj
  console.log(name)

  const onChageWord = function(text) {
    if (text.length >= 10) {
      onlyMyText.value = text
    } else {
      console.warn('글자수 부족')
    }
  }
</script>

<style scoped>

</style>