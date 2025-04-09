<template>
    <div>
      <h1>Listado de usuarios</h1>
        <save-usuarios/>

      <div v-for="user in users" :key="user._id">
        <p>{{ user.name }}</p>
        <p>{{ user.lastname }}</p>
        <p>{{ user.email }}</p>
      </div>
    </div>
  </template>
  
  <script>
  import SaveUsuarios from './SaveUsuarios.vue'
  export default {
    components: {
      SaveUsuarios
    },
    data() {
      return {
        users: [] 
      };
    },
    mounted() {
      fetch('http://127.0.0.1:5000/users')
        .then((response) => response.json())
        .then((response) => {
          this.users = response;  // se guarda directo
        });
    }
  };
  </script>
  