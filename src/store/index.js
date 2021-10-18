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
        }
    },
    mutations: {
        SET_TRANSACTIONS(state, transactions) {
            state.transactions = transactions
        }
    }
})

export default store