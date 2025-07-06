<script setup>
import { ref } from 'vue'
const activeTab = ref(null)

const toggleTab = (tab) => {
  activeTab.value = activeTab.value === tab ? null : tab
}
</script>

<template>
  <div class="sidebar-left d-flex flex-column align-items-center py-2">
    <span class="icon-btn" @click="toggleTab('explorer')">
      <svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#FFFFFF">
        <path d="M72-144q-29.7 0-50.85-21.15Q0-186.3 0-216h168q-29.7 0-50.85-21.15Q96-258.3 96-288v-456q0-29.7 21.15-50.85Q138.3-816 168-816h624q29.7 0 50.85 21.15Q864-773.7 864-744v456q0 29.7-21.15 50.85Q821.7-216 792-216h168q0 30-21.15 51T888-144H72Zm407.79-36q15.21 0 25.71-10.29t10.5-25.5q0-15.21-10.29-25.71t-25.5-10.5q-15.21 0-25.71 10.29t-10.5 25.5q0 15.21 10.29 25.71t25.5 10.5ZM168-288h624v-456H168v456Zm0 0v-456 456Z"/>
      </svg>
    </span>

    <span class="icon-btn" @click="toggleTab('git')" style="transform: rotate(270deg);">
      <svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#FFFFFF">
        <path d="M480-288q-70.59 0-123.3-44.5Q304-377 290.64-444H96v-72h195q13-67 65.7-111.5Q409.41-672 480-672t123.3 44.5Q656-583 669.36-516H864v72H669q-13 67-65.7 111.5Q550.59-288 480-288Zm0-72q50 0 85-35t35-85q0-50-35-85t-85-35q-50 0-85 35t-35 85q0 50 35 85t85 35Z"/>
      </svg>
    </span>
  </div>

  <!-- Tab Area -->
  <div class="sidebar-tab" v-if="activeTab === 'explorer'">
    <p class="text-white m-2">Explorer Content</p>
  </div>

  <div class="sidebar-tab" v-if="activeTab === 'git'">
    <p class="text-white m-2">Git Tab Content</p>
  </div>
</template>

<style scoped>
.sidebar-tab {
  width: 300px;
  background-color: #212121;
  color: #ffffff;
}
.sidebar-left {
  width: 45px;
  background-color: #2b2b2b;
  color: white;
  position: fixed;
  top: 40px;
  bottom: 0;
  left: 0;
  z-index: 999;
}

.sidebar-tab {
  position: fixed;
  left: 45px;
  top: 40px;
  bottom: 0;
  width: 300px;
  background-color: #313335;
  z-index: 998;
  overflow: auto;
  border-right: 1px solid #444;
}

.icon-btn {
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.2s ease;
  padding: 8px;
  border-radius: 6px;
}

.icon-btn:hover {
  background-color: #3c3f41;
}
</style>
