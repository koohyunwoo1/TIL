import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

let id = 0
export const useBalanceStore = defineStore('balance', () => {

  const balances = ref([
      { 
      id: id++,
      name: '김하나',
      balance: 100000
      },
      {
      id: id++,
      name: '김두리',
      balance: 10000
      },
      {
      id: id++,
      name: '김서이',
      balance: 100
      },
      
  ])

  const Info = computed (() => {
    return (name) => balances.value.filter((info) => info.name === name)[0]
  })

  const updateBalance = function (name) {
    balances.value = balances.value.map((info) => {
      if (info.name === name) {
        info.balance += 1000
      }
      return info
    })
  }

  return { balances, Info, updateBalance}
})