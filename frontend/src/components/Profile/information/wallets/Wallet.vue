<script setup>
defineProps({
  Naming:String,
  countOfMoney: Number,
  banknote: String
})
</script>

<template> 
  <RouterLink to="/profile/wallet" class="p-4 block mx-auto bg-amber-300 hover:bg-yellow-400 active:bg-yellow-500 rounded-lg shadow w-full h-full max-w-80">
    <h3 class="text-xl font-medium text-gray-900">{{ Naming }}</h3>
    <p class="mt-1 text-gray-500"> {{ countOfMoney }} {{ banknote }}</p>
  </RouterLink>
</template>
