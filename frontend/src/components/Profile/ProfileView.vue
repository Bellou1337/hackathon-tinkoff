<script setup>
import UserInfoView from '@/components/profile/information/UserInfoView.vue'
import MoneyView from '@/components/profile/information/MoneyView.vue'
import WalletsView from '@/components/profile/information/wallets/WalletsView.vue'
</script>

<template>
  <div class="flex flex-col">
      <UserInfoView/>
    <div class="flex items-center gap-5">
      <MoneyView class="w-2/3"/>
      <WalletsView class="w-1/3"/>
    </div>  
  </div>
</template>
