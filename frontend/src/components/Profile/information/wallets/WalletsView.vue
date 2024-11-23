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
  <div class=" mt-10 flex flex-col items-center gap-5">
    <p class=" text-3xl">Текущие кошельки</p>
    <div class="rounded-lg max-h-80 w-full pl-4 overflow-y-auto flex flex-col mb-2 scrollbar">
      <div class="flex flex-col w-full min-h-20 h-full rounded-xl justify-between items-center my-1">
        <wallet v-for="wal in Wallets" 
          key="index"
          class="my-2"
          :Naming="wal.naming"
          :countOfMoney = "wal.countOfMoney"
          :banknote = "wal.banknote"
          ></wallet>  
        </div>
    </div>
    <router-link to="/profile/newWallet" class=" text-black bg-gray-200 hover:bg-gray-300 active:bg-gray-400 flex items-center justify-center rounded-xl shadow-xl text-xl text-center  max-w-40 my-5"> Создать кошелек </router-link>
  </div>
</template>
