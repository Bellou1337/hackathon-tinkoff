<script setup>
import tranz from '@/components/ChoosenWallet/Tranzaction.vue'
import digr from '@/components/Diagramm/IncomeExpenseChart.vue'
import {ref} from 'vue'

// Данные для диаграммы
const chartData = {
  labels: ['Доходы', 'Расходы'],
  datasets: [
    {
      label: 'Доходы-Расходы',
      data: [7000, 3000], //изменяемое значение (брать из бека)
      backgroundColor: ['rgba(75, 192, 192, 0.6)', 'rgba(255, 99, 132, 0.6)'],
      hoverBackgroundColor: ['rgba(75, 192, 192, 0.8)', 'rgba(255, 99, 132, 0.8)']
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


const arr = ref([
  //временный вариант если что
  {
    to:"Шлюхи",
    spend:"-300",
    ban:"руб."
  },
  {
    to:"Шлюхи",
    spend:"+400",
    ban:"руб."
  },
  {
    to:"Шлюхи",
    spend:"-500",
    ban:"руб."
  },
  {
    to:"Шлюхи",
    spend:"-500",
    ban:"руб."
  },
  {
    to:"Шлюхи",
    spend:"-500",
    ban:"руб."
  },
  {
    to:"Шлюхи",
    spend:"-500",
    ban:"руб."
  },
  {
    to:"Шлюхи",
    spend:"-500",
    ban:"руб."
  },
  {
    to:"Шлюхи",
    spend:"-500",
    ban:"руб."
  },
  {
    to:"Шлюхи",
    spend:"-500",
    ban:"руб."
  },
  {
    to:"Шлюхи",
    spend:"-300",
    ban:"руб."
  },
  {
    to:"Шлюхи",
    spend:"+400",
    ban:"руб."
  },
])
const date = ref('12.05.2005');
//Изменяется при прокрутке.

</script>

<template>
  <div class="dark:bg-gradient-to-r dark:from-neutral-800 dark:to-neutral-600 md:bg-gradient-to-r bg-gradient-to-b p-2 from-slate-300 to-slight-gray flex flex-col md:flex-row min-h-screen">
    <div class=" flex flex-col gap-5 items-center justify-center md:w-1/2 w-full">
        <div class="border-b-2 pb-5 border-black dark:border-white">
          <!-- Передаем данные и настройки через props -->
          <digr class=" dark:bg-neutral-100 dark:rounded-lg" :data="chartData" :options="chartOptions" />
        </div>
        <p class="text-5xl bg-gradient-to-tr from-slate-400 to-slate-100 rounded-lg h-52 flex items-center bg-slate-300">Имя кошелька</p>
        <p class="text-3xl border-b-2 border-black dark:border-white dark:text-white pb-5">Баланс руб.</p>
    </div>
<!--В идеале окно прокрутки трогать по минимуму. Эту залупу хуй настроишь нормально-->
    <div class=" max-h-screen mt-5 min-h-96 md:w-1/2 w-full md:m-5 overflow-y-auto scrollbar flex flex-col items-center mb-10">
      <div class="sticky top-0 bg-yellow-300/50 dark:bg-yellow-500/90 text-xl text-center rounded-md w-48 z-10 mb-4">{{ date }}</div>
      <div class="w-full flex flex-col items-center">
        <tranz v-for="(tr, index) in arr" :key="index"
               :to="tr.to"
               :spend="tr.spend"
               :bancnote="tr.ban">
        </tranz>
      </div>
    </div>
  </div>
</template>
