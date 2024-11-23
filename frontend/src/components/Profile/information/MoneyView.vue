<template>
    <div class="">
      <!--Либо график либо те карточки оставляем-->
        <div class=" flex items-center justify-center bg-white my-2 shadow-xl lg:gap-10 gap-5 dark:bg-neutral-200 rounded-lg p-5">
          <!-- Передаем данные и настройки через props -->
          <digr :data="chartData" :options="chartOptions" />
        </div>
      <!-- Costs -->
       <!--
      <div class="w-full">
        <a class=" bg-yellow-300 hover:bg-yellow-400  min-h-32 w-full flex items-center justify-center  rounded-xl shadow-xl">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="h-16 w-16 lg:h-40 lg:w-40 rounded-lg">
            <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 6 9 12.75l4.286-4.286a11.948 11.948 0 0 1 4.306 6.43l.776 2.898m0 0 3.182-5.511m-3.182 5.51-5.511-3.181" />
          </svg>
          <div class="mx-5">
            <p class="text-center text-xl text-gray-600"> Расходы</p>
            <p class="text-3xl lg:text-7xl">{{ costs }} {{ bancnot }}</p>
          </div>
        </a>
      </div>
-->
      <!-- Income -->
       <!--
      <div class="w-full">
        <a class="  bg-gray-300 hover:bg-yellow-300 active:bg-yellow-400 min-h-32 w-full flex items-center justify-center rounded-xl shadow-xl">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="h-16 w-16 lg:h-40 lg:w-40 rounded-lg">
            <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 18 9 11.25l4.306 4.306a11.95 11.95 0 0 1 5.814-5.518l2.74-1.22m0 0-5.94-2.281m5.94 2.28-2.28 5.941" />
          </svg>
          <div class="mx-5">
            <p class="text-center text-xl text-gray-600"> Доходы</p>
            <p class="text-3xl lg:text-7xl">{{ incomes }} {{ bancnot }}</p>
          </div>
        </a>
      </div>
        -->
      
    </div>
  </template>
  
  <script setup>
  import digr from '@/components/Diagramm/IncomeExpenseChart.vue'
  import { ref } from 'vue'
  
  const costs = ref('1500')
  const incomes = ref('2000')
  const bancnot = ref('руб.')

  // Данные для диаграммы
const chartData = {
  labels: ['Доходы', 'Расходы'],
  datasets: [
    {
      label: 'Доходы-Расходы',
      data: [7000, 3000], //изменяемое значение (брать из бека)
      backgroundColor: ['#FFE041', '##292929'],
      hoverBackgroundColor: ['#ffe45c', '#171717']
    }
  ]
}

// Настройки диаграммы
const chartOptions = {
  responsive: true,
  plugins: {
    legend: {
      display: true,
      position: 'top'
    },
    title: {
      display: true,
      text: 'Доходы и Расходы'
    }
  }
}

  </script>
  