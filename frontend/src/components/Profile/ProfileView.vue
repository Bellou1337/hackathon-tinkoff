<script setup>
import UserInfoView from '@/components/profile/information/UserInfoView.vue'
import MoneyView from '@/components/profile/information/MoneyView.vue'
import WalletsView from '@/components/profile/information/wallets/WalletsView.vue'
</script>

<template>
<<<<<<< HEAD
  <div class="dark:bg-neutral-800 bg-slight-gray flex flex-col px-5 min-h-screen">
    <div class="dark:text-white border-b-2 border-black dark:border-white pb-5">
      <UserInfoView />
      <div
        class="flex flex-col sm:flex-col md:flex-row lg:flex-row items-center justify-center gap-5"
      >
        <MoneyView class="lg:w-2/3 w-full" />
        <WalletsView class="lg:w-1/3 w-full" />
      </div>
=======
  <div class=" dark:bg-neutral-800 bg-slight-gray md:px-5 px-2 min-h-screen items-center md:items-baseline justify-center py-10 flex md:flex-row flex-col">
    <div class=" md:w-7/12 w-full flex flex-col items-start">
      <UserInfoView/>
      <MoneyView class="md:w-5/6 w-full"/>
>>>>>>> 3af8846c7f918174b84009f5bc9bccf5e64d9334
    </div>
    <div class="md:w-5/12 w-full">
      <WalletsView class=""/>
    </div>      
  </div>
</template>
