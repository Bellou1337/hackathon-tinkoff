<script setup>
defineProps({
  name: String,
  amount: Number,
  currency: String,
  date: String,
})
</script>


<template>
  <div
    class="flex w-full min-h-20 max-h-44 h-auto bg-white hover:bg-white/50 rounded-xl px-5 shadow-xl justify-between items-center"
  >
    <div class="w-1/3">
        <div class="overflow-x-auto">
          <div>
            <p class="text-xl font-bold text-slight-black">{{ name }}</p>
          </div>
        </div>
      
      <p class="inline-block mt-1 text-gray-500">{{ date }}</p>
    </div>
    <div class="w-1/3 flex flex-col items-center justify-center text-center">
      <p class="text-lg md:text-3xl font-bold text-slight-black">{{ amount }} {{ currency }}</p>
    </div>
    
    <div class="flex flex-col gap-2 items-center justify-center">
      <button
  @click="">
  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6">
    <path stroke-linecap="round" stroke-linejoin="round" d="M6 18 18 6M6 6l12 12" />
  </svg>
</button>
    <router-link  to="/profile/wallet/changeTransaction"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"     stroke="currentColor" class="size-4">
      <path stroke-linecap="round" stroke-linejoin="round" d="m16.862 4.487 1.687-1.688a1.875 1.875 0 1 1 2.652 2.652L6.832 19.82a4.5 4.5 0 0 1-1.897 1.13l-2.685.8.8-2.685a4.5 4.5 0 0 1 1.13-1.897L16.863 4.487Zm0 0L19.5 7.125" />
      </svg>

    </router-link>
      

    </div>
  </div>
</template>
