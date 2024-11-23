<script setup>
import UserInfoView from '@/components/profile/information/UserInfoView.vue'
import MoneyView from '@/components/profile/information/MoneyView.vue'
import WalletsView from '@/components/profile/information/wallets/WalletsView.vue'
</script>

<template>
  <div class="md:my-16 my-8 max-w-screen-xl mx-auto flex flex-col justify-center">
    <div class="flex md:flex-row flex-col mb-8">
      <div class="md:w-1/2 w-full"><UserInfoView /></div>
      <div class="md:w-1/2 w-full"><WalletsView /></div>
    </div>

    <MoneyView />
  </div>
</template>
