<template>
  <div>
    <h1>detail!!!</h1>
    <img :src="poster" alt="">
    <p>제목 : {{movie?.title}}</p>
    <!-- <p>{{movie?.vote}}</p> -->

    <p>관객 수 : {{movie?.popularity}}</p>
    <p>개봉일 : {{movie?.release_date}}</p>
    <p>줄거리 : {{movie?.overview}}</p>

    <!-- <span v-for="(genre,index) in movie.genre" 
    :key="index">{{genre.name}}</span> -->
    <!-- {{movie.genre.name}} -->
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'
export default {
    name : 'DetailView',
    data() {
      return {
        movie : null,
        poster : null,
      }
    },
    // props: {
    //   movie : Object,
    // },
    methods: {
      getMovieDetail() {
        const movie_id = this.$route.params.id
        // console.log(movie_id)
        axios({
          method : 'get',
          url : `${API_URL}/api/v1/movies/`,
          headers : true
        })
        .then((res) => {
          console.log(res)
          const detail = res.data.filter((movie)=> {
            // console.log(movie.movie_id === Number(movie_id)) 
            return Number(movie.movie_id) === Number(movie_id)
          })
          this.movie = detail[0]
          this.poster = this.movie.poster_path
          console.log(this.movie)
          // this.movie = res.data
          // console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },
    created() {
      this.getMovieDetail()
    },


}
</script>

<style>

</style>