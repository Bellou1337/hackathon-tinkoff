<script setup>
defineProps({
  name: String,
  amount: Number,
  currency: String,
})
</script>

<template>
  <router-link
    to="/profile/wallet"
    class="px-3 py-2 mx-auto bg-white hover:bg-yellow-300 active:bg-yellow-500 rounded-3xl shadow-xl w-full h-full"
  >
  <div class="flex items-center justify-between">
    <h3 class="text-xl font-bold text-gray-900">{{ name }}</h3>
    <div class="flex flex-col items-center justify-center">
        <p class=" text-gray-500">Баланс</p>
        <p class="mt-1">{{ amount }} {{ currency }}</p>
    </div>
    <button class=" bg-primary-yellow  px-4 py-2 rounded-xl"> Анализ </button>
  </div>
  </router-link>
</template>