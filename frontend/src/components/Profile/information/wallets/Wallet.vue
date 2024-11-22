<script setup>
defineProps({
  Naming:String,
  countOfMoney: Number,
  banknote: String
})
</script>

<template> 
  <a href="#" class=" bg-gray-100 p-4 block mx-auto hover:bg-yellow-300 active:bg-yellow-400 rounded-lg shadow w-full h-full max-w-80">
    <h3 class="text-xl font-medium text-gray-900">{{ Naming }}</h3>
    <p class="mt-1 text-gray-500"> {{ countOfMoney }} {{ banknote }}</p>
  </a>
</template>
