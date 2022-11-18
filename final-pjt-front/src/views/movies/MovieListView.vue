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
import axios from 'axios'
import MovieCard from '@/components/MovieCard'

const API_KEY = '1cc991c3c4ede5f1631fb06af01f8fd8'
const API_URL = `https://api.themoviedb.org/3/movie/popular?api_key=${API_KEY}&language=ko-KR&page=1?sort_by=vote_average`
export default {
    name : 'IndexView',
    data() {
      return {
        movieData : null,
        addid : 1,
      }
    },
    components : {
      MovieCard
    },
    computed: {
      isLogin() {
        return this.$store.getters.isLogin
      }
    },
    methods:{
      movieApi() {
        if (this.isLogin) {
          axios({
          method : 'get',
          url : `${API_URL}/api/v1/movies/`,
          headers : {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        .then((response) => {
          
          // console.log(response)
          // overview 있는 영화만 출력
          const datas = response.data.filter((movie)=>{
              return movie.overview
          })

          this.movieData = datas

          // console.log(datas)
      })            
      .catch((error)=>{
          console.log(error)
      })
        } else {
          alert('로그인이 필요한 서비스입니다.')
          this.$router.push({name : 'LogIn'})
        }
      }
    },
  created() {
    this.movieApi()
  }
}
</script>

<style>

</style>