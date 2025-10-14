<template>
  <nav class="bg-white shadow-md fixed w-full z-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between h-16 items-center">

        <!-- Left: Logo -->
        <div class="flex-shrink-0 flex items-center">
          <img src="@/assets/logoschool.png" alt="Logo" class="h-10 w-auto" />
        </div>

        <!-- Center: Nav Items (Desktop Only) -->
        <div class="hidden md:flex space-x-8">
          <router-link to="/" class="text-gray-700 hover:text-orange-500 font-medium">Home</router-link>
          <router-link to="/aboutus" class="text-gray-700 hover:text-orange-500 font-medium">AboutUs</router-link>
          <router-link to="/schoollife" class="text-gray-700 hover:text-orange-500 font-medium">School Life</router-link>
          <router-link to="/announcements" class="text-gray-700 hover:text-orange-500 font-medium">Announcements</router-link>
          <router-link to="/gallery" class="text-gray-700 hover:text-orange-500 font-medium">Gallery</router-link>
          <router-link to="/contactus" class="text-gray-700 hover:text-orange-500 font-medium">Contact</router-link>
        </div>

        <!-- Right: Login & Admission (Desktop Only) -->
        <div class="hidden md:flex items-center space-x-4">
           <a href="/login"
            class="border border-orange-500 text-orange-500 px-4 py-2 rounded-lg hover:bg-orange-500 hover:text-white transition-colors">
            Login
          </a>
           <a href="http://127.0.0.1:8000/studentadmission" class="bg-orange-500 hover:bg-orange-500 text-white px-4 py-2 rounded-lg">
            Admission
          </a>
        </div>

        <!-- Mobile Menu Button -->
        <div class="md:hidden">
          <button @click="isOpen = !isOpen" class="text-gray-700 focus:outline-none">
            <svg v-if="!isOpen" xmlns="http://www.w3.org/2000/svg" class="h-6 w-6"
              fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M4 6h16M4 12h16M4 18h16" />
            </svg>
            <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-6 w-6"
              fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile Menu Dropdown -->
    <div v-if="isOpen" class="md:hidden bg-white shadow-lg">
      <div class="px-4 pt-4 pb-4 space-y-2">
        <router-link to="/" class="block text-gray-700 hover:text-orange-500">Home</router-link>
        <router-link to="/aboutus" class="block text-gray-700 hover:text-orange-500">About</router-link>
        <router-link to="/schoollife" class="block text-gray-700 hover:text-orange-500">School Life</router-link>
        <router-link to="/announcements" class="text-gray-700 hover:text-orange-500 font-medium">Announcements</router-link>
        <router-link to="/gallery" class="block text-gray-700 hover:text-orange-500">Gallery</router-link>
        <router-link to="/contactus" class="block text-gray-700 hover:text-orange-500">Contact</router-link>

        <div class="border-t pt-3 flex items-center gap-3">
            <!-- Login Button -->
            <button class="border border-orange-500 text-orange-500 px-4 py-1 rounded-lg hover:bg-orange-500 hover:text-white transition-colors">
                Login
            </button>

            <!-- Admission Button -->
            <a href="http://127.0.0.1:8000/studentadmission" class="bg-orange-500 hover:bg-orange-600 text-white px-4 py-1 rounded-lg">
                Admission
            </a>
        </div>

      </div>
    </div>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      isOpen: false
    }
  }
}
</script>
