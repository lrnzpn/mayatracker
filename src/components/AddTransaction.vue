<template>
  <div>
        <h3>Add new transaction</h3>
        <form @submit.prevent="onSubmit" ref="form">
            <div>
                <label for="text">Text</label>
                <input type="text" v-model="text" name="text" placeholder="Enter text..." />
            </div>
            <div>
                <label for="amount">
                    Amount <br />
                    (negative - expense, positive - income)
                </label>
                <input type="number" v-model="amount" name="amount" placeholder="Enter amount..." />
            </div>
            <button class="btn" type="submit">Add transaction</button>
        </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      text: null,
      amount: null
    }
  },
  methods: {
    onSubmit() {
      const transaction = {
        "text": this.text,
        "amount": parseInt(this.amount)
      }

      this.$store.dispatch('addTransaction', transaction)

      location.reload()
    }
  }
}
</script>

<style lang="scss" scoped>
label {
  display: inline-block;
  margin: 10px 0;
}

input[type='text'],
input[type='number'] {
  border: 1px solid #dedede;
  border-radius: 2px;
  display: block;
  font-size: 16px;
  padding: 10px;
  width: 100%;
}

.btn {
  cursor: pointer;
  background-color: #9c88ff;
  box-shadow: $box-shadow;
  color: #fff;
  border: 0;
  display: block;
  font-size: 16px;
  margin: 10px 0 30px;
  padding: 10px;
  width: 100%;
}

.btn:focus,
.delete-btn:focus {
  outline: 0;
}
</style>