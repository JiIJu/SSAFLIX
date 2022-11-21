<template>
<div class="recommend">
    <header>
      <h2>당신이 좋아할 만한</h2>

      <!-- <div>
      <v-select v-model="genre" :item="genres" itme-text="id" item-value="genre" v-on:change="conBox"></v-select>
      </div> -->
      <select 
        v-model="genre"
        @change="change" 
    >
        <option
            v-for   ="each in genres"
            :key    ="each.id"
            v-text  ="each.genre"
            :value  ="each.genre"
        ></option>

    </select>
      

      <h4>당신이 가장 좋아하는 장르는 {{ bestGenre }}입니다.</h4>
    </header>
    <div v-if="recommendMovies == null">
      선호하는 장르를 골라주세요!</div>
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
    genre : 'default',
    id : 'default',
    genres: [
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
    conBox : function() {
      console.log(this.cont)
    }
  },
  computed: {
    ...mapGetters([
      'recommendMovies', 'bestGenre'
    ])
  },
  created() {
    this.$store.dispatch('getLikeGenreMovies', this.setToken())
  }
}
</script>

<style>

</style>
