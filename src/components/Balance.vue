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
            try {
                return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
            } catch {}
        }
    },
    computed: {
      transactions() {
        return this.$store.state.transactions
      }
    },
    mounted() {
        this.$store.dispatch('getTransactions');

        setTimeout(() => {
            const amounts = this.transactions.map(t => t.amount)
            this.total = amounts.reduce((acc, item) => (acc+=item), 0).toFixed(2)
        }, 0)
    },
}
</script>

<style>

</style>