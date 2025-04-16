import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import 'bootswatch/dist/lux/bootstrap.min.css' 
import 'bootstrap/dist/js/bootstrap.bundle.min.js'



axios.defaults.withCredentials = true

const app = createApp(App)
app.use(router)
app.use(store)
app.mount('#app')