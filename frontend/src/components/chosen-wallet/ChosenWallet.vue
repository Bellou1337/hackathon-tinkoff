<script setup>
import { ref, computed } from 'vue'

import Transaction from '@/components/chosen-wallet/Transaction.vue'
import Graph from '@/components/graphs/MoneyGraph.vue'

const dropdownOpen = ref(false)
const dates = ref('')

const chartData = {
  labels: ['Доходы', 'Расходы'],
  datasets: [
    {
      label: 'Доходы - Расходы',
      data: [7000, 3000],
      backgroundColor: ['#facc15', '#313232'],
      hoverBackgroundColor: ['#20d457', '#c44242'],
      borderColor: 'transparent',
      borderWidth: 0,
      hoverBorderColor: 'transparent',
      hoverBorderWidth: 0,
    },
  ],
}

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

const transactions = ref([
  {
    label: 'wwwww',
    amount: '-300',
    currency: 'руб.',
    date: '01.10.2010',
  },
  {
    label: 'wwwww',
    amount: '+400',
    currency: 'руб.',
    date: '02.10.2010',
  },
  {
    label: 'wwwww',
    amount: '-500',
    currency: 'руб.',
    date: '03.10.2010',
  },
  {
    label: 'wwwww',
    amount: '-500',
    currency: 'руб.',
    date: '04.10.2010',
  },
  {
    label: 'wwwww',
    amount: '-500',
    currency: 'руб.',
    date: '05.10.2010',
  },
  {
    label: 'wwwww',
    amount: '-500',
    currency: 'руб.',
    date: '06.10.2010',
  },
  {
    label: 'wwwww',
    amount: '-500',
    currency: 'руб.',
    date: '07.10.2010',
  },
  {
    label: 'wwwww',
    amount: '-500',
    currency: 'руб.',
    date: '08.10.2010',
  },
  {
    label: 'wwwww',
    amount: '-500',
    currency: 'руб.',
    date: '09.10.2010',
  },
  {
    label: 'wwwww',
    amount: '-300',
    currency: 'руб.',
    date: '10.10.2010',
  },
  {
    label: 'wwwww',
    amount: '+400',
    currency: 'руб.',
    date: '11.10.2010',
  },
])

const categories = ref([
  {
    flag: true,
    value: 'wwwww',
  },
])

const filter = computed(() => {
  const filterArray = []

  transactions.value.forEach((element) => {
    const dateMatch = element.date.includes(dates.value)
    const categoryMatch = categories.value.some(
      (category) => category.flag && element.label.includes(category.value)
    )

    if (dateMatch && categoryMatch) {
      filterArray.push(element)
    }
  })

  return filterArray
})
</script>

<template>
  <div class="md:my-32 my-8 max-w-screen-xl mx-auto flex flex-col justify-center px-4">
    <h1 class="text-center text-5xl font-bold text-slight-black md:mb-20 mb-8">Имя кошелька</h1>

    <div class="flex md:flex-row flex-col mb-8">
      <div class="md:w-1/2 w-full mb-8">
        <div class="flex items-center md:justify-start justify-center lg:gap-10 gap-5">
          <div
            class="flex flex-col items-center justify-center bg-white my-2 shadow-xl lg:gap-10 gap-5 rounded-lg p-5"
          >
            <Graph :data="chartData" :options="chartOptions" />
            <p class="text-3xl font-bold text-slight-black">Баланс руб.</p>
          </div>
        </div>
      </div>

      <!-- Транзакции -->
      <div class="md:w-1/2 w-full">
        <div class="flex flex-col items-center gap-5">
          <p class="text-3xl font-bold text-slight-black">Транзакции</p>

          <!-- Фильтр -->
          <div class="flex items-center justify-end text-right gap-4 mx-auto">
            <div class="relative inline-block">
              <!-- Кнопка для открытия выпадающего списка -->
              <button
                @click="dropdownOpen = !dropdownOpen"
                class="inline-block rounded-lg bg-yellow-300 px-5 py-3 text-sm font-medium transition hover:bg-yellow-400"
              >
                Выберите категории
              </button>

              <!-- Выпадающий список -->
              <div
                v-show="dropdownOpen"
                class="absolute mt-2 w-48 bg-white border rounded-lg shadow-lg z-10 p-2"
              >
                <label
                  v-for="(category, index) in categories"
                  :key="index"
                  class="flex items-center space-x-2"
                >
                  <input
                    type="checkbox"
                    v-model="category.flag"
                    :value="category.value"
                    class="h-4 w-4 text-green-500 border-gray-300 rounded focus:ring-green-500"
                  />
                  <span>{{ category.value }}</span>
                </label>
              </div>
            </div>

            <!-- class="h-12 rounded-lg p-4 pe-12 text-sm shadow-sm transition hover:bg-white/50" -->

            <input
              class="inline-block rounded-lg px-5 py-3 text-sm font-medium transition hover:bg-white/100"
              type="text"
              v-model="dates"
              placeholder="Введите дату"
            />
          </div>
        </div>

        <div class="rounded-lg max-h-96 w-full pl-4 overflow-y-auto flex flex-col mb-2 scrollbar">
          <div
            class="flex flex-col w-full min-h-20 h-full rounded-xl justify-between items-center my-1"
          >
            <Transaction
              v-for="transaction in filter"
              key="index"
              class="my-2"
              :label="transaction.label"
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

<style></style>
