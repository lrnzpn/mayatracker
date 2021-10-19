import Vuex from 'vuex'
import Vue from 'vue'
import axios from 'axios'

Vue.use(Vuex)

const url = 'http://localhost:8000/api/v1/transactions/'

// const username = 'admin'
// const password = 'password'

const store = new Vuex.Store({
    state: {
        transactions: [],
        transaction: "",
        username: 'admin',
        password: 'password'
    },
    getters: {
        allTransactions: (state) => state.transactions,
        getTransaction: (state) => state.transaction
    },
    actions: {
        getTransactions({commit}) {
            const usernamePasswordBuffer = Buffer
                                            .from(this.state.username
                                                +':'+ this.state.password);
            const base64data = usernamePasswordBuffer.toString('base64');
            const config = {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Basic ${base64data}`,
                }
            }

            return axios.get(url, config)
                .then(res => {
                    commit('SET_TRANSACTIONS', res.data)
                })
                .catch(err => console.log(err))
        },
        getTransaction({commit}, txnId) {
            const usernamePasswordBuffer = Buffer
                                            .from(this.state.username
                                                +':'+ this.state.password);
            const base64data = usernamePasswordBuffer.toString('base64');
            const config = {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Basic ${base64data}`,
                }
            }
            return axios.get(url+`${txnId}/`, config)
                .then(res => {
                    commit('SET_TRANSACTION', res.data)
                })
                .catch(err => console.log(err))

        },
        addTransaction({commit}, payload) {
            const usernamePasswordBuffer = Buffer
                                            .from(this.state.username
                                                +':'+ this.state.password);
            const base64data = usernamePasswordBuffer.toString('base64');
            const config = {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Basic ${base64data}`,
                }
            }

            return axios.post(url, payload, config)
                .then(res => {
                    commit('ADD_TRANSACTION', res.data)
                })
                .catch(err => console.log(err))
        },
        editTransaction({commit}, payload) {
            const usernamePasswordBuffer = Buffer
                                            .from(this.state.username
                                                +':'+ this.state.password);
            const base64data = usernamePasswordBuffer.toString('base64');
            const config = {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Basic ${base64data}`,
                }
            }

            return axios.put(url+`${payload.id}/`, payload, config)
                .then(res => {
                    commit('EDIT_TRANSACTION', res.data)
                })
                .catch(err => {
                    console.log(err)
                })
        },
        deleteTransaction({commit}, txnId) {
            const usernamePasswordBuffer = Buffer
                                            .from(this.state.username
                                                +':'+ this.state.password);
            const base64data = usernamePasswordBuffer.toString('base64');
            return axios.delete(url + `${txnId}/`, {
                headers: {
                    'Authorization': `Basic ${base64data}`,
                },
            })
                .then(res => {
                    console.log(txnId)
                    commit('DELETE_TRANSACTION', txnId)
                })
                .catch(err => console.log(err))
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
        SET_USERNAME(state, username) {
            state.username = username
        },
        SET_PASSWORD(state, password) {
            state.password = password
        }
    }
})

export default store