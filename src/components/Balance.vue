<template>
  <div>
      <h5>Your Balance</h5>
      <h1>Php {{numberWithCommas(total)}}</h1>
  </div>
</template>

<script>
export default {
    data() {
        return {
            total: null
        }
    },
    methods: {
        numberWithCommas(x) {
            // https://stackoverflow.com/a/2901298
            return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
        }
    },
    computed: {
      transactions() {
        return this.$store.getters.allTransactions
      }
    },
    mounted() {
        const amounts = this.transactions.map(t => t.amount)
        this.total = amounts.reduce((acc, item) => (acc+=item), 0).toFixed(2)
    }
}
</script>

<style>

</style>