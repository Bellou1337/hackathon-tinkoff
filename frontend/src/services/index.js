import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'http://git-ts2.ru:8000',
  headers: {
    'Content-Type': 'application/json',
  },
})

export default apiClient
