# Sistema de Gestión de Usuarios con Login

Este proyecto es un sistema de gestión de usuarios que incluye un sistema de autenticación y un CRUD completo. Está desarrollado con Vue.js en el frontend y Flask con MongoDB en el backend.

## Características Principales

- **Sistema de Login**: Autenticación de usuarios con email y contraseña
- **CRUD de Usuarios**: 
  - Crear nuevos usuarios
  - Leer lista de usuarios
  - Actualizar información de usuarios
  - Eliminar usuarios
- **Búsqueda de Usuarios**: Filtrado por nombre, apellido o email
- **Interfaz Responsiva**: Diseño adaptativo usando Bootstrap

## Tecnologías Utilizadas

### Frontend
- Vue.js 3
- Vue Router
- Vuex
- Axios
- Bootstrap 5
- Bootstrap Icons

### Backend
- Python 3
- Flask
- PyMongo
- MongoDB


## Configuración

1. Asegúrate de tener MongoDB instalado y corriendo en tu sistema
2. Configura la conexión a MongoDB en `Backend/src/app.py`:
```python
app.config["MONGO_URI"] = "mongodb://localhost:27017/python-flask-vuejs"
```

## Ejecución

1. Iniciar el Backend:
```bash
cd Backend/src
python app.py
```

2. Iniciar el Frontend:
```bash
cd Frontend
npm run serve
```

3. Acceder a la aplicación:
- Frontend: http://localhost:8080
- Backend: http://localhost:5000

## Uso

1. Inicia sesión con tus credenciales
2. Una vez autenticado, serás redirigido al dashboard
3. En el dashboard podrás:
   - Ver la lista de usuarios
   - Crear nuevos usuarios
   - Editar usuarios existentes
   - Eliminar usuarios
   - Buscar usuarios por nombre, apellido o email
