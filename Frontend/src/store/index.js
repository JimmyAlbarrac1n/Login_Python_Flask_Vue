import { createStore } from 'vuex'
import authService from '../services/auth'

export default createStore({
  state: {
    user: null,
    isAuthenticated: false
  },
  mutations: {
    setUser(state, user) {
      state.user = user
      state.isAuthenticated = true
    },
    clearUser(state) {
      state.user = null
      state.isAuthenticated = false
    }
  },
  actions: {
    async checkAuth({ commit }) {
      try {
        const response = await authService.checkAuth()
        if (response.authenticated) {
          commit('setUser', response.user)
        }
      } catch (error) {
        commit('clearUser')
      }
    },
    async logout({ commit }) {
      try {
        await authService.logout()
        commit('clearUser')
      } catch (error) {
        console.error('Error al cerrar sesión:', error)
      }
    }
  }
}) 