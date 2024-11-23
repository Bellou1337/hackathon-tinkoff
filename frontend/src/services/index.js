import axios from 'axios'
import { getCookie } from '@/utils/cookies'

const apiClient = axios.create({
  baseURL: 'http://git-ts2.ru:8000',
  headers: {
    'Content-Type': 'application/json',
  },
})

apiClient.interceptors.request.use(
  (config) => {
    const token = getCookie('auth_token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

export default apiClient
