<template>
<section class="w-full pt-16">
  <img 
    src="@/assets/hom.jpg" 
    alt="Home Page Image" 
    class="w-full h-auto  object-cover"
  />
</section>
<section class="w-full p-4 px-10 md:px-24">
  <!-- Filter Section -->
  <div
    class="flex flex-wrap sm:flex-nowrap items-center justify-center gap-2 sm:gap-3 mb-3 px-2 py-2 sm:py-0 bg-white sm:bg-transparent rounded-lg shadow-sm sm:shadow-none"
  >
    <!-- Category Dropdown -->
    <div class="relative flex-shrink-0 w-32 sm:w-36">
      <select
        v-model="selectedCategory"
        class="appearance-none bg-white border border-gray-300 rounded-xl px-3 py-1.5 sm:px-3 sm:py-2 pr-8 text-gray-700 text-sm focus:outline-none focus:ring-2 focus:ring-orange-400 w-full"
        style="-webkit-appearance: none; -moz-appearance: none; appearance: none;"
      >
        <option value="">All Categories</option>
        <option
          v-for="category in categories"
          :key="category"
          :value="category"
        >
          {{ category }}
        </option>
      </select>
      <svg
        class="w-3 h-3 absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-600 pointer-events-none"
        fill="none"
        stroke="currentColor"
        stroke-width="2"
        viewBox="0 0 24 24"
      >
        <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
      </svg>
    </div>

    <!-- Year Dropdown -->
    <div class="relative flex-shrink-0 w-28 sm:w-32">
      <select
        v-model="selectedYear"
        class="appearance-none bg-white border border-gray-300 rounded-xl px-3 py-1.5 sm:px-3 sm:py-2 pr-8 text-gray-700 text-sm focus:outline-none focus:ring-2 focus:ring-orange-400 w-full"
        style="-webkit-appearance: none; -moz-appearance: none; appearance: none;"
      >
        <option value="">All Years</option>
        <option v-for="year in years" :key="year" :value="year">
          {{ year }}
        </option>
      </select>
      <svg
        class="w-3 h-3 absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-600 pointer-events-none"
        fill="none"
        stroke="currentColor"
        stroke-width="2"
        viewBox="0 0 24 24"
      >
        <path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7" />
      </svg>
    </div>

    <!-- Apply Button -->
    <button
      @click="applyFilter"
      class="bg-orange-500 hover:bg-slate-600 text-white text-sm px-3 py-1.5 sm:px-4 sm:py-2.5 rounded-xl shadow-md whitespace-nowrap"
    >
      Apply
    </button>
  </div>

  <!-- Gallery Grid -->
  <div
    v-if="filteredGallery.length"
    class="p-4 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4"
  >
    <div
      v-for="item in filteredGallery"
      :key="item.name"
      class="rounded-xl overflow-hidden shadow-md hover:scale-105 transition-transform cursor-pointer"
      @click="goToDetails(item.name)"
    >
      <img
        :src="item.main_image"
        :alt="item.title || 'Gallery Image'"
        class="w-full h-48 object-cover"
      />
    </div>
  </div>

  <p v-else class="text-center text-gray-600 text-sm">
    No gallery items found for selected filters.
  </p>
</section> 
<section class="bg-gray-100">
      <div class="max-w-7xl mx-auto p-8 sm:px-10 lg:px-10 py-5 flex flex-col md:flex-row items-center md:justify-center gap-4">
        <!-- Right Image -->
        <div class="w-full md:w-1/2 flex justify-center md:pr-0">
          <img src="@/assets/students.png" alt="Hero Image" class="w-full max-w-sm md:max-w-md h-auto object-cover rounded-lg" />
        </div>
        <!-- Left Content -->
        <div class="w-full md:w-1/2 md:pr-20 px-4">
            <h1 class="text-[1rem] md:text-[1.5rem] font-semibold text-orange-400 mb-2">
              Innovating New Ways to Train Students
            </h1>
            <p class="text-black font-light text-sm md:text-xl">
              Every child has innate capabilities that help him/her shine. Our expert faculty provides the right guidance to bring out 
              these latent qualities, transforming the student into a successful individual.</p> 
            <p class="text-black font-light mt-2 text-sm md:text-xl">
              Sri Chaitanya syllabus is a unique one with
              an orientation of enabling the students take up to the task of getting selected for the student into a successful individual.Sri Chaitanya Syllabus is a unique one with
              and other Medical and Engineering Institutes and other streams with ease and other Medical and Engineering Institutes and other streams with ease and comfort.
            </p>
        </div>
      </div>

 <section class="bg-gray-100">
      <div class="max-w-7xl mx-auto px-6 sm:px-6 md:px-10 lg:px-20 py-5 flex flex-col md:flex-row items-center md:justify-between gap-8">        
        <!-- Left Content -->
        <div class="w-full md:w-1/2 md:text-left md:px-6 px-4">
            <h1 class="text-[1rem] md:text-[1.5rem] font-bold text-orange-400 ">
              Educational Approach
            </h1>
            <p class="text-black font-light mt-2 text-sm md:text-xl">
              The pattern of education in the higher sections of Bhashyam Academy has undergone a paradigm shift and 
              goes beyond the stipulated syllabus. 
            </p>  
            <p class="text-black font-light mt-2 text-sm md:text-xl">It provides a stress free education while preparing the students for
              future Engineering and Medical competitive examinations. For our Foundation students, Bhashyam has designed
              interactive and its practical based learning that includes group discussions, seminars and workshops. Several 
              projects are allotted to students in groups and they are asked to make their presentations in the classroom
               after completing their project.
            </p>
        </div>
        <div class="w-full md:w-1/2 flex justify-center md:justify-center">
          <img src="@/assets/seminar-designers.jpg" alt="Hero Image" class="w-full max-w-sm md:max-w-md h-auto object-cover rounded-lg" />
        </div>
      </div>
</section>
</section>

</template>

<script>
import axios from "axios";

export default {
  name: "Home",
  data() {
    return {
      categories: [],  // will be dynamically filled
      years: [],       // will be dynamically filled
      selectedCategory: "",
      selectedYear: "",
      gallery: [],
      filteredGallery: [],
    };
  },
  
  mounted() {
    this.fetchGallery();
  },
  methods: {
    fetchGallery() {
    axios
      .get("/api/method/school.api.homegallery.get_all_events")
      .then((res) => {
        // Convert main_image to full URL dynamically and convert year to number
        this.gallery = res.data.message.map(event => ({
          ...event,
          main_image: event.main_image
            ? event.main_image.startsWith("http")
              ? event.main_image
              : `${window.location.origin}${event.main_image}`
            : null,
          year: Number(event.year)
        }));

        this.filteredGallery = this.gallery;

        // Dynamically get unique categories
        const categorySet = new Set(this.gallery.map(event => event.category));
        this.categories = Array.from(categorySet);

        // Dynamically get last 4 years relative to current year
        const allYears = Array.from(new Set(this.gallery.map(event => event.year))).sort((a, b) => a - b);
        const currentYear = new Date().getFullYear();
        this.years = allYears
          .filter(y => y > currentYear - 5 && y <= currentYear) // last 4 years
          .sort((a, b) => a - b);
      })
      .catch((err) => console.error(err));
  },
    applyFilter() {
      this.filteredGallery = this.gallery.filter(
        (item) =>
          (this.selectedCategory ? item.category === this.selectedCategory : true) &&
          (this.selectedYear ? item.year === Number(this.selectedYear) : true)
      );
    },
    goToDetails(name) {
      this.$router.push({ name: "Details", params: {id: name } });
    },
  },
};
</script>
