import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/Home.vue'),
  },
  
  {
    path: '/contactus',
    name: 'Contactus',
    component: () => import('@/pages/Contactus.vue'),
  },
   
  {
    path: '/aboutus',
    name: 'Aboutus',
    component: () => import('@/pages/Aboutus.vue'),
  },
  
  {
    path: '/announcements',
    name: 'Announcements',
    component: () => import('@/pages/Announcements.vue'),
  },
  
  {
    path: '/gallery',
    name: 'Gallery',
    component: () => import('@/pages/Gallery.vue'),
  },

  {
    path: '/schoollife',
    name: 'Schoollife',
    component: () => import('@/pages/Schoollife.vue'),
  },

  { 
    path: "/details/:id",
    name: "Details",
    component: () => import('@/pages/Details.vue'),
  },

  {
  path: "/announcement-details/:name",
  name: "AnnouncementDetails",
  component: () => import('@/pages/AnnouncementDetails.vue'),
  },
  { 
  path: '/enquiry', 
  name: 'Enquiry', 
  component: () => import('@/pages/Enquiry.vue')
 },

]

let router = createRouter({
  history: createWebHistory('/frontend'),
  routes,
   scrollBehavior() {
    return { top: 0 }  // always scroll to top on navigation
  }
})

export default router
