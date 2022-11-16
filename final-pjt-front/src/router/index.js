import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieListView from '../views/movies/MovieListView.vue'
import DetailView from '../views/movies/DetailView.vue'
import RecommendView from '../views/movies/RecommendView.vue'
// import WatchListView from '../views/movies/WatchListView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/movies',
    name: 'MovieList',
    component: MovieListView
  },
  {
    path: '/movies/recommend',
    name: 'Recommend',
    component: RecommendView
  },
  {
    path: '/movies/:id',
    name: 'Detail',
    component: DetailView
  },
 
  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  // }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
