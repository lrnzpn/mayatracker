<template>
  <div>
        <form @submit.prevent="onSubmit" ref="form">
            <div class="form-group">
                <label for="description">Description</label>
                <input class="form-control" type="description" v-model="description" name="text" placeholder="Enter text..." required />
            </div>
            <div class="form-group">
                <label for="amount">
                    Amount <br />
                    (negative - expense, positive - income)
                </label>
                <input class="form-control" type="number" v-model="amount" name="amount" placeholder="Enter amount..." required />
            </div>
            <div class="form-group">
                <label for="date">Transaction Date</label>
                <input class="form-control" type="date" v-model="date" name="date" :max="setMaxDate" required />
            </div>
            <div class="form-group">
                <div class="form-group">
                <label for="category">Category</label>
                <input class="form-control" type="category" v-model="category" name="text" required />
            </div>
            </div>

            <button class="btn" type="submit">Add transaction</button>
        </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      description: null,
      amount: null,
      date: null,
      category: null
    }
  },
  methods: {
    onSubmit() {
      const transaction = {
        "description": this.description,
        "amount": parseFloat(this.amount),
        "transaction_date": this.date,
        "category": this.category
      }

      this.$store.dispatch('addTransaction', transaction).then(() => {
          setTimeout(() => {
            location.reload()
          },500)})
    },
  },
  computed: {
    setMaxDate() {
      const today = new Date();
      const date = today.getFullYear() + '-' + (today.getMonth()+1) + '-' + today.getDate();

      return date
    }
  }
}
</script>

<style lang="scss" scoped>
label {
  display: inline-block;
  margin: 10px 0;
}

// input[type='text'],
// input[type='number'] {
//   border: 1px solid #dedede;
//   border-radius: 2px;
//   display: block;
//   font-size: 16px;
//   padding: 10px;
//   width: 100%;
// }

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