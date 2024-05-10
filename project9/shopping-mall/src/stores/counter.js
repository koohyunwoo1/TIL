import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
// 컴포넌트 끼리 함께 사용하는 공간 ( 전역변수 )
export const useCartStore = defineStore('cart', () => {
  // store에 저장되는 변수 : state(상태)
  const products = ref([
    
  ])
  const carts = ref([

  ])

  // 누가 getProducts를 호출해야 할까 ?
  const getProducts = function() {
    // 외부에서 데이터 가져오기 axios 라이브러리
    axios({
      method: 'get',
      url: 'https://fakestoreapi.com/products',
    })
    .then((response) => {
      // console.log(response)
      products.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
    
  }

    const addCart = function(product) {
      carts.value.push(product)
    }
    
    const deleteCart = function(productId) {
      const idx = carts.value.findIndex(cart => cart.id === productId)
      if (idx !== -1) {
        carts.value.splice(idx, 1)
      }
    }


  return { products, getProducts, addCart, deleteCart, carts }
},
{ persist: true }
) 
