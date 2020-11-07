<template>
  <v-app>
    <app-bar>
      <v-spacer></v-spacer>
      <v-responsive max-width="260">
        <v-btn outlined rounded>Log In</v-btn>
        <v-btn outlined rounded class="ml-4">Sign Up</v-btn>
      </v-responsive>
    </app-bar>
    <v-main class="grey lighten-5">
      <v-sheet>
        <v-row>
          <div>
          </div>
          <v-col>
            <v-img
                style="position: absolute;"
                max-height="800px"
                src="/images/helping.jpg"
            ></v-img>
            <div style="position: absolute; margin: 80px; max-width: 400px" class="text-center">
              <h1>Help People Just like you</h1>
              <p>Sometimes people with past experiences can give you the best advice</p>
              <div>
                <v-btn rounded outlined class="mt-3" @click="findHelp">Getting Started</v-btn>
              </div>
            </div>
          </v-col>
        </v-row>
      </v-sheet>
    </v-main>
  </v-app>
</template>

<script>


import AppBar from "@/components/AppBar";

export default {
  name: 'Home',
  components: {AppBar},
  methods: {
    findHelp: function () {
      this.$store.commit('clear')
      this.$router.push('questions')
    }
  }
}
</script>
