<template>
  <div class="w-full pt-16">
    <!-- Banner -->
    <div class="w-full">
      <img 
        src="@/assets/admission.jpg" 
        alt="School life Banner" 
        class="w-full h-auto object-cover"
      />
    </div>

    <!-- Enquiry Form Section -->
    <div class="max-w-3xl mx-auto p-6 pt-12">
      <div class="bg-gray-100 shadow-lg rounded-xl p-8 border border-gray-300">
        <h2 class="text-2xl font-bold mb-6 text-center text-black">Enquiry Form</h2>

        <form @submit.prevent="submitForm" class="space-y-5">
          <!-- Name -->
          <div>
            <label class="block mb-1 font-semibold text-gray-700">
              Name <span class="text-red-500">*</span>
            </label>
            <input
              type="text"
              v-model="form.name"
              class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-orange-400"
              required
            />
          </div>

          <!-- Email -->
          <div>
            <label class="block mb-1 font-semibold text-gray-700">
              Email <span class="text-red-500">*</span>
            </label>
            <input
              type="email"
              v-model="form.email"
              class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-orange-400"
              required
            />
          </div>

          <!-- Phone -->
          <div>
            <label class="block mb-1 font-semibold text-gray-700">Phone Number</label>
            <input
              type="tel"
              v-model="form.phone"
              class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-orange-400"
              required
            />
          </div>

          <!-- Message -->
          <div>
            <label class="block mb-1 font-semibold text-gray-700">
              Message <span class="text-red-500">*</span>
            </label>
            <textarea
              v-model="form.message"
              rows="4"
              class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-orange-400"
              required
            ></textarea>
          </div>

          <!-- Submit -->
          <div class="text-center">
            <button
              type="submit"
              class="bg-orange-500 hover:bg-orange-600 text-white font-semibold px-6 py-2 rounded-lg transition"
            >
              Submit Enquiry
            </button>
          </div>
        </form>

        <!-- Success Message -->
        <p v-if="success" class="text-green-600 mt-4 text-center">
          Your enquiry has been submitted successfully!
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "EnquiryForm",
  data() {
    return {
      form: {
        name: "",
        email: "",
        phone: "",
        message: "",
      },
      success: false,
    };
  },
  methods: {
    async submitForm() {
      try {
        await axios.post("/api/method/school.api.admission.submit_admission", {
          student_name: this.form.name,
          email: this.form.email,
          phone_number: this.form.phone,
          message: this.form.message,
        });
        this.success = true;
        this.form = { name: "", email: "", phone: "", message: "" };
      } catch (err) {
        console.error("Failed to submit enquiry:", err);
        alert("Failed to submit enquiry. Please try again.");
      }
    },
  },
};
</script>
