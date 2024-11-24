import { createRouter, createWebHistory } from 'vue-router'

import Home from '@/components/Home.vue'
import Login from '@/components/auth/Login.vue'
import Register from '@/components/auth/Register.vue'
import Verify from '@/components/auth/Verify.vue'
import Wallet from '@/components/chosen-wallet/ChosenWallet.vue'
import Profile from '@/components/profile/ProfileView.vue'
import CreateWallet from '@/components/profile/information/wallets/CreateWallet.vue'
import Support from '@/components/support/Supporter.vue'
import CreateTransaction from '@/components/chosen-wallet/CreateTransaction.vue'
import SharedWallet from '@/components/chosen-wallet/SharedWallet.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/auth/login', component: Login },
  { path: '/auth/register', component: Register },
  { path: '/auth/verify', component: Verify },
  { path: '/profile/wallet', component: Wallet },
  { path: '/profile/shared', component: SharedWallet },
  { path: '/profile', component: Profile },
  { path: '/profile/create-wallet', component: CreateWallet },
  { path: '/support', component: Support },
  { path: '/profile/wallet/create-transaction', component: CreateTransaction },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
