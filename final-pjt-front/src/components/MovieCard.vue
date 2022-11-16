<template>
  <div>
    <p>제목 : {{movie.title}}</p>
    <p>평점 : {{movie.vote_average}}</p>
    <p>{{movie.overview}}</p>
  </div>
</template>

<script>
export default {
    name : 'MovieCard',
    props : {
        movie : Object,
    }
}
</script>

<style>

</style>