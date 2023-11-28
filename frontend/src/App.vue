<script setup lang="ts">
</script>

<template>
  <div className="App">
    <div>
      <!-- <Navbar /> -->
      Nabbar
    </div>
    <div className="flex min-h-screen bg-gray-100 justify-center pt-3">
      <div className="w-11/12">
        <div className="col-span-1 md:col-span-2 bg-white shadow-lg rounded-lg p-4">
    
          <router-view></router-view>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
