<script>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { getCookie } from '@/utils/cookies'
import apiClient from '@/services'

export default {
  setup() {
    const name = ref('')

    const router = useRouter()

    const handleSubmit = async (event) => {
      event.preventDefault()

      try {
        const token = await getCookie('auth_token')

        if (!token) {
          throw new Error('Token not found')
        }

        const response = await apiClient.post(
          '/wallet/add',
          {
            name: name.value,
          },
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        )

        if (response.status === 200) {
          console.log(response.data)
          router.push('/profile')
        }
      } catch (err) {
        console.log(err)
      }
    }

    return {
      name,
      handleSubmit,
    }
  },
}
</script>

<template>
  <section class="relative flex items-center justify-center min-h-screen px-4">
    <div
      class="max-w-screen-sm mx-auto w-full bg-white rounded-2xl px-4 py-12 sm:px-6 sm:py-16 lg:px-8 lg:py-24"
    >
      <div class="mx-auto max-w-xl text-center">
        <h1 class="text-auth-g text-2xl font-bold sm:text-3xl">Создание кошелька</h1>
      </div>

      <form @submit="handleSubmit" class="mx-auto mb-0 mt-8 max-w-md space-y-4">
        <!-- Ввод почты -->
        <div>
          <div class="relative">
            <input
              v-model="name"
              type="text"
              class="w-full rounded-lg border-gray-200 bg-gray-100 p-4 pe-12 text-sm shadow-sm transition hover:bg-gray-200"
              placeholder="Введите название кошелька"
              required
            />
          </div>
        </div>

        <!-- Сообщение об ошибке/успехе -->
        <!-- <p
          v-if="messageType !== MessageTypeEnum.NONE"
          :class="{
            'text-green-500': messageType === MessageTypeEnum.LOGIN_SUCCESS,
            'text-red-500': messageType === MessageTypeEnum.LOGIN_FAILED,
          }"
          class="text-sm"
        >
          {{ message }}
        </p> -->

        <!-- Кнопка отправки формы и ссылки -->
        <div class="flex items-center justify-center">
          <button
            type="submit"
            class="inline-block rounded-lg bg-yellow-300 px-5 py-3 mt-4 text-sm font-medium transition items:bg-yellow-400"
          >
            Создать кошелёк
          </button>
        </div>
      </form>
    </div>
  </section>
</template>
