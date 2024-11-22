<script setup>
import wallet from '@/components/profile/information/wallets/Wallet.vue';
import {ref} from 'vue';

const infoAboutWallet = ref(
  {
    naming:'',
    countOfMoney:'',
    banknote:''
  }
)
const arrayOfWallet = ref([]);

//Заглушка v
const Wallets = ref([
  {
    naming:'First',
    countOfMoney:1000,
    banknote:'руб.'
  },
  {
    naming:'Second',
    countOfMoney:2500,
    banknote:'руб.'
  },
  {
    naming:'Third',
    countOfMoney:300,
    banknote:'руб.'
  }
])
//
</script>

<template>
  <div class="w-full">
    <wallet v-for="wallet in Wallets" 
    key="index"
    class=" my-5"
    :Naming=wallet.naming
    :countOfMoney = wallet.countOfMoney
    :banknote = wallet.banknote
    ></wallet>
  </div>
</template>
