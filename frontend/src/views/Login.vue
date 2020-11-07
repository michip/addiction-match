<template>
  <v-app>
    <app-bar></app-bar>
    <v-main class="grey lighten-5">
      <v-container class="d-flex justify-center">
        <validation-observer v-slot="{ invalid }" ref="observer">
          <form>
            <v-card class="pa-5" min-width="500px">
              <v-card-title>Login</v-card-title>
              <validation-provider
                  v-slot="{ errors }"
                  name="Name"
                  rules="required">
                <v-text-field
                    v-model="name"
                    :error-messages="errors"
                    label="Name"
                ></v-text-field>
              </validation-provider>
              <validation-provider
                  v-slot="{ errors }"
                  name="Password"
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
      password: null
    }
  },
  methods: {
    submit: async function () {

    }
  },
  computed: {}
}
</script>
