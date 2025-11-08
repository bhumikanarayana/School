<template>
<div>
      <img
        v-if="gallery?.main_image"
        :src="gallery.main_image"
        :alt="gallery.title"
        class="px-14 w-full h-auto max-h-[400px] object-fill pt-14 mb-6 rounded-2xl"
      />
      <section class="max-w-6xl mx-auto">
    <div v-if="loading" class="text-center">Loading...</div>

    <div v-else-if="gallery">

      <div class="flex gap-2 text-orange-600 text-3xl md:px-0 px-14">
        <h2><strong>{{ gallery?.category }}</strong></h2>
        <h2><strong>{{ gallery?.year }}</strong></h2>
      </div>

      <div class="mt-4 px-14 md:px-0 ql-editor read-mode" v-html="gallery?.description"></div>

      <hr class="my-6" />

      <!-- Games Conducted -->
      <div v-if="gallery?.games_conducted?.length">
        <div v-for="game in gallery.games_conducted" :key="game.game_name" class="mb-4">
        <div class="flex gap-2 text-orange-600 text-2xl">
        <h2><strong>{{ game.game_name }}</strong></h2>
        <h2><strong>{{ game.winners }}</strong></h2>
      </div>

          <div class="flex flex-col md:flex-row gap-4 mt-2">
          <div class="md:w-1/2 flex flex-col gap-4">
            <div v-for="img in game.game_image" :key="img.image">
              <img :src="img.image" class="w-full h-80 object-cover rounded" />
            </div>
          </div>
           <div class="md:w-1/2 flex flex-col gap-4">
            <div v-for="img in game.winners_image" :key="img.image">
              <img :src="img.image" class="w-full h-80  object-cover rounded" />
            </div>
            </div>
            <!-- Combined Images Section -->

          </div>
        </div>
      </div>

      <!-- Guests -->
      <div v-if="gallery?.guests?.length">
        <h2 class="text-2xl font-semibold mb-2">Guests</h2>
        <div v-for="guest in gallery.guests" :key="guest.guest_name" class="flex items-center gap-4 mb-2">
          <img v-if="guest.photo" :src="guest.photo" class="w-16 h-16 object-cover rounded-full" />
          <div>
            <p class="font-semibold">{{ guest.guest_name }}</p>
            <p>{{ guest.designation }}</p>
          </div>
        </div>
      </div>

      <!-- Gallery Images -->
      <div v-if="gallery?.gallery_images?.length">
        <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
          <div v-for="img in gallery.gallery_images" :key="img.image">
            <img :src="img.image" class="w-full h-40 object-cover rounded" />
            <p class="text-sm mt-1">{{ img.caption }}</p>
          </div>
        </div>
      </div>
    </div>

    <div v-else class="text-center text-red-500">
      Gallery not found.
    </div>
  </section>
</div>
</template>


<script>
import axios from "axios";

export default {
  data() {
    return {
      gallery: null,
      loading: true,
    };
  },
  async mounted() {
    const id = this.$route.params.id; // get id from route
    try {
      const res = await axios.get("/api/method/school.api.details.get_gallery", {
        params: { name: id }, // pass id as title to the API
      });
      this.gallery = res.data.message;
    } catch (err) {
      console.error("Error fetching gallery details:", err);
    } finally {
      this.loading = false;
    }
  },
};
</script>
