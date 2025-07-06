<template>
  <nav
    class="d-flex justify-content-between align-items-center px-2"
    style="height: 40px; background-color: #2b2b2b;"
  >
    <!-- LEFT: Logo + Menu -->
    <div class="d-flex align-items-center gap-2">
      <img src="../../public/favicon.ico" alt="Logo" width="20" height="20" />

      <!-- Menu Items -->
      <div
        class="dropdown"
        v-for="(item, index) in menuItems"
        :key="index"
      >
        <button
          class="dropdown-toggle text-white border-0 bg-transparent shadow-none"
          type="button"
          data-bs-toggle="dropdown"
          aria-expanded="false"
          style="font-size: 12px; padding: 0 8px;"
        >
          {{ item.title }}
        </button>

        <ul class="dropdown-menu dropdown-menu-dark p-1">
          <li
            v-for="(child, i) in item.children"
            :key="i"
          >
            <a class="dropdown-item py-1 px-3" href="#">{{ child }}</a>
          </li>
        </ul>
      </div>
    </div>

    <!-- RIGHT: Window Controls (Google Material Icons) -->
    <div class="d-flex align-items-center gap-2 me-1 text-white">
      <span class="material-icons" style="font-size: 16px; cursor: pointer;" @click="onMinimize">remove</span>
      <span class="material-icons" style="font-size: 16px; cursor: pointer;" @click="onMaximize">crop_square</span>
      <span class="material-icons" style="font-size: 16px; cursor: pointer;" @click="onClose">close</span>
    </div>

  </nav>
</template>

<script setup>
const menuItems = [
  { title: 'File', children: ['New File', 'Open', 'Save', 'Exit'] },
  { title: 'Edit', children: ['Undo', 'Redo', 'Cut', 'Copy'] },
  { title: 'View', children: ['Tool Windows', 'Appearance'] },
  { title: 'Git', children: ['Commit', 'Branches', 'Push'] },
  { title: 'Help', children: ['About', 'Check for Updates'] },
]

// Dummy handlers (replace with Electron event if needed)
const onMinimize = () => console.log('Minimize')
const onMaximize = () => console.log('Maximize')
const onClose = () => console.log('Close')
</script>

<style scoped>
.dropdown-toggle::after {
  display: none;
}
</style>
