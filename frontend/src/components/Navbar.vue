
<template>
  <nav className="bg-white shadow-lg">
      <!-- Navbar-->
      <div className="max-w-6xl mx-auto px-4">
          <div className="flex justify-between">

              <!-- left side -->
              <div className="flex space-x-7">
                  <!-- logo -->
                  <div>
                      <a href="/" className="flex items-center py-4 px-2">
                          <span className="font-semibold text-gray-500 text-lg">Logo</span>
                      </a>
                  </div>

                  <!-- pc version -->
                  <div className="hidden md:flex items-center space-x-1">
                      <a href="/" className="py-4 px-2 text-green-500 border-b-4 border-green-500 font-semibold ">Booking</a>
                      <a href="contact-us" className="py-4 px-2 text-gray-500 font-semibold hover:text-green-500 transition duration-300">Contact Us</a>
                  </div>
              </div>
              
              <!-- right side -->
              <div className="hidden md:flex items-center space-x-3 ">
                  <a href="/login" className="py-2 px-2 font-medium text-gray-500 rounded hover:bg-green-500 hover:text-white transition duration-300">Log In</a>
              </div>
              
              <!-- hambergur botton -->
              <div className="md:hidden flex items-center">
                  <button className="outline-none mobile-menu-button" @click="onHamburgerClick">
                    <!-- _____ -->
                    <svg className=" w-6 h-6 text-gray-500 hover:text-green-500 "
                        x-show="!showMenu"
                        fill="none"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                        width="30px"
                    >
                        <path d="M4 6h16M4 12h16M4 18h16"></path>
                    </svg>
                  </button>
              </div>
          </div>
      </div>
      
      <!-- mobile menu-->
      <div class="mobile-menu" :class="{ 'hidden': menuActive }">
          <ul className="">
              <li className="active"><a href="/" className="block text-sm px-2 py-4 text-white bg-green-500 font-semibold">Booking</a></li>
              <li><a href="contact-us" className="block text-sm px-2 py-4 hover:bg-green-500 transition duration-300">Contact Us</a></li>
              <li><a href="login" className="block text-sm px-2 py-4 hover:bg-green-500 transition duration-300">Log In</a></li>
          </ul>
      </div>
  </nav>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const menuActive = ref(true);

const onHamburgerClick = () => {
  menuActive.value = !menuActive.value;
}

</script>

<style lang="scss" scoped>
</style>