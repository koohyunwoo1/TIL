import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import PostListView from '@/views/PostListView.vue'
import PostDetailView from '@/views/PostDetailView.vue'
import CategoryCreateView from '@/views/CategoryCreateView.vue'
import PostFormView from '@/views/PostFormView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView
    },
    {
      path: '/posts',
      name: 'posts',
      component: PostListView
    },
    {
      path: '/detail/:pk',
      name: 'detail',
      component: PostDetailView
    },
    {
      path: '/category',
      name: 'category',
      component: CategoryCreateView
    },
    {
      path: '/post',
      name: 'postCreate',
      component: PostFormView
    },
    {
      path: '/post/:pk',
      name: 'postUpdate',
      component: PostFormView
    },
  ]
})

export default router
