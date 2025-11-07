<template>
   <section class="w-full pt-16">
  <img 
    :src="bannerImg" 
    alt="Home Page Image" 
    class="w-full h-auto object-cover"
  />
  </section>
    <!-- About School Section -->
    <section class="bg-gray-50 py-6 px-6 md:px-20 text-center">
      <div class="max-w-4xl mx-auto">
        <h2 class="text-2xl md:text-4xl font-bold text-black mb-4">
          About Our School
        </h2>
        <p class="text-gray-700 text-sm md:text-lg font-light leading-relaxed mb-6">
          Our institution is dedicated to nurturing young minds by providing a strong foundation
          in academics, discipline, and values. With an experienced faculty and a focus on holistic
          development, we ensure every student grows with confidence and curiosity. Our goal is to
          create responsible citizens who are ready to face the challenges of tomorrow.
        </p>

        <!-- Centered Button -->
       <a
        href="http://127.0.0.1:8000/studentadmission"
          class="bg-orange-500 hover:bg-black hover:text-white text-white px-3 py-2 text-sm  md:px-4 md:py-2 rounded-xl shadow-md transition duration-300"
        >
          Register Now
        </a>
      </div>
    </section>
    <section class="bg-gray-100 py-4">
          <div class="max-w-7xl mx-auto px-6 sm:px-6 md:px-10  lg:px-20 py-5 flex flex-col md:flex-row items-center md:justify-between gap-4">   
          <div class="w-full md:w-5/12 flex justify-center md:justify-end">
              <img :src="aboutImg" alt="Hero Image" class="w-full max-w-sm md:max-w-md h-auto object-cover rounded-lg" />
            </div>     
            <!-- Left Content -->
            <div class="w-full md:w-7/12 md:text-left md:px-6 ">
                <h1 class="text-[1rem] md:text-[1.5rem] font-bold text-orange-500">
                  Management
                </h1>
                <p class="text-black font-light">
                  Sri chaitanya Junior College was founded in the year 1991. has since grown across geographies and is now present not only in Telangana, but also in Andhrapradesh & Karnataka. 
                provide quality education right from playgroup and kindergarten.</p>
                <p class="text-black font-light mt-2 text-sm md:text-xl">Bhashyam has designed
                  interactive and its practical based learning that includes group discussions, seminars and workshops. Several 
                  projects are allotted to students in groups and they are asked to make their presentations in the classroom
                  after completing their project.
                </p>
            </div>
          
          </div>
    </section>
     
    <section
      class="relative w-full h-[400px] md:h-[500px] bg-cover bg-center flex items-center justify-start"
      :style="{ backgroundImage: `url(${student4})` }"
      >

      <!-- Overlay for dark effect (optional) -->
      <div class="absolute inset-0 bg-black bg-opacity-50"></div>

      <!-- Content on top of image -->
      <div class="z-10 text-white px-6  text-left">
        <h2 class="text-2xl md:text-4xl font-bold mb-4">Our Vision & Mission</h2>
        <p class="text-sm md:text-lg  max-w-2xl mx-auto mb-6">
          Discipline is the cornerstone of our school’s philosophy. We believe that true learning flourishes in an environment of order, respect, and responsibility. Every student is 
          guided to maintain self-control, punctuality, and commitment to their studies and behavior. Through regular mentoring, value-based education, and a structured daily routine, we help our 
          students develop good habits that extend beyond the classroom. Our aim is not just to enforce discipline, but to inspire students to understand its importance in achieving success and building strong character.
        </p>

        <!-- Button -->
        <a href="/login" class="bg-orange-500 hover:bg-black text-white text-sm font-semibold px-6 py-2 rounded-lg transition duration-300">
          Learn More
        </a>
      </div>
    </section>

    <section class="bg-gray-100">
      <div class="max-w-7xl mx-auto px-6 sm:px-6 md:px-10 lg:px-20 py-5 flex flex-col md:flex-row items-center md:justify-between gap-8">        
        <!-- Left Content -->
        <div class="w-full md:w-7/12 md:text-left md:px-8">
            <h1 class="text-[1rem] md:text-[1.5rem] font-bold text-orange-500 ">
              Who We Are
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
        <div class="w-full md:w-5/12 flex justify-center md:justify-end">
          <img src="@/assets/seminar-designers.jpg" alt="Hero Image" class="w-full max-w-sm md:max-w-md h-auto object-cover rounded-lg" />
        </div>
      </div>
</section>
</template>

<script>
import bannerImg from '@/assets/aboutus.jpg'
import aboutImg from '@/assets/manage.jpg'
import managementImg from '@/assets/management.jpg'
import student4 from '@/assets/student4.jpg'

export default {
  name: "Aboutus",
  data() {
    return { bannerImg, aboutImg, managementImg, student4 }
  }
}
</script>

<style scoped>
/* optional styling */
</style>