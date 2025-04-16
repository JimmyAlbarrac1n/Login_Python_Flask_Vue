<template>
  <div class="container mt-4">
    <div class="row mb-4">
      <div class="col-md-8">
        <h2 class="mb-4">Listado de Usuarios</h2>
      </div>
      <div class="col-md-4 text-end">
        <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#createUserModal">
          <i class="bi bi-plus-circle"></i> Nuevo Usuario
        </button>
      </div>
    </div>

    <!-- Buscador de usuarios -->
    <div class="row mb-4">
      <div class="col-md-6">
        <div class="input-group">
          <input 
            type="text" 
            class="form-control" 
            placeholder="Buscar por nombre o email" 
            v-model="searchTerm"
          >
          <button class="btn btn-outline-secondary" type="button" @click="searchUsers">
            <i class="bi bi-search"></i> Buscar
          </button>
        </div>
      </div>
    </div>

    <!-- Tabla de usuarios -->
    <div class="card shadow-sm">
      <div class="card-body">
        <div v-if="loading" class="text-center py-5">
          <div class="spinner-border text-primary" role="status">
            <span class="visually-hidden">Cargando...</span>
          </div>
        </div>
        <div v-else-if="users.length === 0" class="alert alert-info">
          No se encontraron usuarios.
        </div>
        <div v-else class="table-responsive">
          <table class="table table-hover">
            <thead>
              <tr>
                <th>Nombre</th>
                <th>Apellido</th>
                <th>Email</th>
                <th>Acciones</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="user in users" :key="user._id">
                <td>{{ user.name }}</td>
                <td>{{ user.lastname }}</td>
                <td>{{ user.email }}</td>
                <td>
                  <div class="btn-group" role="group">
                    <button class="btn btn-sm btn-warning me-2" @click="editUser(user)">
                      <i class="bi bi-pencil-fill"></i> Editar
                    </button>
                    <button class="btn btn-sm btn-danger" @click="confirmDelete(user)">
                      <i class="bi bi-trash-fill"></i> Eliminar
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Modal para crear usuario -->
    <div class="modal fade" id="createUserModal" tabindex="-1" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Nuevo Usuario</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <save-usuarios @user-created="loadUsers" />
          </div>
        </div>
      </div>
    </div>

    <!-- Modal para editar usuario -->
    <div class="modal fade" id="editUserModal" tabindex="-1" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Editar Usuario</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <edit-usuarios 
              :user="selectedUser" 
              @user-updated="loadUsers" 
              v-if="selectedUser"
            />
          </div>
        </div>
      </div>
    </div>

    <!-- Modal de confirmación para eliminar -->
    <div class="modal fade" id="deleteConfirmModal" tabindex="-1" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Confirmar eliminación</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <p>¿Estás seguro de que deseas eliminar al usuario <strong>{{ selectedUser?.name }} {{ selectedUser?.lastname }}</strong>?</p>
            <p class="text-danger">Esta acción no se puede deshacer.</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
            <button type="button" class="btn btn-danger" @click="deleteUser">Eliminar</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SaveUsuarios from './SaveUsuarios.vue';
import EditUsuarios from './EditUsuarios.vue';
import UserService from '@/services/UserService';
import { Modal } from 'bootstrap';
import * as bootstrap from 'bootstrap';

export default {
  components: {
    SaveUsuarios,
    EditUsuarios
  },
  data() {
    return {
      users: [],
      filteredUsers: [],
      selectedUser: null,
      searchTerm: '',
      loading: true,
      editModal: null,
      deleteModal: null
    };
  },
  mounted() {
    this.loadUsers();
  },
  methods: {
    loadUsers() {
      this.loading = true;
      UserService.getUsers()
        .then(response => {
          this.users = response.data;
          this.filteredUsers = [...this.users];
          this.loading = false;
        })
        .catch(error => {
          console.error('Error al cargar usuarios:', error);
          this.loading = false;
        });
    },
    
    searchUsers() {
  if (!this.searchTerm.trim()) {
    this.users = this.filteredUsers; // Restaurar la lista completa
    return;
  }
  
  const term = this.searchTerm.toLowerCase();
  this.users = this.filteredUsers.filter(user => 
    user.name.toLowerCase().includes(term) || 
    user.email.toLowerCase().includes(term) ||
    user.lastname.toLowerCase().includes(term)
  );
    },
    userCreated(success, errorMessage) {
    // Cierra el modal correctamente
    const modalEl = document.getElementById('createUserModal');
    const modal = bootstrap.Modal.getInstance(modalEl);
    if (modal) modal.hide();
    
   
    setTimeout(() => {
      document.body.classList.remove('modal-open');
      document.querySelectorAll('.modal-backdrop').forEach(el => el.remove());
    }, 200);
    
    if (success) {
      alert('Usuario creado correctamente');
      this.loadUsers(); // Recargar la lista
    } else {
      alert(`Error al crear usuario: ${errorMessage || 'Error desconocido'}`);
    }
  },
    
    viewUser(id) {
      this.selectedUserId = id;
      this.viewModal = new Modal(document.getElementById('viewUserModal'));
      this.viewModal.show();
    },
    
    editUser(user) {
      this.selectedUser = { ...user };
      this.editModal = new Modal(document.getElementById('editUserModal'));
      this.editModal.show();
    },
    
    confirmDelete(user) {
      this.selectedUser = user;
      this.deleteModal = new Modal(document.getElementById('deleteConfirmModal'));
      this.deleteModal.show();
    },
    
    deleteUser() {
      if (this.selectedUser) {
        UserService.deleteUser(this.selectedUser._id)
          .then(() => {
            this.deleteModal.hide();
            this.loadUsers();
            this.showToast('Usuario eliminado correctamente');
          })
          .catch(error => {
            console.error('Error al eliminar usuario:', error);
          });
      }
    },
    
    showToast(message) {
      alert(message); 
    }
  }
};
</script>

<style scoped>
.table th, .table td {
  vertical-align: middle;
}
</style>