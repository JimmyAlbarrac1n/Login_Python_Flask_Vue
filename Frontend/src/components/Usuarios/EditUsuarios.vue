<template>
    <div>
      <form @submit.prevent="updateUser">
        <div class="mb-3">
          <label for="name" class="form-label">Nombre</label>
          <input 
            type="text" 
            class="form-control" 
            id="name" 
            v-model="userForm.name" 
            required
          >
        </div>
        
        <div class="mb-3">
          <label for="lastname" class="form-label">Apellido</label>
          <input 
            type="text" 
            class="form-control" 
            id="lastname" 
            v-model="userForm.lastname" 
            required
          >
        </div>
        
        <div class="mb-3">
          <label for="email" class="form-label">Email</label>
          <input 
            type="email" 
            class="form-control" 
            id="email" 
            v-model="userForm.email" 
            required
          >
        </div>
        
        <div class="mb-3">
          <label for="password" class="form-label">Contraseña</label>
          <input 
            type="password" 
            class="form-control" 
            id="password" 
            v-model="userForm.password" 
            placeholder="Deja en blanco para mantener la actual"
          >
          
        </div>
        
        <div class="d-flex justify-content-end gap-2">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
            Cancelar
          </button>
          <button type="submit" class="btn btn-primary" :disabled="loading">
            <span v-if="loading" class="spinner-border spinner-border-sm me-1" role="status" aria-hidden="true"></span>
            Actualizar
          </button>
        </div>
      </form>
    </div>
  </template>
  
  <script>
  import UserService from '@/services/UserService';
  import { Modal } from 'bootstrap';
  
  export default {
    props: {
      user: {
        type: Object,
        required: true
      }
    },
    data() {
      return {
        userForm: {
          name: '',
          lastname: '',
          email: '',
          password: ''
        },
        loading: false
      };
    },
    created() {
      // Copiar los valores del usuario a editar
      this.userForm = { 
        name: this.user.name,
        lastname: this.user.lastname,
        email: this.user.email,
        password: '' // No mostramos la contraseña actual por seguridad
      };
    },
    methods: {
      async updateUser() {
        this.loading = true;
        
        try {
          // Si no se proporciona contraseña, necesitamos obtener la actual
          if (!this.userForm.password) {
            const currentUser = await UserService.getUserById(this.user._id);
            this.userForm.password = currentUser.data.password;
          }
          
          await UserService.updateUser(this.user._id, this.userForm);
          
          // Cerrar el modal
          const modalElement = document.getElementById('editUserModal');
          const modal = Modal.getInstance(modalElement);
          modal.hide();
          
          // Emitir evento para que se actualice la lista
          this.$emit('user-updated');
          
          // mensaje de éxito
          alert('Usuario actualizado correctamente');
        } catch (error) {
          console.error('Error al actualizar usuario:', error);
          alert('Error al actualizar el usuario');
        } finally {
          this.loading = false;
        }
      }
    }
  };
  </script>