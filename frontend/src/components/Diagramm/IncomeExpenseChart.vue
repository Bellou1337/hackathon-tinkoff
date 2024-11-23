<script setup>
import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement } from 'chart.js'
import { Pie } from 'vue-chartjs'

// Регистрация модулей Chart.js
ChartJS.register(Title, Tooltip, Legend, ArcElement)

// Принимаем данные и настройки через `props`
defineProps({
  data: Object, // Данные для диаграммы
  options: Object // Настройки диаграммы
})
</script>

<template>
  <div>
    <!-- Круговая диаграмма -->
    <Pie :data="data" :options="options" />
  </div>
</template>