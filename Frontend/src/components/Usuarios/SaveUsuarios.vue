<template>
  <div>
    <form @submit.prevent="sendForm">
      <div class="mb-3">
        <label for="name" class="form-label">Nombre</label>
        <input 
          type="text" 
          class="form-control" 
          id="name" 
          v-model="user.name" 
          required
        >
      </div>
      
      <div class="mb-3">
        <label for="lastname" class="form-label">Apellido</label>
        <input 
          type="text" 
          class="form-control" 
          id="lastname" 
          v-model="user.lastname" 
          required
        >
      </div>
      
      <div class="mb-3">
        <label for="email" class="form-label">Email</label>
        <input 
          type="email" 
          class="form-control" 
          id="email" 
          v-model="user.email" 
          required
        >
      </div>
      
      <div class="mb-3">
        <label for="password" class="form-label">Contraseña</label>
        <input 
          type="password" 
          class="form-control" 
          id="password" 
          v-model="user.password" 
          required
        >
      </div>
      
      <div class="d-flex justify-content-end">
        <button type="submit" class="btn btn-primary" :disabled="loading">
          <span v-if="loading" class="spinner-border spinner-border-sm me-1" role="status" aria-hidden="true"></span>
          Guardar
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import UserService from '@/services/UserService';

export default {
  data() {
    return {
      user: {
        name: "",
        lastname: "",
        email: "",
        password: ""
      },
      loading: false
    };
  },
  methods: {
    async sendForm() {
      this.loading = true;
      
      try {
      await UserService.createUser(this.user);
      this.$emit('user-created', true); // Enviar true para indicar éxito
      this.resetForm();
    } catch (error) {
      console.error('Error:', error);
      this.$emit('user-created', false, error.message); // Enviar false y mensaje de error
    } finally {
      this.loading = false;
    }
    },
    
    resetForm() {
      this.user = { name: '', lastname: '', email: '', password: '' };
    }
  }
};
</script>