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


const arr = ref([
  //временный вариант если что
  {
    to:"Шлюхи",
    spend:"-300",
    ban:"руб.",
    date:"1.10.2010"
  },
  {
    to:"Шлюхи",
    spend:"+400",
    ban:"руб.",
    date:"2.10.2010"
  },
  {
    to:"Шлюхи",
    spend:"-500",
    ban:"руб.",
    date:"3.10.2010"
  },
  {
    to:"Шлюхи",
    spend:"-500",
    ban:"руб.",
    date:"4.10.2010"
  },
  {
    to:"Шлюхи",
    spend:"-500",
    ban:"руб.",
    date:"5.10.2010"
  },
  {
    to:"Шлюхи",
    spend:"-500",
    ban:"руб.",
    date:"6.10.2010"
  },
  {
    to:"Шлюхи",
    spend:"-500",
    ban:"руб.",
    date:"7.10.2010"
  },
  {
    to:"Шлюхи",
    spend:"-500",
    ban:"руб.",
    date:"8.10.2010"
  },
  {
    to:"Шлюхи",
    spend:"-500",
    ban:"руб.",
    date:"9.10.2010"
  },
  {
    to:"Шлюхи",
    spend:"-300",
    ban:"руб.",
    date:"10.10.2010"
  },
  {
    to:"Шлюхи",
    spend:"+400",
    ban:"руб.",
    date:"11.10.2010"
  },
])
const date = ref('12.05.2005');
//Изменяется при прокрутке.

</script>

<template>
  <div class="dark:bg-gradient-to-r px-2 dark:from-neutral-800 dark:to-neutral-600  bg-slight-gray flex flex-col md:flex-row min-h-screen justify-center items-center md:items-start gap-10 pb-5">
    <div class=" flex flex-col gap-5 items-center  md:w-1/2 w-full mt-5">
       
      <div class="border-b-2 pb-5 border-black dark:border-white">
          <!-- Передаем данные и настройки через props -->
          <digr class=" dark:bg-neutral-100 dark:rounded-lg" :data="chartData" :options="chartOptions" />
        
        </div>
        
        <p class="text-5xl bg-gradient-to-tr from-slate-400 to-slate-100 rounded-lg h-52 flex items-center bg-slate-300">Имя кошелька</p>
        
        <p class="text-3xl border-b-2 border-black dark:border-white dark:text-white pb-5">Баланс руб.</p>
    </div>
<!--В идеале окно прокрутки трогать по минимуму. Эту залупу хуй настроишь нормально-->
<div class="mt-20 rounded-lg max-h-[30rem] md:w-1/2 w-full pl-4 overflow-y-auto flex flex-col mb-2 scrollbar">
  <div class="flex flex-col w-full min-h-20 h-full rounded-xl justify-between items-center my-1">
    <tranz v-for="tranzaction in arr" 
      key="index"
      class="my-2"
      :to="tranzaction.to"
      :spend = "tranzaction.spend"
      :banknote = "tranzaction.ban"
      :date="tranzaction.date"
      ></tranz>
    </div>
    </div>
</div>
</template>

<style>
</style>