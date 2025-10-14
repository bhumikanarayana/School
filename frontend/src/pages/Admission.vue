<!-- <template>
  <div class="w-full pt-16">
    <!-- Banner -->
    <div class="w-full">
      <img 
        src="@/assets/admission.jpg" 
        alt="School life Banner" 
        class="w-full h-64 md:h-auto object-cover"
      />
    </div>

    <!-- Online Admission Form -->
    <div class="max-w-3xl mx-auto px-4 py-10">
      <h2 class="text-3xl font-bold text-center mb-8 text-gray-800">
        Online Admission
      </h2>

      <form @submit.prevent="submitAdmission" class="bg-white p-6 rounded-xl shadow-md space-y-6">
        <!-- Student Name -->
        <div>
          <label class="block text-gray-700 font-medium mb-1" for="name">Student Name</label>
          <input 
            type="text" 
            id="name" 
            v-model="form.student_name"
            placeholder="Enter student name"
            class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-orange-500"
            required
          />
        </div>

        <!-- Email -->
        <div>
          <label class="block text-gray-700 font-medium mb-1" for="email">Email</label>
          <input 
            type="email" 
            id="email" 
            v-model="form.email"
            placeholder="Enter email"
            class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-orange-500"
            required
          />
        </div>

        <!-- Phone Number -->
        <div>
          <label class="block text-gray-700 font-medium mb-1" for="phone">Phone Number</label>
          <input 
            type="tel" 
            id="phone" 
            v-model="form.phone_number"
            placeholder="Enter phone number"
            class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-orange-500"
            required
          />
        </div>

        <!-- Class / Grade -->
        <div>
          <label class="block text-gray-700 font-medium mb-1" for="class">Class / Grade</label>
          <select 
            id="class" 
            v-model="form.class_grade"
            class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-orange-500"
            required
          >
            <option value="">Select class</option>
            <option value="1">1st Grade</option>
            <option value="2">2nd Grade</option>
            <option value="3">3rd Grade</option>
            <option value="4">4th Grade</option>
            <option value="5">5th Grade</option>
          </select>
        </div>

        <!-- Submit Button -->
        <div class="mt-4">
          <button 
            type="submit" 
            :disabled="loading"
            class="w-full bg-orange-500 hover:bg-orange-600 text-white px-6 py-2 rounded-lg font-medium transition-colors flex items-center justify-center"
          >
            <span v-if="!loading">Submit</span>
            <span v-else class="flex items-center space-x-2">
              <svg class="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8H4z"></path>
              </svg>
              <span>Submitting...</span>
            </span>
          </button>
        </div>
      </form>
    </div>
  </div>
</template>   

<script>
export default {
  data() {
    return {
      form: {
        student_name: "",
        email: "",
        phone_number: "",
        class_grade: ""
      },
      loading: false
    };
  },
  methods: {
    async submitAdmission() {
      this.loading = true;

      try {
        await fetch(
          "http://127.0.0.1:8000/api/method/school.api.admission.submit_admission",
          {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(this.form)
          }
        );

        // Reset form after submission
        this.form.student_name = "";
        this.form.email = "";
        this.form.phone_number = "";
        this.form.class_grade = "";

        // Optionally refresh the page
        // location.reload();
      } catch (error) {
        console.error(error);
      } finally {
        this.loading = false;
      }
    }
  }
};
</script> --->
