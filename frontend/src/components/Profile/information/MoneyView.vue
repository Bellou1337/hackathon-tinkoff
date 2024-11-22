<template>
  <div class="flex items-center justify-center gap-10 mt-16 h-2/3">
      <!--Costs-->
      <div>
          <div class="flex items-center justify-center">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class=" h-40 w-40">
              <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 6 9 12.75l4.286-4.286a11.948 11.948 0 0 1 4.306 6.43l.776 2.898m0 0 3.182-5.511m-3.182 5.51-5.511-3.181" />
              </svg>
              <p class=" text-7xl">{{ costs }}</p>
          </div>
      </div>

      <!--Income-->
      <div>
          <div class="flex items-center">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class=" h-40 w-40">
               <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 18 9 11.25l4.306 4.306a11.95 11.95 0 0 1 5.814-5.518l2.74-1.22m0 0-5.94-2.281m5.94 2.28-2.28 5.941" />
              </svg>
              <p class=" text-7xl">{{ incomes }}</p>
          </div>
      </div>
  </div>
</template>

<script setup>
  import {ref} from 'vue'

  const costs = ref('1500');
  const incomes = ref('2000')

</script>