/** @type {import('tailwindcss').Config} */
export default {
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
  plugins: [],
}
