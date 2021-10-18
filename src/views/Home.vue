<template>
  <div>
    <b-modal 
      id="modal-1" 
      title="Add new transaction"
      hide-footer
      >
      <AddTransaction />
    </b-modal>

    <Balance />
    <IncomeExpenses />
    <b-button 
      v-b-modal.modal-1 
      block 
      class="btn-new">New Transaction</b-button>
    <TransactionList />
    
  </div>
</template>

<script>
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
    Balance,
    IncomeExpenses,
    AddTransaction,
    TransactionList
  },
  computed: {
    testing() {
      return this.$store.state.test
    }
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