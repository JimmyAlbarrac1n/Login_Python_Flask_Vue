<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
      <div class="container">
        <a class="navbar-brand" href="#">
          <i class="bi bi-people-fill me-2"></i>
          Sistema CRUD de Usuarios
        </a>
      </div>
    </nav>
    
    <div class="container">
      <list-usuarios />
    </div>
    
    
  </div>
</template>

<script>
import ListUsuarios from './components/Usuarios/ListUsuarios.vue'

export default {
  name: 'App',
  components: {
    ListUsuarios
  }
}
</script>

<style>
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css");

body {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

#app {
  flex: 1;
  display: flex;
  flex-direction: column;
}

footer {
  margin-top: auto;
}
</style>