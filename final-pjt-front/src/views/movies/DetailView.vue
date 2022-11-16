<template>
  <div>
    <h1>detail!!!</h1>
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
      }
    },
    created() {
      this.getMovieDetail()
    },
    methods: {
      getArticleDetail() {
        axios({
          method : 'get',
          url : `${API_URL}/`
        })
      }
    }


}
</script>

<style>

</style>