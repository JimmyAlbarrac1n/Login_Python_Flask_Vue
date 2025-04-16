<template>
  <div class="dashboard">
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
      <div class="container">
        <a class="navbar-brand" href="#">
          <i class="bi bi-people-fill me-2"></i>
          Sistema CRUD de Usuarios
        </a>
        <div class="d-flex align-items-center">
          <span class="text-light me-3">Bienvenido, {{ user.name }} {{ user.lastname }}</span>
          <button @click="handleLogout" class="btn btn-danger">Cerrar Sesión</button>
        </div>
      </div>
    </nav>
    
    <div class="container">
      <list-usuarios />
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import ListUsuarios from './Usuarios/ListUsuarios.vue'

export default {
  name: 'DashboardPage',
  components: {
    ListUsuarios
  },
  computed: {
    ...mapState(['user'])
  },
  methods: {
    async handleLogout() {
      await this.$store.dispatch('logout')
      this.$router.push('/login')
    }
  }
}
</script>

<style scoped>
.dashboard {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.navbar {
  margin-bottom: 2rem;
}

.container {
  flex: 1;
}
</style> 