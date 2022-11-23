<template>
  <div class="home">
    <header>
      <h2 style="text-align:center;" @click="random">랜덤영화</h2>

    </header>
    <br><br>
    <div class="movie-detail-body">
        <div class="movie-detail-poster ">
          <img :src="imgSrc" alt="포스터 없음">
        </div>
        <div class="movie-detail-upper">
            <div class="movie-detail-info-header">
                <div class="movie-detail-info-header-left">
                    <div class="movie-detail-title">
                        {{ movies.title }}
                    </div>
                    <div
                        v-if="movies.release_date"
                        class="movie-release-date">
                        개봉  :  {{ movies.release_date }}
                    </div>
                </div>
                <div class="movie-detail-info-header-right">
                <div class="movies-vote">
                  {{ movies.vote_average }}
                </div>
                <img id="movie-star" src="@/assets/images/star.png">
              </div>
            </div>
            <div class="movie-detail-overview-header">
              줄거리
            </div>
            <hr>
            <div
              v-if="movies.overview"
              class="movie-detail-overview-body">
              {{ movies.overview }}
            </div>
            <div v-else
              class="movie-detail-overview-body">
              해당 영화는 줄거리가 제공되지 않습니다.
            </div>
        </div>
        <div class="movie-detail-lower">
          </div>
    </div>
</div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
    name : 'Random',
    methods: {
    setToken() {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    random() {
    this.$store.dispatch('randomMovies', this.setToken())
    // this.$store.dispatch('getGenres', this.setToken())
    }
  },
    computed: {
        ...mapGetters([
        'movies'
        ]),
        imgSrc: function () {
      return "https://image.tmdb.org/t/p/original" + this.movies.poster_path
    },

    },
    
    created() {
        this.$store.dispatch('randomMovies', this.setToken())
        // this.$store.dispatch('getGenres', this.setToken())
    },

}
</script>

<style>
h2:hover {
  cursor: pointer;
}
</style>