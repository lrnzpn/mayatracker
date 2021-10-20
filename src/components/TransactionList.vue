<template>
  <div class="mt-4">
      <h3>Transactions Today</h3>
        <h2 v-if="transactions.length == 0">You have no transactions</h2>
        <div v-else class="accordion list" role="tablist">
          <b-card 
            no-body 
            class="mb-1"
            v-for="(t, idx) in transactions" 
              :key="idx"
          >
            <b-card-header 
              header-tag="header" 
              class="list-item m-0" 
              :class="t.amount < 0 ? 'minus' : 'plus'"
              role="tab" 
              v-b-toggle="'accordion-'+idx">
              {{t.description}} 
                <span>{{t.amount>=0 ? '+' : '-'}}Php {{numberWithCommas(Math.abs(t.amount))}}</span>
            </b-card-header>
            <b-collapse :id="'accordion-' + idx" accordion="my-accordion" role="tabpanel">
              <b-card-body>
                <b-card-text class="mb-2">Category: {{t.category}}</b-card-text>       
                <b-card-text class="mb-2">Transaction Date: {{t.transaction_date}}</b-card-text>

                <b-button 
                  class="me-2" 
                  variant="outline-success" 
                  size="sm"
                  v-b-modal="'modal-'+t.id"
                  >Edit</b-button>
                <b-button variant="danger" size="sm" @click="deleteTxn(t.id)">Delete</b-button>
              </b-card-body>
            </b-collapse>
            <b-modal :id="'modal-'+t.id" hide-footer title="Edit Transaction">
              <EditTransaction v-if="t.id" :txnId="t.id" />
            </b-modal>
          </b-card>

          <router-link to="/history">View all Transactions</router-link>
        </div>
  </div>
</template>

<script>
import EditTransaction from './EditTransaction.vue'

export default {
  components: {
    EditTransaction
  },
  data() {
    return {
      queryDate: ''
    }
  },
    computed: {
      transactions() {
        return this.$store.state.transactions.sort((a,b) => {
          return new Date(b.created_at) - new Date(a.created_at)
        })
      },
      setMaxDate() {
        const today = new Date();
        const date = today.getFullYear() + '-' + (today.getMonth()+1) + '-' + today.getDate();

        return date
      }
    },
    methods: {
      numberWithCommas(x) {
          return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      },
      deleteTxn(txnId) {
        this.$store.dispatch('deleteTransaction', txnId).then(() => {
          setTimeout(() => {
            location.reload()
          },500)
        })
      },
    },
    mounted() {
      this.$store.dispatch('filterGetTransactions');
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