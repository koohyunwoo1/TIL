import { ref, computed } from 'vue'
import { defineStore } from 'pinia'


export const useProductStore = defineStore('product', () => {
  let id = 0
  const products  = ref([
    {
      id: 1, title: 'Product 1', content: 'quia et suscipit suscipit recusandae'
    },
    {
      id: 2, title: 'Product 2', content: 'quo iure voluptatem occaecati omnis'
    },
    {
      id: 3, title: 'Product 3', content: 'repudiandae veniam quaerat sunt'
    },
  ])
  

  return { products }

})
