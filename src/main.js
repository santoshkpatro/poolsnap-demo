import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'bootstrap/dist/css/bootstrap.min.css'

const app = createApp(App)
app.config.productionTip = false

app.use(store)
app.use(router)
app.mount('#app')
