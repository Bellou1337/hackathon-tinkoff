<script setup>
defineProps({
  Naming:String,
  countOfMoney: Number,
  banknote: String
})
</script>

<template>
  <div>  
<button class="mx-auto rounded-lg bg-white shadow w-full max-w-80">
  <div class="p-4">
    <h3 class="text-xl font-medium text-gray-900">{{ Naming }}</h3>
    <p class="mt-1 text-gray-500"> {{ countOfMoney }} {{ banknote }}</p>
  </div>
</button>

  </div>
</template>
