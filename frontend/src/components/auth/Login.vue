<script>
import { ref, computed } from 'vue'

export default {
  setup() {
    const password = ref('')
    const isPasswordVisible = ref(false)

    const togglePasswordVisibility = () => {
      isPasswordVisible.value = !isPasswordVisible.value
    }

    const shouldShowPasswordToggle = computed(() => {
      password.value.length > 0
    })

    return {
      password,
      isPasswordVisible,
      togglePasswordVisibility,
      shouldShowPasswordToggle,
    }
  },
}
</script>

<template>
  <section class="relative flex flex-wrap lg:h-screen lg:items-center">
    <div class="w-full px-4 py-12 sm:px-6 sm:py-16 lg:px-8 lg:py-24">
      <div class="mx-auto max-w-xl text-center">
        <h1 class="text-2xl font-bold sm:text-3xl">Начните смотреть погоду сегодня!</h1>

        <p class="mt-4 text-gray-500">
          Войдите в аккаунт, чтобы получить доступ к погоде в любом месте и в любое время.
        </p>
      </div>

      <form action="#" class="mx-auto mb-0 mt-8 max-w-md space-y-4">
        <div>
          <div class="relative">
            <input
              type="email"
              class="w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm transition hover:bg-gray-100"
              placeholder="Введите почту"
            />
          </div>
        </div>

        <div>
          <div class="relative">
            <input
              v-model="password"
              :type="isPasswordVisible ? 'text' : 'password'"
              class="w-full rounded-lg border-gray-200 p-4 pe-12 text-sm shadow-sm transition hover:bg-gray-100"
              placeholder="Введите пароль"
            />

            <span class="absolute inset-y-0 end-0 grid place-content-center px-4">
              <svg
                v-show="shouldShowPasswordToggle"
                @click="togglePasswordVisibility"
                xmlns="http://www.w3.org/2000/svg"
                :class="{ 'text-gray-700 hover:text-gray-800': isPasswordVisible }"
                class="size-4 text-gray-400 transition hover:text-gray-500"
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

        <div class="flex items-center justify-between">
          <p class="text-sm text-gray-500">
            Нет аккаунта?
            <router-link class="underline" to="/auth/register">Регистрация</router-link>
          </p>

          <button
            type="submit"
            class="inline-block rounded-lg bg-blue-600 px-5 py-3 text-sm font-medium text-white transition hover:bg-blue-700"
          >
            Вход
          </button>
        </div>
      </form>
    </div>
  </section>
</template>
