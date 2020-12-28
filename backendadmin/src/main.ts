import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { ElButton, ElSelect } from 'element-plus';

const app = createApp(App)

app.use(ElButton).use(ElSelect)

app.use(router).mount('#app')
