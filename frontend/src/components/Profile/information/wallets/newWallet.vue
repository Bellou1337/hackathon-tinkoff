<script setup>
import {ref} from 'vue'

const nameOfNew = ref('');

</script>

<template>
 <div class=" bg-slight-gray dark:bg-neutral-800 flex items-center justify-center h-screen">
    <div class=" flex items-center justify-center w-auto bg-white dark:bg-neutral-600 flex-col rounded-lg py-24 px-20">
        <p class="text-3xl font-bold p-5 border-b-2 mb-8">Создание нового кошелька</p>
        <input placeholder="Введите название" class="w-full rounded-lg border-gray-200 bg-gray-100 p-4 pe-12 text-sm shadow-sm transition hover:bg-gray-200" type="text" v-model="nameOfNew" maxlength="10">
        <button class="block outline-none bg-yellow-300 my-4 p-2 rounded-xl hover:bg-yellow-400 active:bg-yellow-500"> Создать </button>
    </div>
 </div>
</template>
