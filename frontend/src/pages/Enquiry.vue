<template>
 <div class="w-full pt-16">
    <!-- Banner -->
    <div class="w-full">
      <img 
        src="@/assets/admission.jpg" 
        alt="School life Banner" 
        class="w-full h-64 md:h-auto object-cover"
      />
    </div>
  <div class="max-w-2xl mx-auto p-6  bg-white shadow-lg rounded-lg pt-16">
    <h2 class="text-2xl font-bold mb-6 text-center pt-5">Enquiry Form</h2>

    <form @submit.prevent="submitForm" class="space-y-4">
      <!-- Name -->
      <div>
        <label class="block mb-1 font-semibold">Name</label>
        <input
          type="text"
          v-model="form.name"
          class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-orange-400"
          required
        />
      </div>

      <!-- Email -->
      <div>
        <label class="block mb-1 font-semibold">Email</label>
        <input
          type="email"
          v-model="form.email"
          class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-orange-400"
          required
        />
      </div>

      <!-- Phone Number -->
      <div>
        <label class="block mb-1 font-semibold">Phone Number</label>
        <input
          type="tel"
          v-model="form.phone"
          class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-orange-400"
          required
        />
      </div>

      <!-- Message -->
      <div>
        <label class="block mb-1 font-semibold">Message</label>
        <textarea
          v-model="form.message"
          rows="4"
          class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-orange-400"
          required
        ></textarea>
      </div>

      <!-- Submit Button -->
      <div class="text-center">
        <button
          type="submit"
          class="bg-orange-500 hover:bg-orange-600 text-white font-semibold px-6 py-2 rounded-lg"
        >
          Submit Enquiry
        </button>
      </div>
    </form>

    <!-- Success message -->
    <p v-if="success" class="text-green-600 mt-4 text-center">
      Your enquiry has been submitted successfully!
    </p>
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
        // Call your Frappe API
        await axios.post("/api/method/school.api.admission.submit_admission", {
          student_name: this.form.name,
          email: this.form.email,
          phone_number: this.form.phone,
          message: this.form.message
        });

        this.success = true;
        this.form = { name: "", email: "", phone: "", message: "" }; // reset form
      } catch (err) {
        console.error("Failed to submit enquiry:", err);
        alert("Failed to submit enquiry. Please try again.");
      }
    },
  },
};
</script>