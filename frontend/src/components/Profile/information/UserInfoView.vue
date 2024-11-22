<template>
  <div class="flex text-center gap-5 justify-left m-5 h-auto">
    <div>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="lg:w-40 lg:h-40 w-20 h-20"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="currentColor"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M17.982 18.725A7.488 7.488 0 0 0 12 15.75a7.488 7.488 0 0 0-5.982 2.975m11.963 0a9 9 0 1 0-11.963 0m11.963 0A8.966 8.966 0 0 1 12 21a8.966 8.966 0 0 1-5.982-2.275M15 9.75a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z"
        />
      </svg>
    </div>
    <div>
      <p class="text-center text-3xl lg:text-[4rem] ">{{ name }}</p>
      <p class="text-center text-xl lg:text-3xl">{{ email }}</p>
      <a class="text-center text-sm lg:text-base underline text-gray-500" href="#"> Хотите сменить пароль?</a>
    </div>
  </div>
</template>

<script setup>
import {ref} from 'vue'

const name = ref('Username');
const email = ref('asdasd@mail.ru');

</script>
