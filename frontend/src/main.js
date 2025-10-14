import './index.css'
import './styles/main.scss'

import { createApp } from 'vue'
import router from './router'
import App from './App.vue'

// Frappe UI
import { Button, setConfig, frappeRequest, resourcesPlugin } from 'frappe-ui'

// FontAwesome
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faYoutube, faFacebook, faInstagram, faLinkedin } from '@fortawesome/free-brands-svg-icons'

// Add icons to library
library.add(faYoutube, faFacebook, faInstagram, faLinkedin)

// Create app
const app = createApp(App)

// Frappe UI config
setConfig('resourceFetcher', frappeRequest)
app.use(router)
app.use(resourcesPlugin)

// Register components
app.component('Button', Button)
app.component('font-awesome-icon', FontAwesomeIcon) // Register FontAwesome globally

// Mount app
app.mount('#app')
