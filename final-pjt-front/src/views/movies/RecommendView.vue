<template>
  <div>
    <h1>RecommendView</h1>
    {{movieData}}
  </div>
</template>

<script>
import axios from 'axios'
// const API_URL = 'http://127.0.0.1:8000/api/v1/movies/'
axios.defaults.baseURL = 'http://127.0.0.1:8000/' //백엔드 요청경로


// const AxiosInst = Axios.create({
//     baseURL : 'http://127.0.0.1:8000'
// })

// AxiosInst.interceptors.request.use(
//     (config) => {
//         config.headers.authorization = 'token';
//         config.headers['Access-Control-Allow-Origin'] = '*';  // CORS 설정(모든 리소스 허용)
//         return config;
//     }
// )
// export default AxiosInst;

export default {
    name : 'RecommendView',
    data() {
      return {
        movieData : null,
      }
    },
    methods:{
      movieApi() {
        axios.get('/api/v1/movies',{
          headers : {
          'Access-Controal-Origin':'*',
          'Content-Type' : 'application/json; charset=utf-8'
        },
        })
        .then((response) => {
          
          console.log(111)
          // overview 있는 영화만 출력
          const datas = response.data.results.filter((movie)=>{
              return movie.overview
          })
          
          // 평점순 내림차순
          const datas2 = datas.sort((a,b)=>{
              return b['vote_average'] - a['vote_average']
          })
          const datas3 = datas2.slice(0,11)
          this.movieData = datas3
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