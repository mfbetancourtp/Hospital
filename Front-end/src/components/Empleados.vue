<template>
    
    <div class="container">

        <div class="row">
            <div class="col">
                <h2>CREAR</h2>
                <form v-on:submit.prevent="processCreate">
                    <input type="text" class="form-control" v-model="elementP.nombres" placeholder="Nombres" />
                    <br />
                    <input type="text" class="form-control" v-model="elementP.apellidos" placeholder="Apellidos" />
                    <br />
                    <input type="text" class="form-control" v-model="elementP.cedula" placeholder="Cédula" />
                    <br />
                    <input type="text" class="form-control" v-model="elementP.correo" placeholder="Correo" />
                    <br />
                    <input type="text" class="form-control" v-model="elementP.celular" placeholder="Celular" />
                    <br />
                    <input type="text" class="form-control" v-model="elementP.direccion" placeholder="Dirección" />
                    <br />
                    <input type="text" class="form-control" v-model="elementP.cargo" placeholder="Cargo" />
                    <br />
                    <input type="text" class="form-control" v-model="elementP.contrasena" placeholder="Contraseña" />
                    <br />
                    <button type="submit" class="btn btn-primary">Crear</button>
                </form>
            </div>
            <div class="col">
            <h2>CONSULTAR</h2>
            <form v-on:submit.prevent="processGetProduct">
                <input type="text" class="form-control" v-model="elementP.id" placeholder="Ingrese Id del empleado" />
                <br />
                <p style="text-align: center">
                <span> {{ onlyOneP.nombres }} </span>
                <br />
                <span> {{ onlyOneP.apellidos }} </span>
                <br />
                <span> {{ onlyOneP.cedula }} </span>
                <br />
                <span> {{ onlyOneP.correo }} </span>
                <br />
                <span> {{ onlyOneP.celular }} </span>
                <br />
                <span> {{ onlyOneP.direccion }} </span>
                <br />
                <span> {{ onlyOneP.cargo }} </span>
                <br />
                <span> {{ onlyOneP.contrasena }} </span>
                </p>
                <br />
                <button type="submit" class="btn btn-primary">CONSULTAR</button>
            </form>
            </div>
            <div class="col">
            <h2>ACTUALIZAR</h2>
            <form v-on:submit.prevent="processUpgrade">
                <input type="number" class="form-control" v-model="elementP.id" placeholder="Ingrese Id del empleado" />
                <br />
                <input type="text" class="form-control" v-model="elementP.nombres" placeholder="Nombres" />
                <br />
                <input type="text" class="form-control" v-model="elementP.apellidos" placeholder="Apellidos" />
                <br />
                <input type="text" class="form-control" v-model="elementP.cedula" placeholder="Cédula" />
                <br />
                <input type="text" class="form-control" v-model="elementP.correo" placeholder="Correo" />
                <br />
                <input type="text" class="form-control" v-model="elementP.celular" placeholder="Celular" />
                <br />
                <input type="text" class="form-control" v-model="elementP.direccion" placeholder="Dirección" />
                <br />
                <input type="text" class="form-control" v-model="elementP.cargo" placeholder="Cargo" />
                <br />
                <input type="text" class="form-control" v-model="elementP.contrasena" placeholder="Contraseña" />
                <br />
                <br />
                <button type="submit" class="btn btn-primary">MODIFICAR</button>
            </form>
            </div>
            <div class="col">
            <h2>BORRAR</h2>
            <form v-on:submit.prevent="processDelete">
                <input type="text" class="form-control" v-model="elementP.id" placeholder="Ingrese Id del empleado"/>
                <br />
                <br />
                <button type="submit" class="btn btn-primary">BORRAR</button>
            </form>
            </div>
        </div>
    </div>
    <br />
    <br />
    <button class="btn btn-secondary" v-on:click="processData">ACTUALIZAR TABLA</button>
    <table class="table">
        <thead>
            <tr>
                <th>Nombres</th>
                <th>Apellidos</th>
                <th>Cédula</th>
                <th>Correo</th>
                <th>Celular</th>
                <th>Dirección</th>
                <th>Cargo</th>
                <th>Contraseña</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="product in products" :key="empleados.id">
                <td>{{ empleados.nombres }}</td>
                <td>{{ empleados.apellidos }}</td>
                <td>{{ empleados.cedula }}</td>
                <td>{{ empleados.correo }}</td>
                <td>{{ empleados.celular }}</td>
                <td>{{ empleados.direccion }}</td>
                <td>{{ empleados.cargo }}</td>
                <td>{{ empleados.contrasena }}</td>
            </tr>
        </tbody>
    </table>
  </template>
<script>
    import axios from "axios";
    export default {
    name: "Empleados",
    data: function () {
      return {
        username: localStorage.getItem("username") || "none",
        products: [],
        elementP: {
          nombres: "",
          apellidos: "",
          cedula: "",
          correo: "",
          celular: "",
          direccion: "",
          cargo: "",
          contrasena: "",
        },
        onlyOneP: {
          nombres: "",
          apellidos: "",
          cedula: "",
          correo: "",
          celular: "",
          direccion: "",
          cargo: "",
          contrasena: "",
        },
      };
    },
    methods: {
      processData: function () {
        axios
          .get("http://127.0.0.1:8000/empleado/", {
            headers: {},
          })
          .then((result) => {
            console.log(result.data);
            this.products = result.data;
          })
          .catch((error) => {
            alert(error);
          });
      },
      processCreate: function () {
        axios
          .post(
            "http://127.0.0.1:8000/empleado/",
            this.elementP,
            {
              headers: {},
            }
          )
          .then((result) => {
            alert(result.status + " Creado exitosamente..");
          })
          .catch((error) => {
            alert(error);
          });
      },
      processGetProduct: function () {
        axios
          .get(
            `http://127.0.0.1:8000/empleado/${this.elementP.id}`,
            this.elementP,
            {
              headers: {},
            }
          )
          .then((result) => {
            this.onlyOneP.name = result.data.name;
            this.onlyOneP.price = result.data.price;
          })
          .catch((error) => {
            alert(error);
          });
      },
      processUpgrade: function () {
        axios
          .put(
            `http://127.0.0.1:8000/empleado/${this.elementP.id}`,
            this.elementP,
            {
              headers: {},
            }
          )
          .then((result) => {
            alert(result.status + " Actualizado exitosamente..");
          })
          .catch((error) => {
            alert(error);
          });
      },
      processDelete: function () {
        axios
          .delete(
            `http://127.0.0.1:8000/empleado/${this.elementP.id}`,
            {
              headers: {},
            }
          )
          .then((result) => {
            alert(result.status + " Borrado exitosamente..");
          })
          .catch((error) => {
            alert(error);
          });
      },
    },
    created: function () {
      this.processData();
    },
    };
    </script>
<style>
h1 {
    font-size: 50px;
    color: #283747;
}

span {
    color: crimson;
    font-weight: bold;
}
</style>