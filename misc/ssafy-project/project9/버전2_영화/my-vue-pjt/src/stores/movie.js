
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'


export const useMovieStore = defineStore('Movie', () => {
  const movies = ref([])

  const API_KEY = import.meta.env.VITE_TMDB_API_KEY

  const getMovies = function() {
    axios({
      method: 'get',
      url: `https://api.themoviedb.org/3/movie/top_rated?language=ko-KR&api_key=${API_KEY}`
    })
    .then((response) => {
      movies.value = response.data.results
    })
    .catch((error) => {
      console.log(error)
    })
  }

  return { movies, getMovies}
},
{ persist: true }
)


