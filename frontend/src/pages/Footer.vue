<template>
<footer class="bg-[#003F7D] text-white py-10 px-8">
  <div class="px-8 max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-[1.5fr_1fr_1fr_1fr] gap-8">
    
    <!-- Column 1: Logo + Social Icons -->
    <div class="flex flex-col items-center md:items-start space-y-4">
      <!-- Logo -->
      <img src="@/assets/logoschool.png" alt="Logo" class="w-32 md:w-30" />

      <!-- Social Icons (FontAwesome) -->
      <div class="flex space-x-4 items-center md:items-start pt-6">
        <a href="#" class="hover:text-red-600">
          <font-awesome-icon :icon="['fab','youtube']" class="h-6 w-6"/>
        </a>
        <a href="#" class="hover:text-blue-600">
          <font-awesome-icon :icon="['fab','facebook']" class="h-6 w-6"/>
        </a>
        <a href="#" class="hover:text-pink-500">
          <font-awesome-icon :icon="['fab','instagram']" class="h-6 w-6"/>
        </a>
        <a href="#" class="hover:text-blue-500">
          <font-awesome-icon :icon="['fab','linkedin']" class="h-6 w-6"/>
        </a>
      </div>
    </div>

    <!-- Column 2: Links -->
    <div class="flex flex-col space-y-2 items-center md:items-start">
      <h3 class="font-semibold mb-2">My Account</h3>
      <a href="#" class="hover:underline">About SBA</a>
      <a href="#" class="hover:underline">Support</a>
      <a href="#" class="hover:underline">Admission</a>
    </div>

    <!-- Column 3: Dashboard -->
    <div class="flex flex-col space-y-2 items-center md:items-start">
      <h3 class="font-semibold mb-2">Dashboard</h3>
      <a href="#" class="hover:underline">Contact Us</a>
      <a href="#" class="hover:underline">School Life</a>
      <a href="#" class="hover:underline">Login</a>
    </div>

    <!-- Column 4: Newsletter / Contact -->
    <div class="flex flex-col space-y-4 items-center md:items-start">
      <h3 class="font-semibold mb-2">Newsletter</h3>
      <p class="text-sm">Join our mailing list to stay up to date with world</p>
      <div class="flex flex-col sm:flex-row gap-2">
        <div class="relative w-full sm:w-auto">
          <EnvelopeIcon class="absolute left-2 top-2.5 h-5 w-5 text-gray-400"/>
          <input 
            type="email" 
            placeholder="Email address" 
            class="pl-8 pr-3 py-2 border rounded-md w-full sm:w-auto"
          />
        </div>
        <button class="bg-orange-500 text-white px-4 py-2 rounded-md hover:bg-orange-600">
          Subscribe
        </button>
      </div>
    </div>

  </div>

  <!-- Footer Bottom -->
  <div class="mt-8 border-t border-white/30 pt-4 text-sm text-white text-center">
    © 2022 Single Best Answer. All Rights Reserved. <br/>
    Created with love by <a href="#" class="hover:underline">thecreation.design</a>
  </div>
</footer>
</template>

<script>
import { EnvelopeIcon } from '@heroicons/vue/24/solid'

export default {
  name: 'Footer',
  components: {
    EnvelopeIcon
  }
}
</script>
