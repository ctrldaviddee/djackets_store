import './assets/main.css'
import 'primeicons/primeicons.css'
// import toast from 'vue-toastification'
// import 'vue-toastification/dist/index.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { autoAnimatePlugin } from '@formkit/auto-animate/vue'
// import axios from 'axios'

import App from './App.vue'
import router from './router'

// axios.defaults.baseURL = 'http://127.0.0.1:8000/'

const app = createApp(App)

app.use(createPinia())
app.use(router, autoAnimatePlugin, /*axios*/)
// app.use(toast)
app.use()

app.mount('#app')
