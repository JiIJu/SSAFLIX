<template>
  <div>
    <h1>Top10 영화</h1>
    <div v-for='movie in movieData' :key='movie.id'>
    <img :src="movie.poster_path" alt=""  width="200" height="300" class="d-inline-block align-text-top">
    <p>제목 : {{movie?.title}}</p>
    <!-- <p>{{movie?.vote}}</p> -->

    <p>관객 수 : {{movie?.popularity}}</p>
    <p>개봉일 : {{movie?.release_date}}</p>
    <p>줄거리 : {{movie?.overview}}</p>
    <hr>
  </div>
  </div>
</template>

<script>
import axios from 'axios'
// const API_URL = 'http://127.0.0.1:8000/api/v1/movies/'
const API_URL = 'http://127.0.0.1:8000' //백엔드 요청경로



export default {
    name : 'RecommendView',
    data() {
      return {
        movieData : null,
        poster : null,
      }
    },
    computed: {
      isLogin() {
        return this.$store.getters.isLogin
      }
    },
    methods:{
      getMovieRecommend() {
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
          // console.log(datas)
          // 평점순 내림차순
          const datas2 = datas.sort((a,b)=>{
              return b['vote_average'] - a['vote_average']
          })
          const datas3 = datas2.slice(0,10)
          this.movieData = datas3

          // console.log(datas)
      })            
      .catch((error)=>{
          console.log(error)
      })
        } else {
          alert('로그인이 필요한 페이지입니다.')
          this.$router.push({name : 'LogIn'})
        }
      }
    },
  created() {
    this.getMovieRecommend()
  }
}
</script>

<style>

</style>