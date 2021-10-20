<template>
  <div>
        <form @submit.prevent="onSubmit" ref="form" v-if="transaction">
            <div class="form-group">
                <label for="description">Description</label>
                <input class="form-control" type="description" v-model="transaction.description" name="text" placeholder="Enter text..." />
            </div>
            <div class="form-group">
                <label for="amount">
                    Amount <br />
                    (negative - expense, positive - income)
                </label>
                <input class="form-control" type="number" v-model="transaction.amount" name="amount" placeholder="Enter amount..." />
            </div>
            <div class="form-group">
                <label for="date">Transaction Date</label>
                <input 
                    class="form-control" 
                    type="date" 
                    v-model="transaction.transaction_date"
                    name="date" 
                    :max="setMaxDate"/>
            </div>
            <div class="form-group">
                <label for="category">
                    Category
                </label>
                <select v-model="transaction.category" class="form-control">
                  <option disabled value="">Please select one</option>
                  <option>Allowance</option>
                  <option>Food</option>
                  <option>Travel</option>
                  <option>Bills</option>
                  <option>Shopping</option>
                </select>
            </div>

            <button class="btn" type="submit">Update transaction</button>
        </form>
        <h3 v-else>
            Loading...
        </h3>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    props: [
        'txnId'
    ],
  methods: {
    onSubmit() {
        const transaction = {
            "id": this.txnId,
            "description": this.transaction.description,
            "amount": parseFloat(this.transaction.amount),
            "transaction_date": this.transaction.transaction_date,
            "category": this.transaction.category
        }
        this.$store.dispatch('editTransaction', transaction)
            .then(() => {
                setTimeout(() => {
                    location.reload()
                },500)
            })
    }
        
  },
  computed: {
    setMaxDate() {
      const today = new Date();
      const date = today.getFullYear() + '-' + (today.getMonth()+1) + '-' + today.getDate();

      return date
    },
    transaction() {
        return this.$store.getters.getTransaction
    }
  },
  mounted() {
      this.$store.dispatch('getTransaction', this.txnId);
    }
}
</script>

<style lang="scss" scoped>
label {
  display: inline-block;
  margin: 10px 0;
}

.btn {
  cursor: pointer;
  background-color: $olive;
  box-shadow: $box-shadow;
  color: #fff;
  border: 0;
  display: block;
  font-size: 16px;
  margin: 10px 0 30px;
  padding: 10px;
  width: 100%;
  &:hover {
    background-color: #7fb939;
    color: $white;
  }
}

.btn:focus,
.delete-btn:focus {
  outline: 0;
}
</style>