import Vuex from 'vuex'
import Vue from 'vue'
import axios from 'axios'

Vue.use(Vuex)

const url = 'http://localhost:8000/api/v1/transactions'

const store = new Vuex.Store({
    state: {
        transactions: []
    },
    getters: {
        allTransactions: (state) => state.transactions
    },
    actions: {
        getTransactions({commit}) {
            axios.get(url)
                .then(res => {
                    commit('SET_TRANSACTIONS', res.data)
                })
        },
        addTransaction({commit}, {text, amount}) {
            const config = {
                headers: {
                    'Content-Type': 'application/json'
                }
            }
            axios.post(url, {text: text, amount: amount}, config)
                .then(res => {
                    commit('ADD_TRANSACTION', res.data)
                })
                .catch(err => console.log(err))
        },
        deleteTransaction({commit}, {txnId}) {
            axios.delete(url, {id: txnId})
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
        ADD_TRANSACTION(state, transaction) {
            state.transactions.push(transaction)
        },
        DELETE_TRANSACTION(state, txnId) {
            let index = state.transactions.findIndex((i) => i.id === txnId)
            if(index > -1) {
                state.transactions.splice(index, 1)
            }
            
        }
    }
})

export default store