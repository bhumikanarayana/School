<template>
  <section class="w-full pt-16">
    <!-- Full Width Top Image -->
    <div class="w-full">
      <img 
        src="@/assets/gallery.jpg" 
        alt="Gallery Banner" 
        class="w-full h-64 md:h-96 object-cover"
      />
    </div>

     <div class="max-w-7xl mx-auto px-8 py-8">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div v-for="(image, index) in images" :key="index">
          <img 
            :src="image.image" 
            alt="Gallery Image" 
            class="w-full h-64 object-cover rounded-xl shadow-md hover:scale-105 transition-transform duration-300"
          />
        </div>
      </div>
    </div>
  </section>
</template>

<script>


export default {
  name: "GalleryPage",
  data() {
    return {
      images: [],
    };
  },
  async created() {
    try {
      const res = await fetch("/api/method/school.api.gallery.get_gallery_images");
      const data = await res.json();
      this.images = data.message; // Frappe returns {message: [...]}
    } catch (error) {
      console.error("Failed to fetch gallery images:", error);
    }
  },
};
</script>
