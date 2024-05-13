import { createRouter, createWebHistory } from 'vue-router'
import TodoView from '@/views/TodoView.vue'
import DetailView from '@/views/DetailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'TodoView',
      component: TodoView
    },
    {
      path: '/todo/:id',
      name: 'DetailView',
      component: DetailView
    },
  ]
})

export default router
