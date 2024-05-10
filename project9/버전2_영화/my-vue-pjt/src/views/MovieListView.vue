<template>
  <div>
    <div class="movie-list">
      <RouterLink v-for="movie in store.movies" class="movie-card" :to="{name : 'MovieDetailView', params: {movieId: movie.id}}">
        <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="image" class="movie-image">
        <b>
          <!-- {{ movie.id }} -->
          {{ movie.title }}
        </b>
        <p>
          {{ movie.overview }}
        </p>       
      </RouterLink>
    </div>
    <RouterView />
  </div>
</template>

<script setup>
import { ref, onMounted} from 'vue'
import { useMovieStore } from '@/stores/movie'
import router from '@/router';
import {useRouter} from 'vue-router'

const store = useMovieStore()

onMounted(() => {
  store.getMovies()
})

</script>

<style scoped>
.movie-card {
  width: 200px;
  border: 1px solid #ccc;
  padding: 10px;
}

.movie-image {
  width: 100%
}

.movie-list {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin-top: 20px;
}
</style>