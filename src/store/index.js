import Vuex from 'vuex'
import Vue from 'vue'
import axios from 'axios'
import router from '../router'

Vue.use(Vuex)

const url = 'http://localhost:8000/api/v1/'

const store = new Vuex.Store({
    state: {
        transactions: [],
        transaction: "",
        user: null,
        token: null
    },
    getters: {
        allTransactions: (state) => state.transactions,
        getTransaction: (state) => state.transaction
    },
    actions: {
        getTransactions({commit}, query) {
            const token = localStorage.getItem('token')
            const config = {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization' : `JWT ${token}`,
                }
            }
     
            return axios.get(`${url}transactions/?${query}`, config)
                .then(res => {
                    commit('SET_TRANSACTIONS', res.data)
                    // console.log(res.data)
                })
                .catch(err => console.log(err))
        },
        filterGetTransactions({commit}) {
            const token = localStorage.getItem('token')
            const config = {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization' : `JWT ${token}`,
                }
            }
            const today = new Date();
            const date = today.getFullYear() + '-' + (today.getMonth()+1) + '-' + today.getDate();

            return axios.get(`${url}transactions/?transaction_date=${date}`, config)
                .then(res => {
                    commit('SET_TRANSACTIONS', res.data)
                })
                .catch(err => console.log(err))
        },
        getTransaction({commit}, txnId) {
            const token = localStorage.getItem('token')
            const config = {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization' : `JWT ${token}`,
                }
            }
            return axios.get(`${url}transactions/${txnId}/`, config)
                .then(res => {
                    commit('SET_TRANSACTION', res.data)
                })
                .catch(err => console.log(err))
                
        },
        addTransaction({commit}, payload) {
            const token = localStorage.getItem('token')
            const config = {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization' : `JWT ${token}`,
                }
            }

            return axios.post(`${url}transactions/`, payload, config)
                .then(res => {
                    commit('ADD_TRANSACTION', res.data)
                })
                .catch(err => console.log(err))
        },
        editTransaction({commit}, payload) {
            const token = localStorage.getItem('token')
            
            const config = {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization' : `JWT ${token}`,
                }
            }

            return axios.put(`${url}transactions/${payload.id}/`, payload, config)
                .then(res => {
                    commit('EDIT_TRANSACTION', res.data)
                })
                .catch(err => {
                    console.log(err)
                })
        },
        deleteTransaction({commit}, txnId) {
            const token = localStorage.getItem('token')
            const config = {
                headers: {
                    'Authorization' : `JWT ${token}`,
                }
            }
            return axios.delete(`${url}transactions/${txnId}/`, config)
                .then(res => {
                    console.log(txnId)
                    commit('DELETE_TRANSACTION', txnId)
                })
                .catch(err => console.log(err))
        },
        registerUser({commit}, payload) {
            const config = {
                headers: {
                    'Content-Type': 'application/json',
                }
            }
            return axios.post(`${url}register/`, payload, config)
                .then(() => {
                    router.push('/login')
                })
                .catch(err => console.log(err))
        },
        loginUser({commit}, payload) {
            const config = {
                headers: {
                    'Content-Type': 'application/json',
                }
            }

            return axios.post(`${url}login/`, payload, config)
                .then((res => {
                    commit('SET_USER', payload)
                    commit('SET_TOKEN', res.data)
                    localStorage.setItem('user', JSON.stringify(payload));
                    localStorage.setItem('token', res.data.access)
                }))
                .then(() => {
                    router.push('/')
                })
                .catch(err => console.log(err))
        },
        logoutUser({commit}) {
            commit('LOGOUT_USER')
            localStorage.removeItem('user')
            localStorage.removeItem('token')

            router.push('/login')
        }
    },
    mutations: {
        SET_TRANSACTIONS(state, transactions) {
            state.transactions = transactions
        },
        SET_TRANSACTION(state, transaction) {
            state.transaction = transaction
        },
        ADD_TRANSACTION(state, transaction) {
            state.transactions.push(transaction)
        },
        DELETE_TRANSACTION(state, txnId) {
            let index = state.transactions.findIndex((i) => i.id === txnId)
            if(index > -1) {
                state.transactions.splice(index, 1)
            } 
        },
        EDIT_TRANSACTION(state, transaction) {
            let index = state.transactions.findIndex((i) => i.id === transaction.id)
            if(index > -1) {
                state.transactions[index] = transaction
            }
        },
        SET_USER(state, user) {
            state.user = user
        },
        SET_TOKEN(state, token) {
            state.token = token
        },
        LOGOUT_USER(state) {
            state.user = null
            state.token = null
        }
        
    }
})

export default store