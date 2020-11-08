<template>
  <v-app>
    <app-bar :includeHome="true"></app-bar>
    <v-main class="grey lighten-5">
      <v-container class="">
        <validation-observer v-slot="{ invalid }" ref="form">
          <form>
            <v-col cols="12" offset-md="2" offset-lg="3" md="8" lg="6">
              <v-card class="pa-5">
                <v-card-title>Login</v-card-title>
                <validation-provider
                    v-slot="{ errors }"
                    name="name"
                    rules="required">
                  <v-text-field
                      v-model="name"
                      :error-messages="errors"
                      label="Name"
                  ></v-text-field>
                </validation-provider>
                <validation-provider
                    v-slot="{ errors }"
                    name="password"
                    rules="required">
                  <v-text-field
                      v-model="password"
                      :error-messages="errors"
                      label="Password"
                      type="password"
                  ></v-text-field>
                </validation-provider>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn
                      large
                      color="primary"
                      rounded
                      class="float-right"
                      :disabled="invalid"
                      @click="submit">
                    Submit
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-col>
          </form>
        </validation-observer>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>

import AppBar from "@/components/AppBar";

const axios = require("axios").default;
import {required, email, max} from 'vee-validate/dist/rules'
import {extend, ValidationObserver, ValidationProvider, setInteractionMode} from 'vee-validate'

setInteractionMode('eager')

extend('required', {
  ...required,
  message: '{_field_} can not be empty',
})

export default {

  name: 'Questionnaire',
  components: {
    AppBar,
    ValidationProvider,
    ValidationObserver
  },
  data: function () {
    return {
      name: null,
      password: null,
      loginError: false
    }
  },
  methods: {
    submit: async function () {
      let success = await this.$store.dispatch('login', {'name': this.name, 'password': this.password})
      if (success) {
        this.$router.push('/dashboard')
      } else {
        this.$refs.form.setErrors({'name': [], 'password': ['wrong credentials']})
      }
    }
  },
  computed: {}
}
</script>
