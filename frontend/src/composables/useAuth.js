// useAuth.js
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { getCookie, setCookie, removeCookie } from '@/utils/cookies'

export function useAuth() {
  const loggedIn = ref(false)
  const isLoading = ref(true)
  const router = useRouter()

  const checkLoginStatus = async () => {
    try {
      const token = await getCookie('auth_token')
      loggedIn.value = !!token
    } catch (error) {
      console.error('Error fetching token:', error)
      loggedIn.value = false
    } finally {
      isLoading.value = false
    }
  }

  const login = async (token) => {
    try {
      await setCookie('auth_token', token, { path: '/' })
      loggedIn.value = true
    } catch (error) {
      console.error('Ошибка при установке токена:', error)
    }
  }

  const logout = async () => {
    try {
      await removeCookie('auth_token', { path: '/' })
      loggedIn.value = false
      await router.push('/')
    } catch (error) {
      console.error('Ошибка при выходе:', error)
    }
  }

  const initAuth = () => {
    checkLoginStatus()

    const pollingInterval = setInterval(() => {
      checkLoginStatus()
    }, 2000)

    onUnmounted(() => {
      clearInterval(pollingInterval)
    })
  }

  onMounted(() => {
    initAuth()
  })

  return {
    loggedIn,
    isLoading,
    checkLoginStatus,
    login,
    logout,
  }
}
