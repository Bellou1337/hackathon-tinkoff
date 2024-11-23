<script setup>
import Graph from '@/components/graphs/MoneyGraph.vue'

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
</script>

<template>
  <div class="flex items-center justify-center lg:gap-10 gap-5">
    <div
      class="flex items-center justify-center bg-white my-2 shadow-xl lg:gap-10 gap-5 rounded-lg p-5"
    >
      <Graph :data="chartData" :options="chartOptions" />
    </div>
  </div>
</template>
