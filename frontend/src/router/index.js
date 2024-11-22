import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/components/Home.vue'
import Login from '@/components/auth/Login.vue'
import Register from '@/components/auth/Register.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/auth/login', component: Login },
  { path: '/auth/register', component: Register },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
