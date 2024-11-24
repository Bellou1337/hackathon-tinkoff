<script setup>
import Wallet from '@/components/profile/information/wallets/Wallet.vue'
import { ref, onMounted } from 'vue'
import { getCookie } from '@/utils/cookies'
import apiClient from '@/services'

const wallets = ref([])

const fetchWallets = async () => {
  try {
    const token = await getCookie('auth_token')

    if (!token) {
      throw new Error('Token not found')
    }

    const response = await apiClient.get('/wallet/get_my', {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })

    if (response.status === 200) {
      console.log(response.data)

      wallets.value = response.data.map((wallet) => ({
        name: wallet.name,
        balance: 0,
        id: wallet.id,
        currency: 'руб.',
      }))
    }
  } catch (err) {
    console.log(err)
  }
}

onMounted(() => {
  fetchWallets()
})
</script>

<template>
  <div class="mt-10 flex flex-col items-center gap-5">
    <p class="text-3xl font-bold text-slight-black">Текущие кошельки</p>
    <div class="rounded-lg max-h-96 w-full pl-4 overflow-y-auto flex flex-col mb-2 scrollbar">
      <div
        class="flex flex-col w-full min-h-20 h-full rounded-xl justify-between items-center my-1"
      >
        <Wallet
          v-for="wallet in wallets"
          key="index"
          class="my-2"
          :name="wallet.name"
          :id="wallet.id"
          :amount="wallet.balance"
          :currency="wallet.currency"
        />
      </div>
    </div>
    <router-link
      to="/profile/create-wallet"
      class="inline-block rounded-lg bg-yellow-300 px-5 py-3 text-sm font-medium transition hover:bg-yellow-400"
    >
      Создать кошелек
    </router-link>
  </div>
</template>
