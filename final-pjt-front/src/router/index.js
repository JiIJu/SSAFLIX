import Vue from 'vue'
import VueRouter from 'vue-router'
import IndexView from '../views/movies/IndexView.vue'
import DetailView from '../views/movies/DetailView.vue'
import RecommendView from '../views/movies/RecommendView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/movies',
    name: 'index',
    component: IndexView
  },
  {
    path: '/movies/:movieid',
    name: 'detail',
    component: DetailView
  },
  {
    path: '/movies/recommend',
    name: 'recommend',
    component: RecommendView
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
