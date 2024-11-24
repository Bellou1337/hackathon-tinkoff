<script setup>
import { ref } from 'vue'
import { getCookie } from '@/utils/cookies'
import apiClient from '@/services'

const props = defineProps({
  name: String,
  amount: Number,
  currency: String,
  date: String,
  id: Number,
})

const isDeleted = ref(false)

const emit = defineEmits(['transactionDeleted'])

const deleteTransaction = async () => {
  try {
    const token = await getCookie('auth_token')

    if (!token) {
      throw new Error('Token not found')
    }

    const response = await apiClient.post(
      '/transaction/delete',
      {
        transaction_id: props.id,
      },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    )

    if (response.status === 200) {
      console.log('Deleted')
      isDeleted.value = true
      emit('transactionDeleted', props.id)
    }
  } catch (err) {
    console.log(err)
  }
}
</script>

<template>
  <div
    v-if="!isDeleted"
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
      <button @click="deleteTransaction">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          stroke-width="1.5"
          stroke="currentColor"
          class="size-6"
        >
          <path stroke-linecap="round" stroke-linejoin="round" d="M6 18 18 6M6 6l12 12" />
        </svg>
      </button>
    </div>
  </div>
</template>
