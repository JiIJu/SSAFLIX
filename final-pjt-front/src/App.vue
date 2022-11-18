<template>
  <div id="app">
    <nav>
      <router-link to="/movies">MovieList</router-link> |
      <!-- <router-link to="/movies/detail">Detail</router-link> | -->
      <router-link to="/movies/recommend">Top10</router-link> |
      <router-link to="/movies/latest">Latest movie</router-link> | 
      <router-link to="/accounts/signup">Sign Up</router-link> |
      <router-link to="/accounts/login" v-show='!this.$store.state.token'>LogIn</router-link> 
      <span @click='logOut' style="cursor: pointer; text-decoration: underline;" v-show='this.$store.state.token'><b>Logout</b></span>
    </nav>
    <router-view/>
  </div>
</template>
<script>
  export default {
      name : 'IndexView',
      methods : {
        logOut() {
        this.$store.commit('CLEAR_TOKEN')
        this.$router.go()
      },
      }
  }
    
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}


nav a {
  font-weight: bold;
  color: #2c3e50;
}
button {
  /* 생략 */

  background: white;
  color: var(#ffffff);

  cursor: pointer;

  transition: 0.5s;
}
nav a.router-link-exact-active {
  color: #42b983;
}


</style>
