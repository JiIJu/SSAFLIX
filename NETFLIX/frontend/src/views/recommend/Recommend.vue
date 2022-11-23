<template>
<div class="recommend">
    <header>
      <select @change="pick($event)" class="btn dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false" style="float:right;">
        <option v-for="genre in genres" :key="genre.id">{{genre.genre}}</option>
      </select>

      <h2>당신이 좋아할 만한</h2>

      <h4 v-if="genre === ''">장르를 선택해 주세요</h4>
      <h4 v-else>{{ genre }} 장르를 모아봤어요</h4>
    </header>

    <!-- MovieCards -->
    <div class="popular-list row row-cols-1 row-cols-md-5 gy-3">
      <MovieCard
        v-for="(movie, idx) in recommendMovies"
        :key="idx"
        :movie="movie"/>
    </div>
  </div>
</template>

<script>

import { mapGetters } from 'vuex'
import MovieCard from '@/components/movies/MovieCard'

export default {
  name: 'Recommend',
  components: {
    MovieCard,
  },
  data() {
    return {
    genre : '',
    id : '',
    genres: [
    {genre : '장르를 선택해 주세요.' , id : -1},
    {genre : 'Adventure', id : 12},
    {genre : 'Fantasy', id : 14 },
    {genre : 'Animation', id : 16},
    {genre : 'Drama', id : 18},
    {genre : 'Horror', id : 27},
    {genre : 'Action', id : 28},
    {genre : 'Comedy', id : 35},
    {genre : 'History', id : 36},
    {genre : 'Western', id : 37},
    {genre : 'Thriller', id : 53},
    {genre : 'Crime', id : 80},
    {genre : 'Documentary', id : 99},
    {genre : 'Science Fiction', id : 878},
    {genre : 'Mystery', id : 9648},
    {genre : 'Music', id : 10402},
    {genre : 'Romance', id : 10749},
    {genre : 'Family', id : 10751},
    {genre : 'War', id : 10752},
    {genre : 'TV Movie', id : 10770},
    ] ,
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
    pick(event){
      console.log(event)
      this.genre = event.target.value
      const genre_id = this.genres.filter((movie) => {
        if (this.genre === movie.genre)
        {return movie.id}
      })
      console.log(this.genre , this.genre_id)
      this.id = genre_id[0].id
      // console.log(genre_id[0].id)
      // console.log(event); //value값 출력
      this.$store.dispatch('getLikeGenreMovies', {'token' : this.setToken(),'movie' : genre_id[0]})
    }
  },
  computed: {
    ...mapGetters([
      'recommendMovies', 'bestGenre'
    ])
  },
  // created() {
  //   this.$store.dispatch('getLikeGenreMovies', this.setToken())
  // }
}
</script>

<style>

</style>
