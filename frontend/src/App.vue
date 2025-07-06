<script setup>
import { RouterLink, RouterView } from 'vue-router'
import TopMenuBar from "@/components/TopMenuBar.vue";
import SideBarLeft from "@/components/SideBarLeft.vue";
import MainContent from "@/components/MainContent.vue";
</script>

<template>
  <top-menu-bar />
  <div class="container-fluid mt-2">
    <!-- Nội dung chính -->
    <side-bar-left/>
<!--    <router-view />-->
    <main-content/>
  </div>
</template>

<style scoped>
</style>
