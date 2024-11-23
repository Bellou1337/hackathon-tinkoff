<script setup>
import UserInfoView from '@/components/profile/information/UserInfoView.vue'
import MoneyView from '@/components/profile/information/MoneyView.vue'
import WalletsView from '@/components/profile/information/wallets/WalletsView.vue'
</script>

<template>
  <div
    class="dark:bg-neutral-800 bg-slight-gray md:px-5 px-2 min-h-screen items-center md:items-baseline justify-center py-10 flex md:flex-row flex-col"
  >
    <div class="md:w-7/12 w-full flex flex-col items-start">
      <UserInfoView />
      <MoneyView class="md:w-5/6 w-full" />
    </div>
    <div class="md:w-5/12 w-full">
      <WalletsView class="" />
    </div>
  </div>
</template>
