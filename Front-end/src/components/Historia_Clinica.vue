<template>
    <div>
        <h1> Registro Familiares</h1>
    </div>
        <div class="row align-items-start" style="background-color: #BBAAB8; border-color: 5px solid #000 ;">
        <div class="col">
        
         
        <form v-on:submit.prevent="processCreate" style="width: 50%; ">
                    <p>id Familia</p>
                    <input type="number" class="form-control" v-model="elementP.name" placeholder="id Familiar">
                  
                    <p>Nombres</p>
                    <input type="tex" class="form-control" placeholder="Nombres">
                
                    <p>Apellidos</p>
       
                    <input type="tex" class="form-control"  placeholder="Apellidos">                
                    <p>Celular</p>
                    <input type="number" class="form-control"  placeholder="Celular">              
                    <p>Email</p>
                    <input type="tex" class="form-control" placeholder="Email">
                    <p>Genero</p>
                    <input type="tex" class="form-control"  placeholder="Genero">
                    <p>Parentesco</p>
                    <input type="tex" class="form-control"  placeholder="Parentesco">
                    <p>id_paciente</p>
                    <input type="number" class="form-control"  placeholder="id_paciente">
           <br>
                    <button type="submit" class="btn btn-primary">Crear</button>
                </form>
        </div>
 
        </div>
   
</template>

<script>
import axios from "axios";
export default {
    name: "Products",
    data: function () {
        return {
            username: localStorage.getItem("username") || "none",
            products: [],
            elementP: {
                idfamiliar: "",
                name: "",
                lastname: "",
                celular:0,
                email:"",
                genero:"",
                parentesco:"",
                id_paciente:"",


            },
            onlyOneP: {
                name: "",
                price: 0,
            }
        };
    }
}

</script>
<style>

.footer{
display: none;
  }

</style>
