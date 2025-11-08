<template>
  <div class="w-full p-10 pt-20 space-y-6">
    <!-- Full-width Cards -->
    <div
      v-for="(announcement, index) in announcements"
      :key="index"
      class="px-14 bg-white shadow-md border border-gray-400 rounded-xl p-6 w-full"
    >
      <!-- Heading -->
      <h2 class="text-xl font-bold mb-4">{{ announcement.title }}</h2>

      <!-- Icon + About -->
      <div class="flex items-start gap-4 mb-4">
        <img
          :src="announcement.icon"
          alt="icon"
          class="w-12 h-8 object-contain"
        />
        <p class="text-gray-700">{{ announcement.about }}</p>
      </div>

      <!-- Date + Button -->
      <div class="flex justify-between items-center">
        <p class="text-sm text-gray-500">{{ announcement.date }}</p>
        <button
        v-if="announcement.more"
        @click="$router.push({ name: 'AnnouncementDetails', params: { name: announcement.name } })"
        class="bg-orange-500 hover:bg-orange-600 text-white text-sm px-4 py-2 rounded-lg"
        >
        Know More
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Announcements",
  data() {
    return {
      announcements: [],
    };
  },
  async created() {
    try {
      const res = await axios.get("/api/method/school.api.announcements.get_announcements");
      this.announcements = res.data.message;
    } catch (error) {
      console.error("Failed to fetch announcements:", error);
    }
  },
};
</script>
