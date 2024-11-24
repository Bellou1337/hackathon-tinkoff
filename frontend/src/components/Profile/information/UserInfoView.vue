<script>
import { ref, onMounted, watch } from 'vue'
import apiClient from '@/services'
import { getCookie } from '@/utils/cookies'
export default {
  setup() {
    const name = ref('user')
    const email = ref('user@example.com')
    const isLoading = ref(true)
    const error = ref(null)

    const fetchUserInfo = async () => {
      try {
        const token = await getCookie('auth_token')

        if (!token) {
          throw new Error('Token not found')
        }

        const response = await apiClient.get('/auth/users/me', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        })

        if (response.status === 200) {
          name.value = response.data.username
          email.value = response.data.email
          isLoading.value = false
        }
      } catch (err) {
        error.value = err.message
        isLoading.value = false
      }
    }

    onMounted(() => {
      fetchUserInfo()
    })

    return {
      name,
      email,
      isLoading,
      error,
    }
  },
}
</script>

<template>
  <div class="my-16 md:gap-8 gap-4 px-8">
    <div class="w-full bg-gray-200 shadow-lg h-full rounded flex flex-col items-center">
      <div class="text-slight-black px-4 py-8 text-center flex flex-col gap-3">
        <h1 class="text-2xl sm:text-4xl p-4 font-extrabold">Ваш профиль</h1>

        <div>
          <h1 class="text-slight-black text-lg sm:text-xl p-4 text-center">
            <b>{{ name }}</b> - имя пользователя
          </h1>

          <h1 class="text-slight-black text-lg sm:text-xl p-4 text-center">
            <b>{{ email }}</b> - почта
          </h1>
        </div>
      </div>

      <img src="/man.png" alt="home" class="md:w-80 md:h-80 sm:w-48 sm:h-48 object-cover" />
    </div>
  </div>
</template>
