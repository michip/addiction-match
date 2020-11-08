<template>
  <v-app>
    <app-bar>
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
            <matched-persons-list ref="matches" :matches="matches"></matched-persons-list>
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
      chats: [],
      matches: []
    }
  },
  mounted: function () {
    this.getData()
  },
  methods: {
    getData: async function () {
      const headers = {'Authorization': 'Bearer ' + this.$store.state.accessToken}
      const url = config.baseUrl + '/profiles/get'
      console.log(url)
      try {
        let response = await axios.get(url, {'headers': headers})
        if (response.status === 200) {
          console.log(response)
          const profile = response.data.profile
          this.name = profile['first_name']
          this.location = profile.city
          this.image = profile['picture_url']
          this.chats = response.data['started_conversations']
          this.matches = response.data['matches']
          this.$refs.matches.animateProgress(this.matches);
          this.$store.commit('addProfileInfo', profile)
        }
      } catch (e) {
        if (e.response.status === 401) {
          this.$router.push('/login')
        }
      }
    }
  }
}
</script>
