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
  <div class="flex flex-col items-center gap-5">
    <p class=" text-3xl">Текущие кошельки</p>
      <div class="  rounded-lg max-h-[10rem] mt-5 min-h-80 w-full overflow-y-auto scrollbar flex flex-col items-center justify-center mb-2">
      <wallet v-for="wallet in Wallets" 
      key="index"
      class="my-1"
      :Naming=wallet.naming
      :countOfMoney = wallet.countOfMoney
      :banknote = wallet.banknote
      ></wallet>
    </div>
    <router-link to="/profile/newWallet" class=" text-black bg-gray-200 hover:bg-gray-300 active:bg-gray-400 flex items-center justify-center rounded-xl shadow-xl text-xl text-center  max-w-40 my-5"> Создать кошелек </router-link>
  </div>
</template>
