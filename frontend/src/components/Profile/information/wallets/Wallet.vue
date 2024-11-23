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
    class="p-4 block mx-auto bg-white hover:bg-yellow-300 active:bg-yellow-500 rounded-3xl shadow-xl w-3/4 h-full"
  >
    <h3 class="text-xl font-bold text-gray-900">{{ name }}</h3>
    <p class="mt-1 text-gray-500">{{ amount }} {{ currency }}</p>
  </router-link>
</template>
