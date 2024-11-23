<script setup>
defineProps({
    to:String,
    spend:String,
    banknote:String,
    date: String,
})
</script>

<template>
  <div class="flex w-full min-h-20 max-h-44 h-auto bg-slate-200 rounded-xl px-5 shadow-xl justify-between items-center">  
    <div>
      <p class="text-xl"> {{ to }}</p>
      <p class=" inline-block">{{ date }}</p>
    </div>
    <p class="text-3xl">{{ spend }} {{ banknote }}</p>
  </div>
</template>
