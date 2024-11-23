<script>
import { ref, computed, watch } from 'vue'
import apiClient from '@/services'
import { getCookie } from '@/utils/cookies'

export default {
  setup() {
    const email = ref('')
    const password = ref('')
    const isPasswordVisible = ref(false)
    const errorMessage = ref('')

    const togglePasswordVisibility = () => {
      isPasswordVisible.value = !isPasswordVisible.value
    }

    const shouldShowPasswordToggle = computed(() => {
      return password.value.length > 0
    })

    const MessageTypeEnum = {
      NONE: 'NONE',
      LOGIN_FAILED: 'LOGIN_FAILED',
      LOGIN_SUCCESS: 'LOGIN_SUCCESS',
    }

    const messageType = ref(MessageTypeEnum.ERROR)
    const message = ref('')

    const handleSubmit = async (event) => {
      event.preventDefault()

      try {
        const token = await getCookie('auth_token')

        if (token) {
          messageType.value = MessageTypeEnum.LOGIN_FAILED
          message.value = response.data.message || 'Пользователь уже авторизован'
          return
        }

        const response = await apiClient.post(
          '/auth/jwt/login',
          new URLSearchParams({
            username: email.value,
            password: password.value,
          }),
          {
            headers: {
              'Content-Type': 'application/x-www-form-urlencoded',
            },
          }
        )

        console.log(response)

        if (response.status === 200) {
          messageType.value = MessageTypeEnum.LOGIN_SUCCESS
          message.value = 'Авторизация прошла успешно!'
          console.log('Авторизация прошла успешно!')

          if (!token) {
            document.cookie = `auth_token=${response.data.token}; path=/;`
            return
          }
        } else {
          messageType.value = MessageTypeEnum.LOGIN_FAILED
          message.value = response.data.message || 'Неверный логин или пароль!'
        }
        console.log('Авторизация успешна:', response.data)

        // setTimeout(() => {
        //   router.push('/')
        // }, 1500)
      } catch (error) {
        messageType.value = MessageTypeEnum.LOGIN_FAILED
        message.value = 'Неверный логин или пароль!'

        if (error.response) {
          console.error('Ошибка авторизации:', error.response.data)
        } else if (error.request) {
          console.error('Нет ответа от сервера:', error.request)
        } else {
          console.error('Ошибка:', error.message)
        }
      }
    }

    watch([password, email], (newValues) => {
      const [newPassword, newEmail] = newValues

      if (newPassword.length === 0 || newEmail.length === 0) {
        messageType.value = MessageTypeEnum.NONE
        message.value = ''
      }
    })

    return {
      email,
      password,
      isPasswordVisible,
      togglePasswordVisibility,
      shouldShowPasswordToggle,
      errorMessage,
      handleSubmit,
      messageType,
      message,
      MessageTypeEnum,
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
        <h1 class="text-auth-g text-2xl font-bold sm:text-3xl">Авторизация</h1>
      </div>

      <form @submit="handleSubmit" class="mx-auto mb-0 mt-8 max-w-md space-y-4">
        <!-- Ввод почты -->
        <div>
          <div class="relative">
            <input
              v-model="email"
              type="email"
              :class="{
                'bg-red-100 border-red-200 hover:bg-red-200':
                  messageType === MessageTypeEnum.LOGIN_FAILED,
              }"
              class="w-full rounded-lg border-gray-200 bg-gray-100 p-4 pe-12 text-sm shadow-sm transition hover:bg-gray-200"
              placeholder="Введите почту"
              required
            />
          </div>
        </div>

        <!-- Ввод пароля -->
        <div>
          <div class="relative">
            <input
              v-model="password"
              :type="isPasswordVisible ? 'text' : 'password'"
              :class="{
                'bg-red-100 border-red-200 hover:bg-red-200':
                  messageType === MessageTypeEnum.LOGIN_FAILED,
              }"
              class="w-full rounded-lg border-gray-200 bg-gray-100 p-4 pe-12 text-sm shadow-sm transition hover:bg-gray-200"
              placeholder="Введите пароль"
              required
            />

            <span class="absolute inset-y-0 end-0 grid place-content-center px-4">
              <svg
                v-show="shouldShowPasswordToggle"
                @click="togglePasswordVisibility"
                xmlns="http://www.w3.org/2000/svg"
                :class="{ 'text-gray-700 hover:text-gray-800': errorMessage }"
                class="size-4 text-gray-400 transition hover:text-gray-500 cursor-pointer"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                />
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
                />
              </svg>
            </span>
          </div>
        </div>

        <!-- Сообщение об ошибке/успехе -->
        <p
          v-if="messageType !== MessageTypeEnum.NONE"
          :class="{
            'text-green-500': messageType === MessageTypeEnum.LOGIN_SUCCESS,
            'text-red-500': messageType === MessageTypeEnum.LOGIN_FAILED,
          }"
          class="text-sm"
        >
          {{ message }}
        </p>

        <!-- Кнопка отправки формы и ссылки -->
        <div class="flex items-center justify-between">
          <p class="text-sm text-gray-500">
            Нет аккаунта?
            <router-link class="underline" to="/auth/register">Регистрация</router-link>
          </p>

          <button
            type="submit"
            class="inline-block rounded-lg bg-yellow-300 px-5 py-3 text-sm font-medium transition hover:bg-yellow-400"
          >
            Войти
          </button>
        </div>
      </form>
    </div>
  </section>
</template>
