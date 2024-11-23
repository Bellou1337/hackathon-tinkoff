<script setup>
import {ref} from 'vue'

const nameOfNew = ref('');

</script>

<template>
 <div class=" bg-slight-gray dark:bg-neutral-800 flex items-center justify-center h-screen">
    <div class=" bg-white dark:bg-neutral-600 flex-col shadow-xl rounded-lg p-5">
        <p class="text-6xl border-b-2 mb-8">ASDASD</p>
        <p class="text-xl dark:text-white mb-5">Новый кошелек</p>
        <p class="text-gray-400"> Введите название</p>
        <input class="h-10 text-center focus:outline-none focus:border-yellow-300 border rounded-lg border-gray-500" type="text" v-model="nameOfNew" maxlength="10">
        <button class="block outline-none bg-yellow-300 my-4 p-2 rounded-xl hover:bg-yellow-400 active:bg-yellow-500"> Создать </button>
    </div>
 </div>
</template>
