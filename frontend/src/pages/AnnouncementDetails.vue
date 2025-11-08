<template>
  <div class="p-6">
    <div v-if="loading">Loading announcement...</div>
    <div v-else>
      <h1 class="text-2xl font-bold mb-4">{{ announcement.title }}</h1>

      <img
        v-if="announcement.icon"
        :src="announcement.icon"
        alt="icon"
        class="w-16 h-16 mb-4"
      />

      <p class="mb-4">{{ announcement.about }}</p>

      <!-- Show more content if show_know_more is checked -->
     <div v-if="announcement.show_know_more && announcement.more_content">
    <h2 class="text-lg font-semibold mb-2">More Details:</h2>
    <div v-html="announcement.more_content"></div>
    </div>


      <p class="text-gray-500 mt-4">{{ announcement.date }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "AnnouncementDetails",
  data() {
    return {
      announcement: {},
      loading: true,
    };
  },
 async created() {
  // The 'name' param comes from the route
  const name = this.$route.params.name;

  if (!name) {
    console.error("No announcement name provided in route!");
    this.loading = false;
    return;
  }

  try {
    const res = await axios.get(
      "/api/method/school.api.announcementsdetails.get_announcement_details",
      { params: { name } }
    );

    console.log("API response:", res.data.message);
    this.announcement = res.data.message;

  } catch (err) {
    // 👇 Replace your old catch block with this
    console.error("Failed to load announcement details:", err);
    if (err.response) {
      console.error("Error Response:", err.response.data);
    } else if (err.request) {
      console.error("No response received:", err.request);
    } else {
      console.error("Error setting up request:", err.message);
    }
  } finally {
    this.loading = false;
  }
}


};
</script>
