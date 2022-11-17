<template>
  <div @click='goDetail(movie)'>
    <!-- {{movie}} -->
    <p>제목 : {{movie.title}}</p>
    <p>평점 : {{movie.vote_average}}</p>
    <p>{{movie.overview}}</p>
    <!-- <p>{{movie.id}}</p> -->
    <!-- <router-link
    :to="{ name: 'Detail',params : { id : movie.id } }"
    >[Detail]</router-link> -->
  </div>
</template>

<script>
export default {
    name : 'MovieCard',
    props : {
        movie : Object,
    },
    methods : {
      goDetail(movie) {
        console.log(movie)
        this.$router.push({name:'Detail',params:{id:`${movie.id}`}})
      }
    }
}
</script>

<style>

</style>