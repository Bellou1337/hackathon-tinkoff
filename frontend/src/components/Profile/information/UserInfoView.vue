<template>
  <div class="flex flex-col text-center items-center gap-2 justify-center m-5">
      <p class="text-3xl lg:text-[4rem] ">{{ name }}</p>
      <p class="text-xl lg:text-3xl">{{ email }}</p>
      <a class="text-sm lg:text-base underline text-gray-500" href="#"> Хотите сменить пароль?</a>
  </div>
</template>


<script setup>
import { ref } from 'vue'

const name = ref('Username')
const email = ref('asdasd@mail.ru')
</script>
