<script setup>
import { computed } from 'vue'
import { useUIStore } from '@/stores/ui'

const ui = useUIStore()

const wrapperStyle = computed(() => ({
  marginLeft: ui.sidebarVisible ? '200px' : '45px',
  marginTop: '40px',
  transition: 'margin-left 0.2s ease',
}))
</script>

<template>
  <div :style="wrapperStyle" class="main-content">
    <slot />
    <router-view />
  </div>
</template>

<style scoped>
.main-content {
  padding: 16px;
  background-color: #1e1e1e;
  min-height: calc(100vh - 40px);
  color: white;
}
</style>
