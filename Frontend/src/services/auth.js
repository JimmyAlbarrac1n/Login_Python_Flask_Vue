import axios from 'axios'

const API_URL = 'http://localhost:5000'

export default {
    async login(email, password) {
        try {
            const response = await axios.post(`${API_URL}/login`, {
                email,
                password
            })
            return response.data
        } catch (error) {
            throw error.response.data
        }
    },

    async logout() {
        try {
            const response = await axios.post(`${API_URL}/logout`)
            return response.data
        } catch (error) {
            throw error.response.data
        }
    },

    async checkAuth() {
        try {
            const response = await axios.get(`${API_URL}/check-auth`)
            return response.data
        } catch (error) {
            throw error.response.data
        }
    }
} 