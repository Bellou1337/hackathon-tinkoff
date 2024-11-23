<script setup>
defineProps({
  Naming:String,
  countOfMoney: Number,
  banknote: String
})
</script>

<template> 
  <RouterLink to="/profile/wallet" class="p-4 block m-auto bg-white hover:bg-[#FFE041] active:bg-yellow-500 rounded-3xl shadow-xl w-2/3 h-full">
    <h3 class="text-xl font-medium text-gray-900">{{ Naming }}</h3>
    <p class="mt-1 text-gray-500"> {{ countOfMoney }} {{ banknote }}</p>
  </RouterLink>
</template>
