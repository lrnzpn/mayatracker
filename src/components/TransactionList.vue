<template>
  <div class="mt-4">
      <h3>History</h3>

        <div class="accordion list" role="tablist">
          <b-card 
            no-body 
            class="mb-1"
            v-for="t in transactions" 
              :key="t.id"
          >
            <b-card-header 
              header-tag="header" 
              class="list-item m-0" 
              :class="t.amount < 0 ? 'minus' : 'plus'"
              role="tab" 
              v-b-toggle="'accordion-' + t.id">
              {{t.text}} 
                <span>{{t.amount>=0 ? '+' : '-'}}Php {{numberWithCommas(Math.abs(t.amount))}}</span>
            </b-card-header>
            <b-collapse :id="'accordion-' + t.id" accordion="my-accordion" role="tabpanel">
              <b-card-body>
                <b-card-text class="mb-2">Created at {{parseDate(t.created_at)}}</b-card-text>
                <b-button class="me-2" variant="outline-success" size="sm">Edit</b-button>
                <b-button variant="danger" size="sm" @click="deleteTxn(t.id)">Delete</b-button>
              </b-card-body>
            </b-collapse>
          </b-card>
        </div>
  </div>
</template>

<script>
import moment from 'moment'


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
      parseDate(date) {
        return moment(date).utc().format('MM/DD/YYYY')
      },
      deleteTxn(txnId) {
        console.log(txnId)
        this.$store.dispatch('deleteTransaction', txnId)
      }
    },
    mounted() {
      this.$store.dispatch('getTransactions');
    }
}
</script>

<style lang="scss" scoped>
.txn-btn {
  width: 100%;
}

.list {
  list-style-type: none;
  padding: 0;
  margin-bottom: 50px;

  .list-item {
    background-color: $navy;
    box-shadow: $box-shadow;
    color: $white;
    display: flex;
    justify-content: space-between;
    position: relative;
    padding: 10px;
    margin: 10px 0;

      &.plus {
          border-right: 8px solid #2ecc71;
      }

      &.minus {
          border-right: 8px solid #c0392b;
      }

  }
}
</style>