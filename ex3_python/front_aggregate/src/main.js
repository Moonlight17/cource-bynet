import { createApp } from 'vue'
import App from './App.vue'

import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"

import axios from 'axios'
import VueAxios from 'vue-axios'

import Datepicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'

import '@vueform/multiselect/themes/default.css'
import Multiselect from '@vueform/multiselect'

const app = createApp(App)
app.use(VueAxios, axios)

// eslint-disable-next-line
app.component('Datepicker', Datepicker);
app.component('MultiSelect', Multiselect);


app.mount('#app')

