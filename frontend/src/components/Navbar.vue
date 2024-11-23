<script>
import { ref } from 'vue'

export default {
  setup() {
    const isDropdownOpen = ref(false)

    const toggleDropdown = () => {
      isDropdownOpen.value = !isDropdownOpen.value
    }

    return {
      isDropdownOpen,
      toggleDropdown,
    }
  },
}
</script>

<template>
  <header class=" bg-white sticky top-0" >
    <div class="mx-auto flex h-20 max-w-screen-xl items-center gap-6 px-4 sm:px-6 lg:px-8">
      <div class="flex items-center gap-4 text-blue-600">
        <svg width="130" height="38" viewBox="0 0 130 38" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M0 2H36V23.5L33.5 29L18 38L3.5 29L0 23.5V2Z" fill="#FFE041"/>
<path d="M8.098 27L15.42 7.4H20.81L28.202 27H22.966L21.58 23.024H14.552L13.194 27H8.098ZM15.602 19.146H20.502L18.038 12.37L15.602 19.146Z" fill="black"/>
<path d="M44.932 27.42C43.5787 27.42 42.2533 27.2287 40.956 26.846C39.668 26.454 38.5807 25.894 37.694 25.166L39.234 22.772C39.7007 23.1733 40.242 23.5187 40.858 23.808C41.4833 24.0973 42.146 24.3213 42.846 24.48C43.546 24.6293 44.246 24.704 44.946 24.704C46.2247 24.704 47.256 24.4613 48.04 23.976C48.8333 23.4907 49.23 22.7813 49.23 21.848C49.23 21.148 48.9593 20.5553 48.418 20.07C47.886 19.5847 46.8967 19.1367 45.45 18.726L43.434 18.138C41.586 17.606 40.2373 16.9013 39.388 16.024C38.548 15.1467 38.128 14.0547 38.128 12.748C38.128 11.88 38.3007 11.096 38.646 10.396C39.0007 9.696 39.4953 9.08933 40.13 8.576C40.774 8.06267 41.53 7.67067 42.398 7.4C43.266 7.12933 44.218 6.994 45.254 6.994C46.57 6.994 47.7927 7.18533 48.922 7.568C50.0513 7.95067 50.9847 8.464 51.722 9.108L50.126 11.432C49.7247 11.068 49.2533 10.7553 48.712 10.494C48.18 10.2327 47.606 10.032 46.99 9.892C46.374 9.752 45.7487 9.682 45.114 9.682C44.33 9.682 43.6347 9.79867 43.028 10.032C42.4307 10.256 41.964 10.5827 41.628 11.012C41.292 11.4413 41.124 11.964 41.124 12.58C41.124 13.028 41.236 13.42 41.46 13.756C41.684 14.092 42.0667 14.4 42.608 14.68C43.1587 14.9507 43.9147 15.226 44.876 15.506L47.004 16.136C48.8147 16.668 50.14 17.3633 50.98 18.222C51.82 19.0713 52.24 20.1773 52.24 21.54C52.24 22.7067 51.9507 23.7333 51.372 24.62C50.8027 25.4973 49.972 26.1833 48.88 26.678C47.788 27.1727 46.472 27.42 44.932 27.42ZM56.13 27V7.4H62.262C64.2127 7.4 65.9347 7.82 67.428 8.66C68.9214 9.49067 70.088 10.6433 70.928 12.118C71.7774 13.5927 72.202 15.2913 72.202 17.214C72.202 18.642 71.9594 19.958 71.474 21.162C70.998 22.3567 70.3167 23.388 69.43 24.256C68.5434 25.124 67.4934 25.8007 66.28 26.286C65.0667 26.762 63.7274 27 62.262 27H56.13ZM59.266 24.074H61.884C62.9387 24.074 63.8954 23.92 64.754 23.612C65.622 23.2947 66.364 22.8373 66.98 22.24C67.6054 21.6427 68.086 20.924 68.422 20.084C68.758 19.2347 68.926 18.278 68.926 17.214C68.926 15.786 68.632 14.5587 68.044 13.532C67.4654 12.496 66.6487 11.7027 65.594 11.152C64.5394 10.592 63.3027 10.312 61.884 10.312H59.266V24.074ZM73.2901 27L80.9061 7.4H84.3081L92.1201 27H88.5781L86.7721 22.324H78.4701L76.7341 27H73.2901ZM79.2821 19.622H85.9321L82.5441 11.082L79.2821 19.622ZM101.342 27.42C99.9888 27.42 98.6635 27.2287 97.3662 26.846C96.0782 26.454 94.9908 25.894 94.1042 25.166L95.6442 22.772C96.1108 23.1733 96.6522 23.5187 97.2682 23.808C97.8935 24.0973 98.5562 24.3213 99.2562 24.48C99.9562 24.6293 100.656 24.704 101.356 24.704C102.635 24.704 103.666 24.4613 104.45 23.976C105.243 23.4907 105.64 22.7813 105.64 21.848C105.64 21.148 105.369 20.5553 104.828 20.07C104.296 19.5847 103.307 19.1367 101.86 18.726L99.8442 18.138C97.9962 17.606 96.6475 16.9013 95.7982 16.024C94.9582 15.1467 94.5382 14.0547 94.5382 12.748C94.5382 11.88 94.7108 11.096 95.0562 10.396C95.4108 9.696 95.9055 9.08933 96.5402 8.576C97.1842 8.06267 97.9402 7.67067 98.8082 7.4C99.6762 7.12933 100.628 6.994 101.664 6.994C102.98 6.994 104.203 7.18533 105.332 7.568C106.461 7.95067 107.395 8.464 108.132 9.108L106.536 11.432C106.135 11.068 105.663 10.7553 105.122 10.494C104.59 10.2327 104.016 10.032 103.4 9.892C102.784 9.752 102.159 9.682 101.524 9.682C100.74 9.682 100.045 9.79867 99.4382 10.032C98.8408 10.256 98.3742 10.5827 98.0382 11.012C97.7022 11.4413 97.5342 11.964 97.5342 12.58C97.5342 13.028 97.6462 13.42 97.8702 13.756C98.0942 14.092 98.4768 14.4 99.0182 14.68C99.5688 14.9507 100.325 15.226 101.286 15.506L103.414 16.136C105.225 16.668 106.55 17.3633 107.39 18.222C108.23 19.0713 108.65 20.1773 108.65 21.54C108.65 22.7067 108.361 23.7333 107.782 24.62C107.213 25.4973 106.382 26.1833 105.29 26.678C104.198 27.1727 102.882 27.42 101.342 27.42ZM112.54 27V7.4H118.672C120.623 7.4 122.345 7.82 123.838 8.66C125.332 9.49067 126.498 10.6433 127.338 12.118C128.188 13.5927 128.612 15.2913 128.612 17.214C128.612 18.642 128.37 19.958 127.884 21.162C127.408 22.3567 126.727 23.388 125.84 24.256C124.954 25.124 123.904 25.8007 122.69 26.286C121.477 26.762 120.138 27 118.672 27H112.54ZM115.676 24.074H118.294C119.349 24.074 120.306 23.92 121.164 23.612C122.032 23.2947 122.774 22.8373 123.39 22.24C124.016 21.6427 124.496 20.924 124.832 20.084C125.168 19.2347 125.336 18.278 125.336 17.214C125.336 15.786 125.042 14.5587 124.454 13.532C123.876 12.496 123.059 11.7027 122.004 11.152C120.95 10.592 119.713 10.312 118.294 10.312H115.676V24.074Z" fill="black"/>
</svg>
      </div>

      <div class="flex flex-1 items-center justify-end">
        <div class="flex items-center gap-4">
          <div class="hidden sm:flex sm:gap-4">
            <router-link
              class="block text-xl px-2 py-2.5  font-medium border-b-2 border-gray-50/100  transition hover:/75
              hover:text-[#FFE041] hover:border-b-2 hover:border-[#FFE041]"
              to="/profile"
            >
              Профиль
            </router-link>
            <router-link
              class="block text-xl px-2 py-2.5  font-medium border-b-2 border-gray-50/100  transition hover:/75
              hover:text-[#FFE041] hover:border-b-2 hover:border-[#FFE041]"
              to="/"
            >
              Домашняя страница
            </router-link>

            <router-link
              class="block text-xl px-2 py-2.5  font-medium border-b-2 border-gray-50/100  transition hover:/75
              hover:text-[#FFE041] hover:border-b-2 hover:border-[#FFE041]"
              to="/auth/login"
            >
              Войти
            </router-link>

            <router-link
              class="block text-xl px-2 py-2.5  font-medium border-b-2 border-gray-50/100  transition hover:/75
              hover:text-[#FFE041] hover:border-b-2 hover:border-[#FFE041]"
              to="/auth/register"
            >
              Создать аккаунт
            </router-link>
          </div>

          <div class="relative sm:hidden">
            <button
              @click="toggleDropdown"
              class="block rounded bg-gray-100 p-2.5 text-gray-600 transition hover:text-gray-600/75"
            >
              <svg
                :class="{ 'rotate-90': isDropdownOpen }"
                xmlns="http://www.w3.org/2000/svg"
                class="size-5 transition-transform duration-200 ease-in-out transform"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
                stroke-width="2"
              >
                <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16" />
              </svg>
            </button>

            <transition
              enter-active-class="transition-all duration-50 ease-out"
              leave-active-class="transition-all duration-50 ease-in"
              enter-class="opacity-0 scale-90"
              enter-to-class="opacity-100 scale-100"
              leave-class="opacity-100 scale-100"
              leave-to-class="opacity-0 scale-90"
            >
              <div
                v-show="isDropdownOpen"
                class="absolute end-0 z-10 mt-2 w-56 divide-y divide-gray-100 rounded-md border border-gray-100 bg-white shadow-lg"
                role="menu"
              >
                <div class="p-2">
                  <router-link
                    to="/auth/login"
                    class="block rounded-lg px-4 py-2 text-sm text-gray-500 hover:bg-gray-50 hover:text-gray-700"
                    role="menuitem"
                  >
                    Войти
                  </router-link>

                  <router-link
                    to="/auth/register"
                    class="block rounded-lg px-4 py-2 text-sm text-gray-500 hover:bg-gray-50 hover:text-gray-700"
                    role="menuitem"
                  >
                    Создать аккаунт
                  </router-link>
                </div>
              </div>
            </transition>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>
