<script setup>
import {ref} from 'vue'


const dropdownOpen = ref(false)

const categories = ref([
  {
    flag: true,
    value: 'wwwww',
  },
])
</script>

<template>
    <div class=" bg-slight-gray min-h-[calc(100vh-80px)] p-5 flex items-center justify-center">
        <div class="bg-white shadow rounded p-16">
            <p class="text-3xl font-bold text-slight-black text-center mb-10">Изменение транзакции</p>
            <div class="flex sm:flex-row flex-col gap-10">
                <div class="flex flex-col ">
                    <div class="my-10">
                        <p class="text-lg mb-5">Категория</p>
                        <button
                            @click="dropdownOpen = !dropdownOpen"
                            class="inline-block rounded-lg w-full bg-yellow-300 px-5 py-3 text-sm font-medium transition hover:bg-yellow-400"
                        >
                            Выберите категории
                        </button>
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
                    <div>
                        <p class="text-lg mb-5">Откуда/Куда</p>
                        <input class="w-full rounded-lg border-gray-200 bg-gray-100 p-4 pe-12 text-sm shadow-sm transition hover:bg-gray-200" type="text">
                    </div>
                    <div>
                        <p class="text-lg mb-5">Сумма</p>
                        <input class="w-full rounded-lg border-gray-200 bg-gray-100 p-4 pe-12 text-sm shadow-sm transition hover:bg-gray-200" type="text">
                    </div>
                </div>
                <div class="bg-gray-200 p-5 my-10 h-32 rounded shadow ">
                    <p class="text-lg mb-5">Дата и время</p>
                    <input class="rounded text-center" type="date"></input>
                </div>
            </div>
 
        </div>
    </div>
</template>