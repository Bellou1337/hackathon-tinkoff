<script setup>
import Navbar from '@/components/Navbar.vue'
import ProfileView from '@/components/profile/ProfileView.vue'
</script>

<template>
  <Navbar />
  <div class="max-w-screen-xl mx-auto h-screen grid grid-rows-layout">
    <ProfileView />
  </div>
</template>
