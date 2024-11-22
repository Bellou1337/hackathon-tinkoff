<script>
import { ref, computed, watch } from 'vue'

export default {
  setup() {
    const firstPassword = ref('')
    const secondPassword = ref('')
    const isPasswordVisible = ref(false)
    const errorMessage = ref('')

    const togglePasswordVisibility = () => {
      isPasswordVisible.value = !isPasswordVisible.value
    }

    const shouldShowPasswordToggle = computed(() => {
      return firstPassword.value.length > 0
    })

    const handleSubmit = (event) => {
      event.preventDefault()

      if (firstPassword.value !== secondPassword.value) {
        errorMessage.value = 'Пароли не совпадают'
      } else {
        errorMessage.value = ''
      }
    }

    watch([firstPassword, secondPassword], (newValues) => {
      const [newFirstPassword, newSecondPassword] = newValues
      if (newFirstPassword.length === 0 || newSecondPassword.length === 0) {
        errorMessage.value = ''
      }
    })

    return {
      firstPassword,
      secondPassword,
      isPasswordVisible,
      togglePasswordVisibility,
      shouldShowPasswordToggle,
      errorMessage,
      handleSubmit,
    }
  },
}
</script>

<template>
  <section class="relative flex flex-wrap lg:h-screen lg:items-center">
    <div
      class="max-w-screen-sm mx-auto w-full bg-white rounded-2xl px-4 py-12 sm:px-6 sm:py-16 lg:px-8 lg:py-24"
    >
      <div class="mx-auto max-w-xl text-center">
        <h1 class="text-auth-g text-2xl font-bold sm:text-3xl">Регистрация</h1>
      </div>

      <form @submit="handleSubmit" class="mx-auto mb-0 mt-8 max-w-md space-y-4">
        <!-- Ввод имени пользователя -->
        <div>
          <div class="relative">
            <input
              type="username"
              class="w-full rounded-lg border-gray-200 bg-gray-100 p-4 pe-12 text-sm shadow-sm transition hover:bg-gray-200"
              placeholder="Введите имя пользователя"
              required
            />
          </div>
        </div>

        <!-- Ввод почты -->
        <div>
          <div class="relative">
            <input
              type="email"
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
              v-model="firstPassword"
              :type="isPasswordVisible ? 'text' : 'password'"
              :class="{ 'bg-red-100 border-red-200 hover:bg-red-200': errorMessage }"
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

        <!-- Подтверждения пароля -->
        <div>
          <div class="relative">
            <input
              v-model="secondPassword"
              type="password"
              :class="{ 'bg-red-100 border-red-200 hover:bg-red-200': errorMessage }"
              class="w-full rounded-lg border-gray-200 bg-gray-100 p-4 pe-12 text-sm shadow-sm transition hover:bg-gray-200"
              placeholder="Подтвердите пароль"
              required
            />
          </div>
        </div>

        <!-- Сообщение об ошибке -->
        <p v-show="errorMessage" class="text-red-500 text-sm">
          {{ errorMessage }}
        </p>

        <!-- Кнопка отправки формы и ссылки -->
        <div class="flex items-center justify-between">
          <p class="text-sm text-gray-500">
            Есть аккаунт?
            <router-link class="underline" to="/auth/login">Вход</router-link>
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
