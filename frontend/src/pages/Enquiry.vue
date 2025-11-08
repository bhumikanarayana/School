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
            />
            <p v-if="errors.name" class="text-red-500 text-sm mt-1">{{ errors.name }}</p>
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
            />
            <p v-if="errors.email" class="text-red-500 text-sm mt-1">{{ errors.email }}</p>
          </div>

          <!-- Phone -->
          <div>
            <label class="block mb-1 font-semibold text-gray-700">
              Phone Number (optional)
            </label>
            <input
              type="tel"
              v-model="form.phone"
              class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-orange-400"
              placeholder="Enter phone number"
            />
            <p v-if="errors.phone" class="text-red-500 text-sm mt-1">{{ errors.phone }}</p>
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
            ></textarea>
            <p v-if="errors.message" class="text-red-500 text-sm mt-1">{{ errors.message }}</p>
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
      errors: {
        name: "",
        email: "",
        phone: "",
        message: "",
      },
      success: false,
    };
  },
  methods: {
    validateForm() {
      this.errors = { name: "", email: "", phone: "", message: "" };
      let valid = true;

      // Name validation
      if (!this.form.name.trim()) {
        this.errors.name = "Name is required.";
        valid = false;
      } else if (this.form.name.length < 3) {
        this.errors.name = "Name must be at least 3 characters long.";
        valid = false;
      }

      // Email validation
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!this.form.email.trim()) {
        this.errors.email = "Email is required.";
        valid = false;
      } else if (!emailPattern.test(this.form.email)) {
        this.errors.email = "Please enter a valid email address.";
        valid = false;
      }

      // Phone validation (optional but must be valid if entered)
      const phonePattern = /^[0-9]{10}$/;
      if (this.form.phone && !phonePattern.test(this.form.phone)) {
        this.errors.phone = "Please enter a valid 10-digit phone number.";
        valid = false;
      }

      // Message validation
      if (!this.form.message.trim()) {
        this.errors.message = "Message is required.";
        valid = false;
      } else if (this.form.message.length < 10) {
        this.errors.message = "Message should be at least 10 characters.";
        valid = false;
      }

      return valid;
    },

    async submitForm() {
      if (!this.validateForm()) return;

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
