<template>
    <header>
        <UserInfo
        :email = userEmail
        :name = userName>
        </UserInfo>
    </header>
    
    <main>

    </main>
    
    <footer>

    </footer>
</template>

<script setup>
import {ref} from 'vue';
import UserInfo from '@/components/Profile/UserInfoView.vue';
import Costs from '@/components/Profile/CostsView.vue';

const userName = ref('Username');
const userEmail = ref('asdasd@mail.ru');


defineProps(

)
</script>