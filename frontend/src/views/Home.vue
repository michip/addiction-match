<template>
  <v-app>
    <app-bar>
      <v-spacer></v-spacer>
      <v-responsive max-width="260">
        <v-btn outlined rounded @click="login">Log In</v-btn>
        <v-btn outlined rounded @click="signup" class="ml-4">Sign Up</v-btn>
      </v-responsive>
    </app-bar>
    <v-main class="grey lighten-5">
      <v-sheet>
        <v-row>
          <v-col>
            <div :style="fullBackground" style="position: relative;
              width: 100%;
              max-height: 100%;
              height: 800px;
              background-repeat: no-repeat;
              background-size: cover;
              display: block;">
              <div style="position: absolute; margin: 80px; max-width: 400px" class="text-center">
                <h1>Help People Just like you</h1>
                <p>Sometimes people with past experiences can give you the best advice</p>
                <div>
                  <v-btn rounded outlined class="mt-3" @click="findHelp">Getting Started</v-btn>
                </div>
              </div>
            </div>
          </v-col>
        </v-row>
      </v-sheet>
      <div style="max-width: 1200px !important;" class="container">
        <v-row class="mx-5">
          <v-col class="col-lg-8 col-md-6 col-12">
            <h1>
              Helping the youth
            </h1>
            <div style="color: #6c757d!important;">
              Preventing the early use of drugs for youth may go a long way in reducing health and mental risks. Young
              people tend to find themselves alone when they encounter hardships in their life. help me,help you allows
              young adults to find a mentor who experienced the same difficulties in their life and can now advise youth
              and build a helpful relationship with them.
              Take on our quick survey below if you’re a newcomer, otherwise you can sign-in !
            </div>
          </v-col>
          <v-col class="col-lg-4 col-md-6 col-12 p-5 p-md-3 p-lg-0">
            <v-row justify="space-around">
              <v-col class="col-4 col-sm-4 col-md-6 col-lg-8">
                <v-img
                    class="img-fluid"
                    src="/images/hands.png"
                ></v-img>
              </v-col>
            </v-row>

          </v-col>
        </v-row>

        <v-row class="mx-5">
          <v-col class="col-lg-4 col-md-6 col-12 p-5 p-md-3 p-lg-0">
            <v-row justify="space-around">
              <v-col class="col-4 col-sm-4 col-md-6 col-lg-8">
                <v-img
                    class="img-fluid"
                    src="/images/community.png"
                ></v-img>
              </v-col>
            </v-row>
          </v-col>

          <v-col class="col-lg-8 col-md-6 col-12">
            <h1>
              Everyone can participate
            </h1>
            <div style="color: #6c757d!important;">
              If you’re looking for someone to talk to or if you’re offering a helping hand you’re welcome at help
              me,help you. We aim to build a big community of mentors and peers so everyone can support each other in
              troubled times but also build a sustainable relationship and share good moments together
            </div>
          </v-col>

        </v-row>

        <v-row class="mx-5">
          <v-col class="col-lg-8 col-md-6 col-12">
            <h1>
              Protecting your data
            </h1>
            <div style="color: #6c757d!important;">
              With help me,help you we ensure the user’s identity privacy and discretion. Our service is free for all
              and, and you can always use it anonymously. However we encourage you to create a profile if you want to
              keep contacts with your precedent matches or if you want to skip the survey.
            </div>
          </v-col>
          <v-col class="col-lg-4 col-md-6 col-12 p-5 p-md-3 p-lg-0">
            <v-row justify="space-around">
              <v-col class="col-4 col-sm-4 col-md-6 col-lg-8">
                <v-img
                    class="img-fluid"
                    src="/images/protection.png"
                ></v-img>
              </v-col>
            </v-row>

          </v-col>
        </v-row>

        <v-row class="mx-5">

          <v-col>
            <h1 class="text-center mb-5 display-2">Our Team</h1>

            <v-row class="mx-5 mt-3">
              <v-col class="col-12 col-md-6 col-lg-3 text-center">
                <v-avatar
                    size="100px"
                >
                  <v-img src="/images/jonas.jpg"></v-img>
                </v-avatar>

                <h3>Jonas Dippel</h3>
              </v-col>

              <v-col class="col-12 col-md-6 col-lg-3 text-center">
                <v-avatar
                    size="100px"
                >
                  <v-img src="/images/oscar.png"></v-img>
                </v-avatar>

                <h3>Oscar Che</h3>
              </v-col>

              <v-col class="col-12 col-md-6 col-lg-3 text-center">
                <v-avatar
                    size="100px">
                  <v-img src="/images/michael.jpg"></v-img>
                </v-avatar>

                <h3>Michael Perk</h3>
              </v-col>

              <v-col class="col-12 col-md-6 col-lg-3 text-center">
                <v-avatar
                    size="100px"
                >
                  <v-img src="/images/piotr.jpg"></v-img>
                </v-avatar>

                <h3>Piotr Proszowski</h3>
              </v-col>

            </v-row>
          </v-col>

        </v-row>
      </div>
    </v-main>
  </v-app>
</template>

<script>


import AppBar from "@/components/AppBar";

export default {
  name: 'Home',
  data() {
    return {
      fullBackground: {
        backgroundImage: `url(${require('@/assets/helping.jpg')})`
      }
    }
  },
  components: {AppBar},
  methods: {
    findHelp: function () {
      this.$store.commit('clear')
      this.$router.push('questions')
    },
    signup: function () {
      this.$router.push('/signup')
    },
    login: function () {
      this.$router.push('/login')
    }
  }
}
</script>
