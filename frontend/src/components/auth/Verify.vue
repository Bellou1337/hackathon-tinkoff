<script>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import apiClient from '@/services'

export default {
  setup() {
    const loading = ref(true)
    const errorMessage = ref(null)
    const successMessage = ref(null)

    const route = useRoute()

    const verifyToken = async () => {
      const token = route.query.token

      if (!token) {
        errorMessage.value = 'Токен отсутствует в URL.'
        loading.value = false
        return
      }

      try {
        const response = await apiClient.post('/auth/verify', {
          token: token,
          withCredentials: true,
        })

        await console.log(response)

        if (response.status === 200) {
          successMessage.value = 'Токен успешно проверен!'
          console.log('Токен установлен сервером')
        } else {
          errorMessage.value = response.data.message || 'Ошибка проверки токена.'
        }
      } catch (error) {
        console.error('Ошибка проверки токена:', error.response)
        if (error.response) {
          errorMessage.value = `Ошибка сервера: ${error.response.data.detail}`
        } else {
          errorMessage.value = 'Не удалось подключиться к серверу.'
        }
      } finally {
        loading.value = false
      }
    }

    onMounted(() => {
      verifyToken()
    })

    return {
      loading,
      errorMessage,
      successMessage,
    }
  },
}
</script>

<template>
  <section class="relative flex flex-col items-center justify-center min-h-screen px-4">
    <div
      class="max-w-screen-sm mx-auto w-full bg-white rounded-2xl px-4 py-12 sm:px-6 sm:py-16 lg:px-8 lg:py-24"
    >
      <div class="mx-auto max-w-xl text-center">
        <h1 class="text-auth-g text-2xl font-bold sm:text-3xl mb-2">Верификация пользователя...</h1>

        <p v-if="loading">Пожалуйста, подождите...</p>
        <p v-if="errorMessage" class="text-red-500 flex flex-col gap-1">
          {{ errorMessage }}
          <router-link class="underline font-bold" to="/auth/register"
            >Вернуться обратно на страницу регистрации</router-link
          >
        </p>
        <p v-if="successMessage" class="text-green-500">
          {{ successMessage }}
          <router-link class="underline font-bold" to="/auth/login">Авторизоваться</router-link>
        </p>
      </div>
    </div>
  </section>
</template>
