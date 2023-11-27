import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import { Button, Form, Select, InputNumber, DatePicker } from 'ant-design-vue';
import AppRouter from "./router";

createApp(App)
    .use(AppRouter)
    .use(Button)
    .use(Form)
    .use(Select)
    .use(InputNumber)
    .use(DatePicker)
    .mount('#app')
