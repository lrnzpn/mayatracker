<template>
  <div>
    <Balance />
    <IncomeExpenses />
    <TransactionList />
    <AddTransaction />
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

</style>