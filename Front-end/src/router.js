import { createRouter, createWebHistory } from "vue-router";
import App from './App.vue';
import LogIn from './components/LogIn.vue'
import SignUp from './components/SignUp.vue'
import Home from './components/Home.vue'
import Pacientes from './components/Pacientes.vue'
import Empleados from './components/Empleados.vue'
import Historia_Clinica from './components/Historia_Clinica.vue'
import Signos_Vitales from './components/Signos_Vitales.vue'

const routes = [{
path: '/',
name: 'root',
component: App
},
{
path: '/user/logIn',
name: "logIn",
component: LogIn
},
{
path: '/user/signUp',
name: "signUp",
component: SignUp
},
{
  path: '/user/Home',
  name: "home",
  component: Home
},
{
  path: '/user/Pacientes',
  name: "pacientes",
  component: Pacientes
},
{
  path: '/user/Empleados',
  name: "empleados",
  component: Empleados
},
{
  path: '/user/Pacientes',
  name: "pacientes",
  component: Pacientes
},
{
  path: '/user/Signos_Vitales',
  name: "signos_vitales",
  component: Signos_Vitales
},{
  path: '/user/Historia_Clinica',
  name: "historia_clinica",
  component: Historia_Clinica
},

];
const router = createRouter({
  history: createWebHistory(),
  routes,
  });
  export default router
