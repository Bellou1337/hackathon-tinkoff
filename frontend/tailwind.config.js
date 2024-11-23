/** @type {import('tailwindcss').Config} */
const plugin = require('tailwind-scrollbar');

export default {
  darkMode: 'media',
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Geologica', 'sans-serif'],
      },
      colors: {
        'slight-gray': '#f6f7f8',
        'auth-gray': '#757373',
      },
    },
  },
  plugins: [
    require('tailwind-scrollbar'), // Подключение плагина
    require('tailwind-scrollbar-hide') // (Опционально) Для скрытия скроллбаров
  ],
}
