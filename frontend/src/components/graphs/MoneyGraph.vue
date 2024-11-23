<script setup>
import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement } from 'chart.js'
import { Pie } from 'vue-chartjs'

ChartJS.register(Title, Tooltip, Legend, ArcElement)

defineProps({
  data: Object,
  options: Object,
})
</script>

<template>
  <div>
    <Pie :data="data" :options="options" />
  </div>
</template>
