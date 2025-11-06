<template>
  <div class="w-full pt-16">
    <!-- Full-width Photo -->
    <div class="w-full">
      <img 
        src="@/assets/student.jpg" 
        alt="School life Banner" 
        class="w-full h-auto  object-cover"
      />
    </div>
<section class="bg-gray-100 ">
  <div class="max-w-7xl mx-auto px-6 sm:px-6 md:px-10 lg:px-20 pt-10 flex flex-col md:flex-row items-center md:justify-between gap-8">
    <!-- Right Image -->
    <div class="w-full md:w-5/12 flex justify-center md:justify-end">
      <img src="@/assets/gallery7.jpg" alt="Hero Image" class="w-full mx-auto max-w-sm md:max-w-md h-64 object-cover rounded-lg" />
    </div>
     <!-- Left Content -->
    <div class="w-full md:w-7/12 text-left mb-4 md:mb-0 md:pl-2">
      <h1 class="font-semibold mb-2 text-orange-500 text-3xl">Personality Development</h1>
      <p class= "text-black font-light mt-2 text-sm md:text-xl">
        A well-rounded personality is built on the back of all-round grooming. Being the
         future citizens of a diverse country, it is essential that these children uphold our
          rich cultural values.  
      </p>
      <p class="text-black font-light mt-2 text-sm md:text-xl">We endeavour to cultivate these values within our global learners
           through cultural meets, art competitions, music and dance competitions, and much more.
            At Sri Chaitanya, every child is given a platform to hone and enhance
         their talents, pursuing them simultaneously with academics.</p>
    </div>

  </div>
</section>
<section class="bg-gray-100">
  <div class="max-w-7xl mx-auto px-6 sm:px-6 md:px-10 lg:px-20 py-5 flex flex-col md:flex-row items-center md:justify-between gap-8">  
     <!-- Left Content -->
    <div class="w-full md:w-7/12 text-left mb-4 md:mb-0 md:pl-2">
      <h1 class="font-semibold mb-2 text-orange-500 text-3xl">Study Programme</h1>
      <p class="text-black font-light mt-2 text-sm md:text-xl">
        At Sri Chaitanya, we believe in a stress-free learning environment. To that end,
         our curriculum is specifically designed to lift the burden off students’ shoulders, 
         ensuring that learning is an interactive, is built on the back of all-round grooming engaging process. </p>
         <p class="text-black font-light mt-2 text-sm md:text-xl">Special emphasis is put 
         on effective and enjoyable methods of education (our digital learning initiatives are
          one such example) so that students become knowledgeable, inquisitive global learners.
      </p>
    </div>
     <!-- Right Image -->
    <div class="w-full md:w-5/12 flex justify-center md:justify-end">
      <img src="@/assets/gallery8.jpg" alt="Hero Image" class="w-full max-w-sm md:max-w-md h-64 mx-auto object-cover rounded-lg" />
    </div>

  </div>
</section>
<section class="bg-gray-100">
  <div class="max-w-7xl mx-auto px-6 sm:px-6 md:px-10 pb-10 lg:px-20 py-5 flex flex-col md:flex-row items-center md:justify-between gap-8">
    <!-- Right Image -->
    <div class="w-full md:w-5/12 flex justify-center md:justify-end">
      <img src="@/assets/gallery9.jpg" alt="Hero Image" class="w-full mx-auto max-w-sm md:max-w-md h-64 object-cover rounded-lg" />
    </div>
     <!-- Left Content -->
    <div class="w-full md:w-7/12 text-left mb-4 md:mb-0 md:pl-2">
      <h1 class="font-semibold mb-2 text-orange-500 text-3xl">Digital Learning</h1>
      <p class="text-black font-light mt-2 text-sm md:text-xl">
        To usher in a new era of world-class education, Sri Chaitanya has adopted a
         technology-driven approach to studies. The schools have replaced textbooks
          with trendy tabs for students from class five to seven. 
      </p>
      <p class="text-black font-light mt-2 text-sm md:text-xl">
      This learning 
          technique not only makes children adept in the use of technology but also 
          reduce the load of study materials to be carried every day.
      </p>
    </div>

  </div>
</section>
   </div>
</template>

<script>
import schoolBanner from '@/assets/school.jpg';
export default{
    name:"Schoollife"
}
</script>