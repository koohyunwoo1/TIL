<template>
  <div>

    <nav>
      
      <RouterLink class="RouterLink2" to="/">ssafy</RouterLink> 
      <RouterLink class="RouterLink" to="/movies">영화조회</RouterLink> 
      <RouterLink class="RouterLink" to="/review-search">리뷰검색</RouterLink>
      <RouterLink class="RouterLink" to="/recommended">영화추천</RouterLink>
      
    </nav>
    
    <RouterView />
  </div>
      
</template>


<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>


<style scoped>

nav {
  background-color: #C9D6DC;
  padding : 1rem;
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: right;
  font-weight: bold;
  }

.RouterLink {
  text-decoration-line: none;
}

.RouterLink2 {
  text-decoration-line: none;

}
</style>
