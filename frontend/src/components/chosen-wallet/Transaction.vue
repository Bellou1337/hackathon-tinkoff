<script setup>
defineProps({
  label: String,
  amount: String,
  currency: String,
  date: String,
})
</script>

<template>
  <div
    class="flex w-full min-h-20 max-h-44 h-auto bg-white hover:bg-white/50 rounded-xl px-5 shadow-xl justify-between items-center"
  >
    <div>
      <p class="text-xl font-bold text-slight-black">{{ label }}</p>
      <p class="inline-block mt-1 text-gray-500">{{ date }}</p>
    </div>
    <p class="text-lg md:text-3xl font-bold text-slight-black">{{ amount }} {{ currency }}</p>
  </div>
</template>
