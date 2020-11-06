<template>
  <v-app>
    <v-app-bar
        app
        color="white"
        flat>
      <v-container class="py-0 fill-height">
        <v-avatar
            class="mb-5"
            width="100px"
            tile>
          <v-img
              src="https://cdn.discordapp.com/attachments/774276728402608202/774383075236905000/f5a0c63c-edf1-4b54-a654-a521cf8521ec_200x200.png">
          </v-img>

        </v-avatar>

        <v-btn
            v-for="link in links"
            :key="link"
            text>
          {{ link }}
        </v-btn>

        <v-spacer></v-spacer>

        <v-responsive max-width="260">
          <v-btn outlined rounded>Log In</v-btn>
          <v-btn outlined rounded class="ml-4">Sign Up</v-btn>
        </v-responsive>
      </v-container>
    </v-app-bar>

    <v-main class="grey lighten-5">
      <v-sheet>
        <v-row>
          <div>
          </div>
          <v-col>
            <v-img
                style="position: absolute;"
                max-height="700px"
                src="/images/helping.jpg"
            ></v-img>
            <div style="position: absolute; margin: 80px; max-width: 400px" class="text-center">
              <h1>Help People Just like you</h1>
              <p>Sometimes people with past experiences can give you the best advice</p>
              <div >
              <v-btn rounded outlined class="mt-3">Getting Started</v-btn>
              </div>
            </div>
          </v-col>
        </v-row>
      </v-sheet>
    </v-main>
  </v-app>
</template>

<script>


export default {
  name: 'Home',
  components: {}
}
</script>
