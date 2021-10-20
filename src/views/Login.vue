<template>
  <div>
          <Header />

      <h3>Login</h3>
       <b-form @submit.prevent="onSubmit" ref="form">
           <b-form-group
                id="input-group-1"
                label="Username:"
                label-for="input-1"
                class="mb-2"
            >
                <b-form-input
                id="input-1"
                v-model="form.username"
                placeholder="Enter username"
                required
                ></b-form-input>
            </b-form-group>

            <b-form-group
                id="input-group-2"
                label="Password:"
                label-for="input-2"
                class="mb-2"
            >
                <b-form-input 
                type="password" 
                id="input-2" 
                v-model="form.password"
                required
                ></b-form-input>
            </b-form-group>

             <div class="form-group">
                <button class="btn btn-primary" type="submit">Login</button>
                <router-link to="/register" class="btn btn-link">Register</router-link>
            </div>
    </b-form>
  </div>
</template>

<script>
import Header from '../components/Header.vue'

export default {
     components: {
        Header
    },
    data() {
        return {
            form: {
                username: "",
                password: ""
            }
        }
    },
    methods: {
        onSubmit() {
            this.$store.dispatch('loginUser', this.form)
        }
    },
}
</script>

<style lang="scss" scoped>

</style>