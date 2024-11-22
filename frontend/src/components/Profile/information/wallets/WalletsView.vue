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
    naming:'4',
    countOfMoney:600,
    banknote:'руб.'
  },
  {
    naming:'5',
    countOfMoney:700,
    banknote:'руб.'
  },
  {
    naming:'6',
    countOfMoney:380,
    banknote:'руб.'
  }
])
//
</script>

<template>
  <div class="flex flex-col gap-5 items-center">
      <div class=" h-full grid grid-cols-3 gap-3 min-w-56 justify-center">
      <wallet v-for="wallet in Wallets" 
      key="index"
      class="my-5"
      :Naming=wallet.naming
      :countOfMoney = wallet.countOfMoney
      :banknote = wallet.banknote
      ></wallet>
    </div>
    <a href="#" class=" hover:bg-yellow-300 active:bg-yellow-400 flex items-center justify-center rounded-xl shadow-xl text-xl text-center bg-slate-300 max-w-40 my-5"> Создать кошелек </a>
  </div>
</template>
