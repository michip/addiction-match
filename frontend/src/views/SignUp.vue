<template>
  <v-app>
    <app-bar></app-bar>
    <v-main class="grey lighten-5">
      <v-container>
        <validation-observer v-slot="{ invalid }" ref="observer">
          <form>
            <v-row>
              <v-col cols="12" lg="6">
                <v-card round class="pa-5">
                  <v-card-title>Tell others about yourself</v-card-title>
                  <validation-provider
                      v-slot="{ errors }"
                      name="username"
                      rules="required">
                    <v-text-field
                        v-model="username"
                        :error-messages="errors"
                        label="Username"
                    ></v-text-field>
                  </validation-provider>
                  <validation-provider
                      v-slot="{ errors }"
                      name="firstName"
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
                  <v-row>
                    <v-col>
                      <validation-provider
                          v-slot="{ errors }"
                          name="Gender"
                          rules="required">
                        <v-select
                            v-model="gender"
                            :items="possibleGenders"
                            item-text="label"
                            item-value="value"
                            :error-messages="errors"
                            label="Gender"
                            single-line
                        ></v-select>
                      </validation-provider>
                    </v-col>
                    <v-col>
                      <v-menu
                          ref="menu"
                          v-model="menu"
                          :close-on-content-click="false"
                          :return-value.sync="date"
                          transition="scale-transition"
                          offset-y
                          max-width="290px"
                          min-width="290px"
                      >
                        <template v-slot:activator="{ on, attrs }">
                          <validation-provider
                              v-slot="{ errors }"
                              name="Birthday"
                              rules="required">
                            <v-text-field
                                v-model="date"
                                label="Birthday"
                                prepend-icon="mdi-calendar"
                                :error-messages="errors"
                                readonly
                                v-bind="attrs"
                                v-on="on"
                            ></v-text-field>
                          </validation-provider>
                        </template>
                        <v-date-picker
                            v-model="date"
                            type="month"
                            no-title
                            scrollable
                        >
                          <v-spacer></v-spacer>
                          <v-btn
                              text
                              color="primary"
                              @click="menu = false"
                          >
                            Cancel
                          </v-btn>
                          <v-btn
                              text
                              color="primary"
                              @click="$refs.menu.save(date)"
                          >
                            OK
                          </v-btn>
                        </v-date-picker>
                      </v-menu>
                    </v-col>
                  </v-row>
                  <validation-provider
                      v-slot="{ errors }"
                      name="Name"
                      rules="required">
                    <v-text-field
                        v-model="location"
                        label="City"
                        prepend-icon="mdi-map-marker"
                        :error-messages="errors"
                    ></v-text-field>
                  </validation-provider>
                </v-card>
              </v-col>
              <v-col cols="12" lg="6">
                <v-card style="height: 100%" round>
                  <div>
                    <v-textarea
                        class="pa-5"
                        outlined
                        style="min-height: 100%"
                        v-model="story"
                        name="story"
                        label="Write your story"
                    ></v-textarea>
                  </div>
                </v-card>
              </v-col>
            </v-row>
            <v-btn
                x-large
                color="primary"
                rounded
                class="float-right"
                :disabled="invalid"
                @click="submit">
              Submit
            </v-btn>
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
      username: null,
      nameErrors: [],
      password: null,
      passwordErrors: [],
      possibleGenders: [{'label': 'Male', 'value': 0},
        {'label': 'Female', 'value': 1},
        {'label': 'Other', 'value': 2}],
      gender: null,
      date: null,
      location: null,
      story: '',
      menu: null
    }
  },
  methods: {
    submit: async function () {
      let infos = {
        'username': this.username,
        'first_name': this.name,
        'password': this.password,
        'birthday_year': parseInt(this.date.substring(0, 4)),
        'city': this.location,
        'story': this.story,
        'gender': this.gender,
        'matching_preference': 0
      }
      console.log(infos)
      try {
        let response = await axios.post('http://40.115.33.104:8000/profiles/create', infos)
        console.log(response)
        this.$store.commit('addProfileInfo', infos)
        this.$router.push('/questions')
      } catch (e) {
        console.log(e)
      }
    }
  },
  computed: {}
}
</script>
