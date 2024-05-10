<template>

   <div>
    <img :src="`https://image.tmdb.org/t/p/w500${movies_detail.poster_path}`" alt="image">
      <p>
        <b>{{ movies_detail.title }}</b>
      </p>
      <p>
        개봉일 : {{ movies_detail.release_date }}
      </p>
      <p>
        러닝타임 : {{ movies_detail.runtime }}
      </p>
      <p>
        <b>
          장르
        </b>
      </p>

      <p v-for="genre in movies_detail.genres">
        {{ genre.name }}
      </p>

      <p>
        <b>
          줄거리
        </b>
      </p>
      <p>
        {{ movies_detail.overview }}
      </p>
      <p>
        <b>
          공식 예고편
        </b>
      </p>
      <img src="../assets/youtube.png" alt="no image" style="width: 100px;">
    </div>

</template>

<script setup>
import { ref, onMounted} from 'vue'
import { useMovieStore } from '@/stores/movie'
import { useRoute } from 'vue-router';
import axios from 'axios'

const store = useMovieStore()
const route = useRoute()
const movieId = route.params.movieId

const movies_detail = ref([])
const API_KEY = import.meta.env.VITE_TMDB_API_KEY

axios({
      method:'get',
      url:`https://api.themoviedb.org/3/movie/${movieId}?language=ko-KR&api_key=${API_KEY}`
    })
    .then((response)=>{
      movies_detail.value=response.data
    })
    .catch((error)=>{
    console.log(error)
    })



</script>

<style scoped>
img {
  margin-top: 30px;
  width: 200px;
}
div {
  text-align: center;
  
}
</style>