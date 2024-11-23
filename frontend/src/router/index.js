import { createRouter, createWebHistory } from 'vue-router'

import Home from '@/components/Home.vue'
import Login from '@/components/auth/Login.vue'
import Register from '@/components/auth/Register.vue'
import Verify from '@/components/auth/Verify.vue'
import Wallet from '@/components/ChoosenWallet/ChoosenWallet.vue'
import Profile from '@/components/profile/ProfileView.vue'
import NewWallet from '@/components/profile/information/wallets/newWallet.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/auth/login', component: Login },
  { path: '/auth/register', component: Register },
  { path: '/auth/verify', component: Verify },
  { path: '/profile/wallet', component: Wallet },
  { path: '/profile', component: Profile },
  { path: '/profile/newWallet', component: NewWallet },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
