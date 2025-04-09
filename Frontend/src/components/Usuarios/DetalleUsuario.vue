<template>
    <div>
      <div v-if="loading" class="text-center py-4">
        <div class="spinner-border text-primary" role="status">
        </div>
      </div>
      
      <div v-else-if="error" class="alert alert-danger">
        {{ error }}
      </div>
      
      <div v-else class="user-details">
        <div class="card border-0">
          <div class="card-body">
            <div class="text-center mb-4">
              <div class="avatar-placeholder bg-secondary text-white rounded-circle d-flex align-items-center justify-content-center mx-auto mb-3">
                {{ userInitials }}
              </div>
              <h4>{{ user.name }} {{ user.lastname }}</h4>
            </div>
            
            <div class="row mb-2">
              <div class="col-4 text-muted fw-bold">ID:</div>
              <div class="col-8">{{ user._id }}</div>
            </div>
            
            <div class="row mb-2">
              <div class="col-4 text-muted fw-bold">Nombre:</div>
              <div class="col-8">{{ user.name }}</div>
            </div>
            
            <div class="row mb-2">
              <div class="col-4 text-muted fw-bold">Apellido:</div>
              <div class="col-8">{{ user.lastname }}</div>
            </div>
            
            <div class="row mb-2">
              <div class="col-4 text-muted fw-bold">Email:</div>
              <div class="col-8">{{ user.email }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import UserService from '@/services/UserService';
  
  export default {
    props: {
      userId: {
        type: String,
        required: true
      }
    },
    data() {
      return {
        user: {},
        loading: true,
        error: null
      };
    },
    computed: {
      userInitials() {
        if (this.user && this.user.name && this.user.lastname) {
          return `${this.user.name.charAt(0)}${this.user.lastname.charAt(0)}`;
        }
        return '';
      }
    },
    mounted() {
      this.loadUserDetails();
    },
    methods: {
      loadUserDetails() {
        this.loading = true;
        UserService.getUserById(this.userId)
          .then(response => {
            this.user = response.data;
            this.loading = false;
          })
          .catch(error => {
            console.error('Error al cargar detalles del usuario:', error);
            this.error = 'No se pudo cargar la información del usuario';
            this.loading = false;
          });
      }
    }
  };
  </script>
  
  <style scoped>
  .avatar-placeholder {
    width: 80px;
    height: 80px;
    font-size: 1.5rem;
  }
  </style>