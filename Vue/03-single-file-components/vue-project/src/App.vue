<template>
<div>
  <h1>App.vue</h1>
  <MyComponent />
  <!-- 여는 태그 닫는 태그를 합쳐버린다. -->
</div>
</template>

<script setup>
// import MyComponent from './components/MyComponent.vue';
import MyComponent from '@/components/MyComponent.vue';
// 절대 경로
// @ :  src/ 경로를 뜻하는 약어
</script>



<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
