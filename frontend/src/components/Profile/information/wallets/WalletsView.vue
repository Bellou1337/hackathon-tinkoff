<script setup>
import Wallet from '@/components/profile/information/wallets/Wallet.vue'
import { ref } from 'vue'

const wallets = ref([
  {
    name: 'первый',
    amount: 1000,
    currency: 'руб.',
  },
  {
    name: 'второй',
    amount: 1000,
    currency: 'руб.',
  },
  {
    name: 'третий',
    amount: 1000,
    currency: 'руб.',
  },
  {
    name: 'четвертый',
    amount: 1000,
    currency: 'руб.',
  },
  {
    name: 'пятый',
    amount: 1000,
    currency: 'руб.',
  },
  {
    name: 'шестой',
    amount: 1000,
    currency: 'руб.',
  },
])
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
          :amount="wallet.amount"
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
