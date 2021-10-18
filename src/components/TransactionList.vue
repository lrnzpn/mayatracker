<template>
  <div>
      <h3>History</h3>
        <ul class="list">
            <li 
              v-for="t in transactions" 
              :key="t.id"
              :class="t.amount < 0 ? 'minus' : 'plus'"
              >
                {{t.text}} 
                <span>
                  {{t.amount>=0 ? '+' : '-'}}
                  Php {{numberWithCommas(Math.abs(t.amount))}}
                </span>
            </li>
        </ul>
  </div>
</template>

<script>

export default {
    computed: {
      transactions() {
        return this.$store.state.transactions
      }
    },
    methods: {
      numberWithCommas(x) {
          return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      },
    },
    mounted() {
      this.$store.dispatch('getTransactions');
    }
}
</script>

<style lang="scss" scoped>
.list {
  list-style-type: none;
  padding: 0;
  margin-bottom: 50px;

  li {
    background-color: #fff;
    box-shadow: $box-shadow;
    color: #333;
    display: flex;
    justify-content: space-between;
    position: relative;
    padding: 10px;
    margin: 10px 0;

      &.plus {
          border-right: 5px solid #2ecc71;
      }

      &.minus {
          border-right: 5px solid #c0392b;
      }

  }
}
</style>