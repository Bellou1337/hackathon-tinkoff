<template>
  <div class="md:w-5/6 w-full md:mb-10 md:mt-10 bg-white rounded-xl shadow-xl p-5">
    <div class="flex flex-col h-auto text-center gap-2 m-5">
      <p class="text-3xl lg:text-[4rem]">{{ name }}</p>
      <p class="text-xl lg:text-3xl">{{ email }}</p>
      <a class="text-sm lg:text-base underline text-gray-500" href="#"> Хотите сменить пароль?</a>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const name = ref('Username')
const email = ref('asdasd@mail.ru')
</script>
