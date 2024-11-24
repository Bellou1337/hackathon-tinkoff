<script setup>
import { ref, computed, onMounted, reactive } from 'vue'
import { useRoute } from 'vue-router'
import Transaction from '@/components/chosen-wallet/Transaction.vue'
import Graph from '@/components/graphs/MoneyGraph.vue'
import apiClient from '@/services'
import { getCookie } from '@/utils/cookies'

const dropdownOpen = ref(false)
const dates = ref('')
const walletName = ref('')
const walletBalance = ref(0)
const incomes = ref(0)
const expenses = ref(0)

const route = useRoute()
const id = route.query.id

const chartData = computed(() => ({
  labels: ['Доходы', 'Расходы'],
  datasets: [
    {
      label: 'Доходы - Расходы',
      data: [incomes.value, expenses.value],
      backgroundColor: ['#facc15', '#313232'],
      hoverBackgroundColor: ['#20d457', '#c44242'],
      borderColor: 'transparent',
      borderWidth: 0,
      hoverBorderColor: 'transparent',
      hoverBorderWidth: 0,
    },
  ],
}))

const chartOptions = {
  responsive: true,
  plugins: {
    legend: {
      display: true,
      position: 'top',
      labels: {
        color: '#333333',
        font: {
          family: 'Geologica, sans-serif',
          size: 14,
          weight: 'bold',
        },
      },
    },
    title: {
      display: true,
      text: 'Доходы и Расходы',
      color: '#333333',
      font: {
        family: 'Geologica, sans-serif',
        size: 24,
        weight: 'bold',
      },
    },
    tooltip: {
      titleFont: {
        family: 'Geologica, sans-serif',
        size: 16,
        weight: 'bold',
      },
      bodyFont: {
        family: 'Geologica, sans-serif',
        size: 14,
      },
    },
  },
}

const categories = ref([])
const transactions = ref([])

const fetchCategories = async () => {
  try {
    const token = await getCookie('auth_token')

    if (!token) {
      throw new Error('Token not found')
    }

    const response = await apiClient.get('/category/get_all', {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })

    if (response.status === 200) {
      categories.value = response.data.map((category) => ({
        name: category.name,
        income: category.is_income,
        active: true,
        id: category.id,
      }))
    }
  } catch (err) {
    console.log(err)
  }
}

const fetchTransactions = async () => {
  try {
    const token = await getCookie('auth_token')

    if (!token) {
      throw new Error('Token not found')
    }

    const response = await apiClient.post(
      '/transaction/get_by_wallet_id',
      {
        wallet_id: id,
      },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    )

    if (response.status === 200) {
      incomes.value = 0
      expenses.value = 0

      transactions.value = response.data.map((transaction) => ({
        name: transaction.title,
        amount: transaction.amount,
        currency: 'руб.',
        date: convertDate(transaction.date),
        id: transaction.id,
        category_id: transaction.category_id,
      }))

      transactions.value.forEach((transaction) => {
        const category = categories.value.find((cat) => cat.id === transaction.category_id)
        if (category) {
          if (category.income) {
            incomes.value += transaction.amount
          } else {
            expenses.value += transaction.amount
          }
        }
      })
    }
  } catch (err) {
    console.log(err)
  }
}

const fetchWallet = async () => {
  try {
    const token = await getCookie('auth_token')

    if (!token) {
      throw new Error('Token not found')
    }

    const response = await apiClient.post(
      '/wallet/get_by_id',
      {
        id: id,
      },
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    )

    if (response.status === 200) {
      walletName.value = response.data.name
      walletBalance.value = response.data.balance
    }
  } catch (err) {
    console.log(err)
  }
}

const filter = computed(() => {
  const filterArray = []

  transactions.value.forEach((element) => {
    const dateMatch = element.date.includes(dates.value)
    const categoryMatch = categories.value.some(
      (category) => category.active && element.category_id === category.id
    )

    if (dateMatch && categoryMatch) {
      filterArray.push(element)
    }
  })

  return filterArray
})

const convertDate = (isoDate) => {
  const date = new Date(isoDate)
  const day = String(date.getDate()).padStart(2, '0')
  const month = String(date.getMonth() + 1).padStart(2, '0')
  const year = date.getFullYear()

  return `${day}.${month}.${year}`
}

onMounted(async () => {
  await fetchCategories()
  await fetchTransactions()
  await fetchWallet()
})
</script>

<template>
  <div class="md:my-32 my-8 max-w-screen-xl mx-auto flex flex-col justify-center px-4">
    <h1 class="text-center text-5xl font-bold text-slight-black md:mb-20 mb-8">{{ walletName }}</h1>

    <div class="flex md:flex-row flex-col mb-8">
      <div class="md:w-1/2 w-full mb-8">
        <div class="flex items-center md:justify-start justify-center lg:gap-10 gap-5">
          <div
            class="flex flex-col items-center justify-center bg-white my-2 shadow-xl lg:gap-10 gap-5 rounded-lg p-5"
          >
            <Graph :data="chartData" :options="chartOptions" />
            <p class="text-3xl font-bold text-slight-black">{{ walletBalance }} руб.</p>
          </div>
        </div>
      </div>

      <!-- Транзакции -->
      <div class="md:w-1/2 w-full">
        <div class="flex flex-col items-center gap-5">
          <p class="text-3xl font-bold text-slight-black">Транзакции</p>
          <router-link
            class="inline-block rounded-lg bg-white px-5 py-3 text-sm font-medium transition hover:text-gray-500"
            :to="`/profile/wallet/create-transaction?id=${id}`"
          >
            Создать транзакцию
          </router-link>

          <!-- Фильтр -->
          <div class="flex items-center justify-end text-right gap-4 mx-auto">
            <div class="relative inline-block">
              <!-- Кнопка для открытия выпадающего списка -->
              <button
                @click="dropdownOpen = !dropdownOpen"
                class="inline-block rounded-lg bg-yellow-300 px-5 py-3 mr-4 text-sm font-medium transition hover:bg-yellow-400"
              >
                Категории
              </button>

              <!-- Выпадающий список -->
              <div
                v-show="dropdownOpen"
                class="absolute mt-2 w-56 bg-white border rounded-lg shadow-lg z-10 p-2"
              >
                <div
                  v-for="(category, index) in categories"
                  :key="index"
                  class="flex items-center space-x-2"
                >
                  <input
                    type="checkbox"
                    v-model="category.active"
                    :value="category.name"
                    class="h-4 w-4 text-green-500 border-gray-300 rounded focus:ring-green-500"
                  />
                  <span>{{ category.name }}</span>
                </div>
              </div>
            </div>

            <input
              class="inline-block rounded-lg px-5 py-3 text-sm font-medium transition hover:bg-white/100"
              type="text"
              v-model="dates"
              placeholder="Дата"
            />
          </div>
        </div>

        <div class="rounded-lg max-h-96 w-full pl-4 overflow-y-auto flex flex-col mb-2 scrollbar">
          <div
            class="flex flex-col w-full min-h-20 h-full rounded-xl justify-between items-center my-1"
          >
            <Transaction
              v-for="transaction in filter"
              :key="transaction.id"
              class="my-2"
              :name="transaction.name"
              :amount="transaction.amount"
              :currency="transaction.currency"
              :date="transaction.date"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
