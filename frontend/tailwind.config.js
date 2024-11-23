/** @type {import('tailwindcss').Config} */
const plugin = require('tailwind-scrollbar')

export default {
  darkMode: 'class',
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Geologica', 'sans-serif'],
      },
      colors: {
        'slight-gray': '#f6f7f8',
        'slight-yellow': '#fff4bc',
        'slight-black': '#313232',
        'auth-gray': '#757373',
      },
    },
  },
  plugins: [require('tailwind-scrollbar'), require('tailwind-scrollbar-hide')],
}
