<template>
  <div>
    
    <b-navbar variant="faded" type="light">
      <b-navbar-brand tag="h1" class="mb-0">Welcome, {{ username }}!</b-navbar-brand>
      <b-navbar-nav class="ms-auto">
        <b-btn @click="logout" variant="outline-primary">Logout</b-btn>
      </b-navbar-nav>
    </b-navbar>

    <Header />
    <b-modal 
      id="modal-add" 
      title="Add new transaction"
      hide-footer
      >
      <AddTransaction />
    </b-modal>
    <Balance />
    <IncomeExpenses />
    <b-button 
      v-b-modal.modal-add 
      block 
      class="btn-new">New Transaction</b-button>
    <TransactionList />
    
  </div>
</template>

<script>
import Header from '../components/Header.vue'

import Balance from '../components/Balance.vue'
import IncomeExpenses from '../components/IncomeExpenses.vue'
import AddTransaction from '../components/AddTransaction.vue'
import TransactionList from '../components/TransactionList.vue'

export default {
  data() {
    return {
      
    }
  },
  components: {
    Header,
    Balance,
    IncomeExpenses,
    AddTransaction,
    TransactionList
  },
  methods: {
    logout() {
      this.$store.dispatch('logoutUser')
    }
  },
  computed: {
    username() {
      return JSON.parse(localStorage.getItem('user')).username
    }
  },
  mounted() {
    // console.log(this.$store.state.user)
    // console.log(localStorage.getItem('user'))
  }
}
</script>

<style lang="scss" scoped>
.btn-new {
  width:100%;
  background-color: $olive;
  border: 0;

  &:hover {
    background-color: #7fb939;
  }
}
</style>