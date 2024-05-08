import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserView from '@/views/UserView.vue'
import UserProfile from '@/components/UserProfile.vue'
import UserPosts from '@/components/UserPosts.vue'
import UserHome from '@/components/UserHome.vue'
import LoginView from '@/views/LoginView.vue'

const isAuthenticated = true

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/user/:id',
      // name: 'user',
      component: UserView,
      // beforeEnter: (to, from) => {
        // console.log(to)
      // },
      children: [
        { path: '', name: 'user', component: UserHome },
        { path: 'profile', name: 'user-profile', component: UserProfile},
        { path: 'posts', name: 'user-posts', component: UserPosts},
      ]
    },
    {
      path:'/login',
      name: 'login',
      component: LoginView,
      beforeEnter: (to, from) => {
        if (isAuthenticated === true) {
          console.log('이미 로그인 상태입니다.')
          return { name: 'home' }
          // 이미 로그인 되어 있는 상태
          // 로그인 페이지로 들어갈려면 들어갈수 없게 하는 코드
        }
      }
    }
  ]
})

// 전역 가드
// router.beforeEach((to, from) => {
//   const isAuthenticated = false

//   if (!isAuthenticated && to.name !== 'login') {
//     console.log('로그인이 필요합니다.')
//     return { name: 'login' }
//   }
// })

export default router
