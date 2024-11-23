<script>
import { ref, onMounted } from 'vue'
import apiClient from '@/services'
import { getCookie } from '@/utils/cookies'

export default {
  setup() {
    const name = ref('Username')
    const email = ref('asdasd@mail.ru')

    const verifyToken = async () => {
      const token = await getCookie('auth_token')

      if (!token) {
        // TODO: перенаправление на 404
        return
      }

      try {
        const response = await apiClient.get('/auth/users/me')
        console.log(response.data)
      } catch (error) {
        console.error('Ошибка получения данных пользователя:', error)
      }
    }

    onMounted(() => {
      verifyToken()
    })

    return {
      name,
      email,
    }
  },
}
</script>
