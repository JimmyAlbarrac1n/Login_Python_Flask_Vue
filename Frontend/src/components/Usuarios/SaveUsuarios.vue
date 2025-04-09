<template>
    <h1>Registrar usuarios</h1>
  
    <form @submit="sendForm">
      <input type="text" v-model="user.name" placeholder="Nombre" required>
      <input type="text" v-model="user.lastname" placeholder="Apellido" required>
      <input type="email" v-model="user.email" placeholder="Correo" required>
      <input type="password" v-model="user.password" placeholder="Contraseña" required>
  
      <button type="submit">Enviar</button>
    </form>
  </template>
  
  <script>
  export default {
    data() {
      return {
        user: {
          name: "",
          lastname: "",
          email: "",
          password: ""
        },
      };
    },
    methods: {
      sendForm(e) {
        e.preventDefault();
  
        fetch('http://127.0.0.1:5000/users', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.user)
        })
        .then(response => response.json())
        .then(data => {
          console.log(data);
          alert("Usuario creado correctamente!");
          this.resetForm();
        })
        .catch(error => {
          console.error('Error:', error);
        });
      },
  
      resetForm() {
        this.user = { name: '', lastname: '', email: '', password: '' };
      }
    }
  }
  </script>
  