import { createApp } from 'vue'
import App from './App.vue'

// import
import PrimeVue from 'primevue/config';

//theme
import "primevue/resources/themes/lara-light-indigo/theme.css";
//core
import "primevue/resources/primevue.min.css";
import 'primeicons/primeicons.css';

// para navegacion
//import VueRouter from 'vue-router'
import { createRouter, createWebHistory  } from 'vue-router';


// cada componente se importa de forma separada +++++++++++++++++++++++++
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';   // optional
import Row from 'primevue/row';
import Button from "primevue/button";
import Menu from 'primevue/menu';
import Splitter from 'primevue/splitter';
import SplitterPanel from 'primevue/splitterpanel';
import Menubar from 'primevue/menubar';
import Avatar from 'primevue/avatar';
import AutoComplete from 'primevue/autocomplete';
import Dialog from 'primevue/dialog';
import InputText from 'primevue/inputtext';
import Calendar from 'primevue/calendar';
import Password from 'primevue/password';
import FileUpload from 'primevue/fileupload';
import Dropdown from 'primevue/dropdown';
import RadioButton from 'primevue/radiobutton';
import Card from 'primevue/card';


const app = createApp(App);
app.use(PrimeVue);


// aqui agregamos el componente ******************************************
app.component('Button', Button);
app.component('DataTable', DataTable);
app.component('Column', Column);
app.component('Menu', Menu);
app.component('Menubar', Menubar);
app.component('Splitter', Splitter);
app.component('SplitterPanel', SplitterPanel);
app.component('Row', Row);
app.component('Avatar', Avatar);
app.component('AutoComplete', AutoComplete);
app.component('Dialog', Dialog);
app.component('InputText', InputText);
app.component('Calendar', Calendar);
app.component('Password', Password);
app.component('FileUpload', FileUpload);
app.component('Dropdown', Dropdown);
app.component('RadioButton', RadioButton);
app.component('Card', Card);

import Login from './components/LogIn'
import AdminiCom from './components/AdminiCom'
import AdminComConf from './components/AdminComConf'
import AdminComCofPass from './components/AdminComCofPass'
import AdminComUF from './components/AdminComUF'
import AdminComUAT from './components/AdminiComUAT'
import AdminComUPT from './components/AdminComUPT'
import AdminComUADT from './components/AdminComUADT'
import AdminComC from './components/AdminComC'
import AdminComCF from './components/AdminComCF'
import AdminCompSal from './components/AdminCompSal'
import AdminCompMat from './components/AdminCompMat'
import AdminCompAsis from './components/AdminCompAsis'
import AdminCompJus from './components/AdminComJus'

import ProfesorCom from './components/ProfesorCom'
import ProfComConf from './components/ProfComConf'
import ProfComCofPass from './components/ProfComCofPass'
import AlumnoCom from './components/AlumnoCom'
import AlumComConf from './components/AlumComConf'
import AlumComCofPass from './components/AlumComCofPass'
import AlumComUAT from './components/AlumComUAT'
import AlumComUJT from './components/AlumComUJT'
import AlumComPart from './components/AlumComPart'

const routes = [
    { path: '/', component: Login },
    { path: '/admin', component: AdminiCom },
    { path: '/admin/config', component: AdminComConf },
    { path: '/admin/config/password', component: AdminComCofPass },
    { path: '/admin/adduser', component: AdminComUF },
    { path: '/admin/alumnos', component: AdminComUAT },
    { path: '/admin/profesores', component: AdminComUPT },
    { path: '/admin/administradores', component: AdminComUADT },
    { path: '/admin/cursos/add', component: AdminComCF },
    { path: '/admin/cursos', component: AdminComC },
    { path: '/admin/salon', component: AdminCompSal },
    { path: '/admin/matricula', component: AdminCompMat },
    { path: '/admin/asistencia', component: AdminCompAsis },
    { path: '/admin/justificaciones', component: AdminCompJus },

    { path: '/prof', component: ProfesorCom },
    { path: '/prof/config', component: ProfComConf },
    { path: '/prof/config/password', component: ProfComCofPass },
    { path: '/alum', component: AlumnoCom },
    { path: '/alum/config', component: AlumComConf },
    { path: '/alum/config/password', component: AlumComCofPass },
    { path: '/alum/asis', component: AlumComUAT },
    { path: '/alum/just', component: AlumComUJT },
    { path: '/alum/part', component: AlumComPart },
  ]

const router = createRouter({
    // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
    history: createWebHistory (),
    routes, // short for `routes: routes`
})

app.use(router)

app.mount("#app")

