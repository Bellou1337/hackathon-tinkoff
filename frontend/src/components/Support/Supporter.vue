<script setup>
import Wallet from '@/components/support/WalletInSupport.vue'
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { getCookie } from '@/utils/cookies'
import apiClient from '@/services'

const wallets = ref([])
const dateFrom = ref('')
const dateTo = ref('')
const isLoading = ref(false)
const recommendation = ref('')
let intervalId = null

const fetchWallets = async () => {
  try {
    const token = await getCookie('auth_token')

    if (!token) {
      throw new Error('Token not found')
    }

    const response = await apiClient.get('/wallet/get_my', {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })

    if (response.status === 200) {
      console.log(response.data)

      wallets.value = response.data.map((wallet) => ({
        name: wallet.name,
        balance: wallet.balance,
        id: wallet.id,
        currency: 'руб.',
      }))
    }
  } catch (err) {
    console.log(err)
  }
}

const handleAnalyze = async ({ walletId }) => {
  console.log('Анализ:', walletId)

  if (!dateFrom.value || !dateTo.value) {
    return
  }

  try {
    const token = await getCookie('auth_token')

    const response = await apiClient.post(
      '/recomendations/generate',
      {
        wallet_id: walletId,
        start: dateFrom.value,
        end: dateTo.value,
      },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    )

    if (response.status === 200) {
      console.log(response)
      recommendation.value = ''
      startFetchingRecommendations(walletId, token)
    }
  } catch (error) {
    console.log(error)
  }
}

const startFetchingRecommendations = (walletId, token) => {
  if (intervalId) {
    clearInterval(intervalId)
  }

  intervalId = setInterval(async () => {
    isLoading.value = true
    try {
      const response = await apiClient.post(
        '/recomendations/get',
        {
          wallet_id: walletId,
        },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      )

      if (response.status === 200) {
        console.log('Рекомендации:', response.data)
        recommendation.value = 'Нет рекомендации'
        if (response.data.detail !== '-1') {
          clearInterval(intervalId)
          intervalId = null
          console.log('Остановка запроса: detail не равен -1')
          recommendation.value = response.data.detail
        }
      } else {
        clearInterval(intervalId)
        intervalId = null
        console.log(`Остановка запроса: статус ${response.status}`)
      }
    } catch (error) {
      console.log(error)
      clearInterval(intervalId)
      intervalId = null
    } finally {
      isLoading.value = false
    }
  }, 2000)
}

onMounted(() => {
  fetchWallets()
})

onBeforeUnmount(() => {
  if (intervalId) {
    clearInterval(intervalId)
  }
})
</script>

<template>
  <div
    class="bg-slight-gray gap-10 lg:my-32 my-8 max-w-screen-xl mx-auto flex lg:flex-row flex-col justify-center px-4"
  >
    <div class="lg:w-1/3">
      <div>
        <p class="text-3xl font-bold text-slight-black text-center mb-10">Текущие кошельки</p>
        <div>
          <div
            class="rounded-lg max-h-96 w-full p-0 overflow-y-auto flex flex-col mb-2 scrollbar-none"
          >
            <div
              class="flex flex-col w-full min-h-20 h-full rounded-xl justify-between items-center my-1"
            >
              <Wallet
                v-for="(wallet, index) in wallets"
                :key="index"
                class="my-2"
                :name="wallet.name"
                :amount="wallet.balance"
                :currency="wallet.currency"
                :id="wallet.id"
                @analyze="handleAnalyze"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="lg:w-2/3 w-full md:gap-10 sm:gap-2 gap-10 flex sm:flex-row flex-col">
      <div class="lg:w-1/2 sm:w-2/3  h-2/3 sm:order-1 order-2">
        <p class="text-3xl font-bold text-slight-black text-center mb-10">Советы от Лисёнка</p>
        <div class="bg-gray-200 shadow h-full rounded overflow-y-auto scrollbar max-h-96">
          <p class="text-base text-slight-black sm:p-5 p-2">
            Выберите промежуток времени для анализа и нажмите на кнопку "анализ", чтобы получить совет.
          </p>
          <p v-if="recommendation" class="text-base text-slight-black sm:p-5 p-2">
            {{ recommendation }}
          </p>
        </div>
      </div>
      <div class="lg:w-1/2 sm:w-1/3 sm:h-full h-1/3 sm:order-2 order-1 flex flex-col">
        <p class="text-3xl font-bold text-slight-black text-center mb-10">Дата и время</p>
        <div
          class="bg-gray-200 p-2 sm:p-10 rounded shadow flex flex-col gap-5 items-center justify-center"
        >
          <div class="bg-gray-300 shadow-lg h-full rounded p-1 sm:p-5">
            <p class="font-bold mb-2 text-center text-lg">От...</p>
            <input v-model="dateFrom" class="rounded text-center" type="date" />
          </div>

          <div class="bg-gray-300 shadow-lg h-full rounded p-1 sm:p-5">
            <p class="font-bold mb-2 text-center text-lg">До...</p>
            <input v-model="dateTo" class="rounded text-center" type="date" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
