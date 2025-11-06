<template>
  <div class="w-full pt-16">
    <!-- Full-width Photo -->
    <div class="w-full">
      <img 
        src="@/assets/co.jpg" 
        alt="Contact Us Banner" 
        class="w-full h-auto sm:h-80 md:h-[500px] object-contain md:object-cover"
      />
    </div>

    <!-- Two Boxes Section -->
    <div class="max-w-7xl mx-auto px-6 md:px-16 py-10 grid grid-cols-1 md:grid-cols-2 gap-8 md:gap-16 items-stretch">
      
      <!-- Box 1: School Details -->
      <div class="bg-gray-100 shadow-lg rounded-2xl p-8 border border-gray-300 flex flex-col justify-center h-full">
        <!-- Contact Number -->
        <div class="flex items-center gap-4 px-4">
          <div class="w-12 h-12 rounded-full bg-[#1A5A96] flex items-center justify-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-orange-400" viewBox="0 0 640 640" fill="currentColor">
              <path d="M224.2 89C216.3 70.1 195.7 60.1 176.1 65.4L170.6 66.9C106 84.5 50.8 147.1 66.9 223.3C104 398.3 241.7 536 416.7 573.1C493 589.3 555.5 534 573.1 469.4L574.6 463.9C580 444.2 569.9 423.6 551.1 415.8L453.8 375.3C437.3 368.4 418.2 373.2 406.8 387.1L368.2 434.3C297.9 399.4 241.3 341 208.8 269.3L253 233.3C266.9 222 271.6 202.9 264.8 186.3L224.2 89z"/>
            </svg>
          </div>
          <div>
            <span class="block text-gray-800 text-lg font-semibold">Contact Number:</span>
            <span class="text-gray-700 text-base">+91 96864 50917</span>
          </div>
        </div>

        <!-- Email -->
        <div class="flex items-center gap-4 px-4 mt-6">
          <div class="w-12 h-12 rounded-full bg-[#1A5A96] flex items-center justify-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-orange-400" fill="currentColor" viewBox="0 0 24 24">
              <path d="M20 4H4C2.897 4 2 4.897 2 6V18C2 19.103 2.897 20 4 20H20C21.103 20 22 19.103 22 18V6C22 4.897 21.103 4 20 4zM20 6L12 11 4 6H20z"/>
            </svg>
          </div>
          <div>
            <span class="block text-gray-800 text-lg font-semibold">Email:</span>
            <span class="text-gray-700 text-base">hello@ramaschool.com</span>
          </div>
        </div>

        <!-- Address -->
        <div class="flex items-center gap-4 px-4 mt-6">
          <div class="w-12 h-12 rounded-full bg-[#1A5A96] flex items-center justify-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="w-6 h-6 text-orange-400" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12 2C8.13 2 5 5.13 5 9C5 13.25 12 22 12 22C12 22 19 13.25 19 9C19 5.13 15.87 2 12 2zM12 11.5C10.62 11.5 9.5 10.38 9.5 9C9.5 7.62 10.62 6.5 12 6.5C13.38 6.5 14.5 7.62 14.5 9C14.5 10.38 13.38 11.5 12 11.5z"/>
            </svg>
          </div>
          <div>
            <span class="block text-gray-800 text-lg font-semibold">Address:</span>
            <span class="text-gray-700 text-base">13th Cross Road, 1st Phase, JP Nagar, Bengaluru, Karnataka</span>
          </div>
        </div>
      </div>

      <!-- Box 2: Map -->
      <div class="bg-gray-100 shadow-lg rounded-2xl border border-gray-300 flex items-center justify-center h-full">
        <iframe
          class="w-full h-[400px] md:h-full rounded-xl"
          src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d31114.123456789!2d77.5798912!3d12.9112345!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae1a5c1234567%3A0xabcdef0123456789!2s13th%20Cross%20Rd%2C%201st%20Phase%2C%20JP%20Nagar%2C%20Bengaluru%2C%20Karnataka%20560078!5e0!3m2!1sen!2sin!4v169XXXXXXXXX!5m2!1sen!2sin"
          allowfullscreen=""
          loading="lazy"
          referrerpolicy="no-referrer-when-downgrade">
        </iframe>
      </div>
      
    </div>
  </div>
</template>

<script>
export default {
  name: "ContactUs",
};
</script>
