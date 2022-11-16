<template>
  <div>
    <h1>Movie List</h1>
    <MovieCard
    v-for="movie in movieData"
    :key='movie.id'
    :movie="movie"
    />
  </div>
</template>

<script>
import Axios from 'axios'
import MovieCard from '@/components/MovieCard'

const API_KEY = '1cc991c3c4ede5f1631fb06af01f8fd8'
const API_URL = `https://api.themoviedb.org/3/movie/popular?api_key=${API_KEY}&language=ko-KR&page=1?sort_by=vote_average`
export default {
    name : 'IndexView',
    data() {
      return {
        movieData : null,
      }
    },
    components : {
      MovieCard
    },
    methods:{
      movieApi() {
        Axios.get(`${API_URL}`)
        .then((response) => {
          console.log(response)
          // overview 있는 영화만 출력
          const datas = response.data.results.filter((movie)=>{
              return movie.overview
          })
          
          // 평점순 내림차순
          const datas2 = datas.sort((a,b)=>{
              return b['vote_average'] - a['vote_average']
          })
          
          this.movieData = datas2
          // console.log(datas)
      })            
      .catch((error)=>{
          console.log(error)
      })
      }
    },
  created() {
    this.movieApi()
  }
}
</script>

<style>

</style>