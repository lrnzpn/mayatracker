<template>
  <div class="inc-exp-container">
        <div>
            <h5>Income</h5>
            <p class="money plus">Php {{numberWithCommas(income)}}</p>
        </div>
        <div>
            <h5>Expense</h5>
            <p class="money minus">Php {{numberWithCommas(expense)}}</p>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            income: null,
            expense: null
        }
    },
    methods: {
        numberWithCommas(x) {
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
        this.income = amounts
                        .filter(item => item > 0)
                        .reduce((acc, item) => (acc+=item), 0)
                        .toFixed(2);
        this.expense = (amounts
                        .filter(item => item < 0)
                        .reduce((acc, item) => (acc +=item), 0) * -1)
                        .toFixed(2);
    }
}
</script>

<style lang="scss" scoped>
.inc-exp-container {
  background-color: #fff;
  box-shadow: $box-shadow;
  padding: 20px;
  display: flex;
  justify-content: space-between;
  margin: 20px 0;

  >div {
        flex: 1;
        text-align: center;

        &:first-of-type {
            border-right: 1px solid #dedede;
        }
  }
}


.money {
  font-size: 20px;
  letter-spacing: 1px;
  margin: 5px 0;

  &.plus {
    color: #2ecc71;
  }

    &.minus {
        color: #c0392b;
    }
}


</style>