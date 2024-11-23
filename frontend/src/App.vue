<template>

  <Navbar/>

  <router-view class=" z-10" />

  <Footer class=" z-50"/>
</template>
<script setup>

import Navbar from './components/Navbar.vue';
import Footer from './components/Footer.vue';
</script>