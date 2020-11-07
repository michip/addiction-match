<template>
  <v-app>
    <app-bar>
      <v-spacer></v-spacer>
      <v-responsive max-width="260">
        <v-btn outlined rounded @click="login">Log Out</v-btn>
      </v-responsive>
    </app-bar>
    <v-main class="grey lighten-5">
      <v-container>
        <v-row>
          <v-col cols="12" lg="6">
            <v-card class="">
              <v-btn
                  class="float-right ma-2"
                  icon>
                <v-icon left>
                  mdi-pencil
                </v-icon>
              </v-btn>
              <v-list>
                <v-list-item two-line>
                  <v-list-item-avatar size="80">
                    <img :src="image">
                  </v-list-item-avatar>
                  <v-list-item-content>
                    <v-list-item-title class="text-h4">{{ name }}</v-list-item-title>
                    <v-list-item-subtitle>{{ location }}</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-card>
            <v-subheader class="text-h5 mt-5">Chats</v-subheader>
            <conversations :chats="chats"></conversations>
          </v-col>
          <v-col cols="12" lg="6">
            <v-subheader class="text-h5">Potential Matches</v-subheader>
            <matched-persons-list></matched-persons-list>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>

import AppBar from "@/components/AppBar";
import MatchedPersonsList from "@/components/MatchedPersonsList";
import Conversations from "@/components/Conversations";

const axios = require("axios").default;
import config from "@/config";

export default {
  name: 'Home',
  components: {Conversations, MatchedPersonsList, AppBar},
  data: function () {
    return {
      name: '',
      location: 'Berlin, Germany',
      image: '',
      chats: [
        {
          id: 1,
          avatar: "https://cdn.vuetifyjs.com/images/lists/1.jpg",
          name: "Piotr Proszowski",
          chat: "Thanks for your help!"
        },
        {
          id: 2,
          avatar: "https://cdn.vuetifyjs.com/images/lists/2.jpg",
          name: "Oscar Che",
          chat: ""
        }
      ]
    }
  },
  created: function () {
    this.getData()
  },
  methods: {
    logout: function () {
      this.$router.push('/login')
    },
    getData: async function () {
      console.log(this.$store.state.accessToken)
      const headers = {'Authorization: Bearer': this.$store.state.accessToken}
      let response = await axios.get("${config.baseUrl}/profiles/get/", {}, headers)
      console.log(response)
    }
  }
}
</script>
