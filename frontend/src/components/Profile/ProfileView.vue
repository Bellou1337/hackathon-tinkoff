<script setup>
import UserInfoView from '@/components/profile/information/UserInfoView.vue'
import MoneyView from '@/components/profile/information/MoneyView.vue'
import WalletsView from '@/components/profile/information/wallets/WalletsView.vue'
</script>

<template>
  <div class="dark:bg-neutral-800 bg-slight-gray flex flex-col px-5 min-h-screen">
    <div class="dark:text-white border-b-2 border-black dark:border-white pb-5">
      <UserInfoView />
      <div
        class="flex flex-col sm:flex-col md:flex-row lg:flex-row items-center justify-center gap-5"
      >
        <MoneyView class="lg:w-2/3 w-full" />
        <WalletsView class="lg:w-1/3 w-full" />
      </div>
    </div>
  </div>
</template>
