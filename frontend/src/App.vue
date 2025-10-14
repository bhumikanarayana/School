<template>
  <div>
    <Navbar />
    <router-view />
    <Footer />

    <!-- Sticky Enquiry Button (Visible on both Desktop & Mobile) -->
    <button
      v-if="$route.name !== 'Enquiry'"
      @click="$router.push({ name: 'Enquiry' })"
      class="flex items-center justify-center 
             fixed right-0 top-1/2 -translate-y-1/2 
             bg-orange-500 hover:bg-orange-600 text-white font-normal
             px-2 py-3 shadow-lg z-50 
             [writing-mode:vertical-rl] rotate-180
             rounded-tr-md rounded-br-md"
    >
      Admission Enquiry
    </button>
  </div>
</template>

<script>
import Navbar from '@/pages/Navbar.vue'
import Footer from '@/pages/Footer.vue'

export default {
  components: { Navbar, Footer },
};
</script>
