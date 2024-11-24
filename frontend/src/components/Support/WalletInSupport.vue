<script setup>
import { useRouter } from 'vue-router'

const emit = defineEmits(['analyze'])

const props = defineProps({
  name: String,
  amount: Number,
  currency: String,
  id: Number,
})

const router = useRouter()

const navigateToWallet = () => {
  router.push(`/profile/wallet?id=${props.id}`)
}

const handleClick = () => {
  emit('analyze', { walletId: props.id })
}
</script>

<template>
  <div
    class="p-4 block mx-auto bg-white hover:bg-gray-100 active:bg-gray-200 rounded-3xl shadow-xl w-full h-full"
    @click="navigateToWallet"
  >
    <div class="flex items-center justify-between">
      <div class="flex flex-col justify-center">
        <h3 class="text-xl font-bold text-gray-900">{{ name }}</h3>
        <p class="mt-1 text-gray-500">
          <span class="font-semibold">Баланс</span> {{ amount }} {{ currency }}
        </p>
      </div>

      <!-- Кнопка с обработкой клика -->
      <button
        class="inline-block rounded-lg bg-yellow-300 px-5 py-3 text-sm font-medium transition hover:bg-yellow-400"
        @click.stop="handleClick"
      >
        Анализ
      </button>
    </div>
  </div>
</template>
