<script setup>
import { ref, onMounted } from 'vue'
import { getCookie } from '@/utils/cookies'
import { useRoute, useRouter } from 'vue-router'
import apiClient from '@/services'

const title = ref('')
const amount = ref('')
const date = ref('')

const dropdownOpen = ref(false)

const categories = ref([])

const route = useRoute()
const router = useRouter()
const id = route.query.id
const selectedOption = ref(""); 

const fetchCategories = async () => {
  try {
    const token = await getCookie('auth_token')

    if (!token) {
      throw new Error('Token not found')
    }

    const response = await apiClient.get('/category/get_all', {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })

    if (response.status === 200) {
      // console.log(response.data)

      categories.value = response.data.map((category) => ({
        name: category.name,
        income: category.is_income,
        active: false,//все false изначально
        id: category.id,
      }))
    }
  } catch (err) {
    console.log(err)
  }
}

const createTransaction = async () => {
  try {
    const token = await getCookie('auth_token')

    if (!token) {
      throw new Error('Token not found')
    }

    const response = await apiClient.post(
      '/transaction/add',
      {
        title: title.value,
        category_id: selectedOption.value,//передаем выбранную категорию 
        amount: Math.abs(amount.value),
        wallet_id: id,
        date: date.value,
      },	
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    )

    if (response.status === 200) {
      // console.log(response.data)
      router.push(`/profile/wallet?id=${id}`)
    }
  } catch (err) {
    console.log(err)
  }
}

onMounted(async () => {
  await fetchCategories()
})
//------------Функция для сброса категории----------------
const selectCategory = (categoryId) => {
  selectedOption.value = categoryId;
  categories.value.forEach((category) => {
    if (category.id !== categoryId) {
      category.active = false;  // Сбросить состояние активности других категорий
    }
  });
}

</script>

<template>
  <div class="bg-slight-gray min-h-[calc(100vh-80px)] p-5 flex items-center justify-center">
    <div class="bg-white shadow rounded p-16">
      <p class="text-3xl font-bold text-slight-black text-center mb-8">Новая транзакция</p>
      <div class="flex sm:flex-row flex-col gap-10 mb-4">
        <div class="flex flex-col">
          <div class="mb-8">
            <button
              @click="dropdownOpen = !dropdownOpen"
              class="inline-block rounded-lg w-full bg-yellow-300 px-5 py-3 text-sm font-medium transition hover:bg-yellow-400"
            >
              Выберите категории
            </button>
            <div
              v-show="dropdownOpen"
              class="absolute mt-2 w-56 bg-white border rounded-lg shadow-lg z-10 p-2"
            >
              <label
                v-for="(category, index) in categories"
                :key="index"
                class="flex items-center space-x-2"
              >
                <input
                  type="checkbox"
                  v-model="category.active"
                  :value="category.name"
									:checked="selectedOption === category.id"
									@change="selectCategory(category.id)"
                  class="h-4 w-4 text-green-500 border-gray-300 rounded focus:ring-green-500"
                />
                <span>{{ category.name }}</span>
              </label>
            </div>
          </div>

          <div class="flex flex-col gap-4">
            <div class="relative">
              <input
                v-model="title"
                type="text"
                class="w-full rounded-lg border-gray-200 bg-gray-100 p-4 pe-12 text-sm shadow-sm transition hover:bg-gray-200"
                placeholder="Название транзакции"
								maxlength="20"
                required
              />
            </div>

            <div class="relative">
              <input
                v-model="amount"
                type="number"
                class="w-full rounded-lg border-gray-200 bg-gray-100 p-4 pe-12 text-sm shadow-sm transition hover:bg-gray-200"
                placeholder="Сумма"
                required
              />
            </div>
          </div>
        </div>
        <div class="bg-gray-200 p-5 my-10 h-32 rounded shadow">
          <p class="text-lg font-bold mb-2 text-center">Дата</p>
          <input v-model="date" class="rounded text-center" type="date" />
        </div>
      </div>

      <div class="flex">
        <button
          @click="createTransaction"
          class="inline-block rounded-lg w-full mx- bg-yellow-300 px-5 py-3 text-sm font-medium transition hover:bg-yellow-400"
        >
          Создать
        </button>
      </div>
    </div>
  </div>
</template>
