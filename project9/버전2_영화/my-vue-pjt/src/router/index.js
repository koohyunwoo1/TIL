import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import MovieListView from '@/views/MovieListView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import ReviewSearchView from '@/views/ReviewSearchView.vue'
import RecommendedView from '@/views/RecommendedView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/',
      name: 'HomeView',
      component: HomeView
    },
    {
      path:'/movies',
      name: 'MovieListView',
      component: MovieListView
    },
    {
      path:'/:movieId',
      name: 'MovieDetailView',
      component: MovieDetailView
    },
    {
      path:'/review-search',
      name: 'ReviewSearchView',
      component: ReviewSearchView
    },
    {
      path:'/recommended',
      name: 'RecommendedView',
      component: RecommendedView
    }
  ]
})

export default router
