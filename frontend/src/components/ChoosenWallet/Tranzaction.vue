<script setup>
defineProps({
    to:String,
    spend:String,
    bancnote:String
})
</script>

<template>
  <div class="flex-col w-full max-w-96 my-1 h-20 bg-slate-200 flex items-center justify-center">
    <p class="text-xl"> {{ to }}</p>
    <p class="text-3xl">{{ spend }} {{ bancnote }}</p>
  </div>
</template>
