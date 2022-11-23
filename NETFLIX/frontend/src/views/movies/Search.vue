<template>
  <div class="home">
    <div class="input-group flex-nowrap">
  <input type="text" class="form-control" v-model="keyword" placeholder="영화제목을 입력하세요" @keyup.enter="search"> 
  <button class="input-group-text" id="addon-wrapping" @click="search">검색</button><br>
  </div><br>
  <div class="popular-list row  row-cols-md-5 ">
      <MovieCard
        v-for="(movie, idx) in searchData"
        :key="idx"
        :movie="movie"/>
    </div>
  </div>

</template>

<script>
import { mapGetters } from 'vuex'
import MovieCard from '@/components/movies/MovieCard'
export default {
    name : 'Search',
    components: {
    MovieCard,
  },
    data(){
        return {
            keyword:"",
            movieList:"",
            searchData : [],
        }
    },
    methods: {
    setToken() {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    search() {
        console.log(this.keyword)
        if(!this.keyword.trim()){
            alert("영화 제목을 입력하세요!");
            this.keyword = ""
            return;
        }
        const data = this.$store.state.movies.filter((movie)=> {
            return movie.title.includes(this.keyword)
        })
        console.log(data)
        this.searchData = data
        this.keyword = ''
    }
  },
    computed: {
    ...mapGetters([
      'movies', 'genre_names'
    ]),
    imgSrc: function () {
      return "https://image.tmdb.org/t/p/original" + this.searchData.poster_path
    },
  },
  created() {
    this.$store.dispatch('getMovies', this.setToken())
    this.$store.dispatch('getGenres', this.setToken())
    console.log(this.$store.state.movies)
  },
}
</script>

<style>

</style>