<template>
  <div id="app" class="app">
  <div class="header">
    <h1 >Hospital Homecare </h1>
    <nav>
      <button v-if="is_auth" v-on:click="loadHome"> Inicio </button>
      <button v-if="is_auth" v-on:click="logOut"> Cerrar Sesión </button>
      <button v-if="!is_auth" v-on:click="loadLogIn"> Iniciar Sesión </button>
      <button v-if="!is_auth" v-on:click="loadSignUp"> Registrarse </button>
      
    </nav>
  </div>
  <div>   
      <nav class="navbar navbar-expand "  style="background-color: #FF5733;">
        <div class="container-fluid">
        
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav  ">
            <li class="nav-item">
                <a class="nav-link" href="#" v-on:click="loadHome">Inicio</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#" v-on:click="loadPacientes">Pacientes</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#" v-on:click="loadEmpleados">Empleados</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#" v-on:click="loadSignos_vitales">Signos Vitales</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#" v-on:click="loadHistoria_clinica">Familiares</a>
            </li>
          </ul>
        </div>
      </div>
  </nav>
</div>
  <div class="main-component">
    <router-view
      v-on:completedLogIn="completedLogIn"
      v-on:completedSignUp="completedSignUp"
      v-on:logOut="logOut">
    
    </router-view>
    </div>


    <div class="footer">
    <h2>Misión TIC 2022</h2>
    </div>
    </div>

  </template>
  <script>
 export default {
  name: 'App',
  data: function () {
    return {
      is_auth: false

    }
  },
  components: {
  },
  methods: {
    verifyAuth: function () {
      this.is_auth = localStorage.getItem("isAuth") || false;

      if (this.is_auth == false)
        this.$router.push({ name: "logIn" });
      else
        this.$router.push({ name: "home" });

    },
    logOut: function () {
      localStorage.clear();
      alert("Sesión Cerrada");
      this.verifyAuth();
    },  
    loadHome: function () {
      this.$router.push({ name: "home" })
    },
    loadPacientes: function () {
      this.$router.push({ name: "pacientes" })
    },
    loadEmpleados: function () {
      this.$router.push({ name: "empleados" })
    },
    loadSignos_vitales: function () {
      this.$router.push({ name: "signos_vitales" })
    },
    loadHistoria_clinica: function () {
      this.$router.push({ name: "historia_clinica" })
    },
    loadLogIn: function () {
      this.$router.push({ name: "logIn" })
    },
    loadSignUp: function () {
      this.$router.push({ name: "signUp" })
    },
    
    completedLogIn: function (data) {
      localStorage.setItem("isAuth", true);
      localStorage.setItem("username", data.username);
      localStorage.setItem("token_access", data.token_access);
      localStorage.setItem("token_refresh", data.token_refresh);
      alert("Autenticación Exitosa");
      this.verifyAuth();
    },
    completedSignUp: function (data) {
      alert("Registro Exitoso");
      this.completedLogIn(data);
    },
  },
  created: function () {
    this.verifyAuth()
  }
}
</script>
<style>
  body {
    margin: 0 0 0 0;
   
  }
  .header{
    margin: 0%;
    padding: 0;
    width: 100%; height: 10vh;
    min-height: 100px;
    background-color: #E99E75;
    color:#E5E7E9 ;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
.header h1{
    width: 20%;
    text-align: center;
    color: #44426E;
;
}
.header nav {
  height: 100%;
  width: 20%;
  display: flex;
  justify-content: space-around;
  align-items: center;
  font-size: 20px;
}
.header nav button{
  color: #E5E7E9;
  background: #44426E;
;
  height: 100%;
  border: 1px solid #E5E7E9;
  border-radius: 5px;
  padding: 10px 20px;
}
.header nav button:hover{
  color: #776483;
  background: #E5E7E9;
  border: 1px solid #E5E7E9;
}
.main-component{
  height: 75vh;
  margin: 0%;
  padding: 0%;
  background: #FDFEFE ;
}
.footer{
  margin: 0;
  padding: 0;
  width: 100%;
  height: 10vh;
  min-height: 100px;
  background-color: #E99E75;
  color: #E5E7E9;
  }
.footer h2{
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
  