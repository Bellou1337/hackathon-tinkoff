<script setup>
import { ref, onMounted, computed } from 'vue'
import Graph from '@/components/graphs/MoneyGraph.vue'
import { getCookie } from '@/utils/cookies'
import apiClient from '@/services'

const incomes = ref(0)
const expenses = ref(0)
const total = ref(0)

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
const wallets = ref([])
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

  incomes.value = 0
  expenses.value = 0
  total.value = 0

  for (const wallet of wallets.value) {
    total.value += wallet.balance

    try {
      const token = await getCookie('auth_token')

      if (!token) {
        throw new Error('Token not found')
      }

      const response = await apiClient.post(
        '/transaction/get_by_wallet_id',
        {
          wallet_id: wallet.id,
        },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      )

      if (response.status === 200) {
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
}

const convertDate = (isoDate) => {
  const date = new Date(isoDate)
  const day = String(date.getDate()).padStart(2, '0')
  const month = String(date.getMonth() + 1).padStart(2, '0')
  const year = date.getFullYear()

  return `${day}.${month}.${year}`
}

onMounted(async () => {
  await fetchCategories()
  await fetchWallets()
})
</script>

<template>
  <div class="flex items-center justify-center lg:gap-10 gap-5">
    <div
      class="flex flex-col items-center justify-center bg-white my-2 shadow-xl lg:gap-10 gap-5 rounded-lg p-5"
    >
      <Graph :data="chartData" :options="chartOptions" />
      <p class="text-3xl font-bold text-slight-black">{{ total }} руб.</p>
    </div>
  </div>
</template>
