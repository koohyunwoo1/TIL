<template>
  <div>
    <nav>
      <RouterLink class="RouterLink" to="/">
          Home
      </RouterLink> 
      |
      <RouterLink class="RouterLink" to="/cart">
        Cart
      </RouterLink>
    </nav>
  
  
  <RouterView />
  </div>

</template>

<script setup>

</script>


<style scoped>
nav {
  text-align: center;
  margin-top: 20px;
}
.RouterLink {
  text-decoration-line: none;
}
</style>
