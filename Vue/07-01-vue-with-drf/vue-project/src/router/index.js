import { createRouter, createWebHistory } from 'vue-router'
import ArticleView from '@/views/ArticleView.vue'
import DetailView from '@/views/DetailView.vue'
import CreateView from '@/views/CreateView.vue'
// import SignUpView from '@/views/SignUpView.vue'
// import LogInView from '@/views/LogInView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'ArticleView',
      component: ArticleView
    },

    // 단일 게시글 조회
    // detail은 받을때 params가 필요함
    // id로 해줬기 때문에 id로 받아줘야됨
    {
      path: '/articles/:id',
      name: 'DetailView',
      component: DetailView
    },
    // 게시글 작성
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },
    // {
    //   path: '/signup',
    //   name: 'SignUpView',
    //   component: SignUpView
    // },
    // {
    //   path: '/login',
    //   name: 'LogInView',
    //   component: LogInView
    // }
  ]
})

export default router
