import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
