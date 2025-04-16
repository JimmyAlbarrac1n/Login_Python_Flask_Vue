import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from '../components/Login.vue'
import Dashboard from '../components/Dashboard.vue'
import store from '../store'

const routes = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginPage,
    meta: { requiresAuth: false }
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: { requiresAuth: true }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach(async (to, from, next) => {
  // Verificar si la ruta requiere autenticación
  if (to.meta.requiresAuth) {
    // Si el usuario no está autenticado, redirigir al login
    if (!store.state.isAuthenticated) {
      next('/login')
    } else {
      next()
    }
  } else {
    // Si el usuario está autenticado y trata de acceder al login, redirigir al dashboard
    if (to.path === '/login' && store.state.isAuthenticated) {
      next('/dashboard')
    } else {
      next()
    }
  }
})

export default router 