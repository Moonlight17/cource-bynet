import { createApp } from 'vue'
import App from './App.vue'

import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"

import axios from 'axios'
import VueAxios from 'vue-axios'

import Datepicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'

const app = createApp(App)
app.use(VueAxios, axios)

// eslint-disable-next-line
app.component('Datepicker', Datepicker);


app.mount('#app')

