<template>
  <div>
    <h3>History</h3>

    <div class="d-flex justify-content-between align-items-start">
        <router-link to="/" class="mb-5 d-block">Back to home</router-link>
        <div>
            Filter by transaction date:
            <form @submit.prevent="getTransactions(date)" ref="form">
                <b-form-datepicker 
                    size="sm" 
                    id="example-datepicker" 
                    v-model="date" 
                    class="mb-2"
                    :date-format-options="{ year: 'numeric', month: 'numeric', day: 'numeric' }"
                    locale="en"
                    :max="setMaxDate"
                    today-button
                    reset-button
                    ></b-form-datepicker>
                <b-btn variant="outline-secondary" size="sm" type="submit" class="me-2">Submit</b-btn>
                <b-btn variant="outline-danger" size="sm" @click="reset">Reset</b-btn>
            </form>
        </div>

    </div>

        <div>
            <h5>Total transactions</h5>
            <h1 v-if="total">Php {{numberWithCommas(total)}}</h1>
            <hr>
        </div>


      <div class="accordion list" role="tablist" v-if="transactions.length">
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
              </b-card-body>
            </b-collapse>
          </b-card>
        </div>
        <h4 v-else>You have no entries for this date</h4>
  </div>
</template>

<script>
export default {
    data() {
        return {
            total: null,
            date: ''
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
            filterTxnDate() {
                
            },
        getTransactions(date) {
            if(date) {
                this.$store.dispatch('getTransactions', `transaction_date=${date}`)
            } else {
                this.$store.dispatch('getTransactions', ``)
            }
            setTimeout(() => {
                const amounts = this.transactions.map(t => t.amount)
                this.total = amounts.reduce((acc, item) => (acc+=item), 0).toFixed(2)
            }, 500)

            console.log(this.transactions)
        },
        reset() {
            location.reload()
        }
      },
    mounted() {
         this.$store.dispatch('getTransactions', '');
            setTimeout(() => {
                const amounts = this.transactions.map(t => t.amount)
                this.total = amounts.reduce((acc, item) => (acc+=item), 0).toFixed(2)
            }, 500)
    }
}
</script>

<style lang="scss" scoped>
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