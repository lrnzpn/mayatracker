<template>
  <div>
          <Header />

      <h3>Register</h3>
       <b-form @submit.prevent="onSubmit" ref="form">
           <b-form-group
                id="input-group-1"
                label="Username:"
                label-for="input-1"
                description="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
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
                id="input-group-3"
                label="Email:"
                label-for="input-3"
                class="mb-2"
            >
                <b-form-input 
                type="email" 
                id="input-3" 
                v-model="form.email"
                placeholder="Enter email"
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

            <div class="form-group pt-2">
                <button 
                    class="btn btn-primary" 
                    type="submit" 
                    >Register</button>
                <router-link to="/login" class="btn btn-link">Cancel</router-link>
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
                email:"",
                password: ""
            }
        }
    },
    methods: {
        onSubmit() {
            this.$store.dispatch('registerUser', this.form)
        }
    }
}
</script>

<style lang="scss" scoped>

</style>