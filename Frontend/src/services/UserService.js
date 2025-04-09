import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000';

class UserService {
  // Obtener todos los usuarios
  getUsers() {
    return axios.get(`${API_URL}/users`);
  }

  // Crear un nuevo usuario
  createUser(user) {
    return axios.post(`${API_URL}/users`, user);
  }

  // Actualizar un usuario existente
  updateUser(id, user) {
    return axios.put(`${API_URL}/users/${id}`, user);
  }

  // Eliminar un usuario
  deleteUser(id) {
    return axios.delete(`${API_URL}/users/${id}`);
  }
}

export default new UserService();