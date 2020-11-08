<template>
  <v-app-bar app color="white" flat>
    <v-container class="py-0 fill-height">
      <v-img max-width="200px" src="/logo_navbar.png"> </v-img>
      <v-spacer></v-spacer>
      <v-btn v-if="!isLoggedIn && !withoutButtons && includeHome" outlined rounded @click="home">Home</v-btn>
      <v-btn v-if="isLoggedIn && !withoutButtons && includeDashboard" outlined rounded @click="dashboard" class="ml-4">Dashboard</v-btn>
      <v-btn v-if="isLoggedIn && !withoutButtons" outlined rounded @click="logout" class="ml-4">Log Out</v-btn>
      <v-btn v-if="!isLoggedIn && !withoutButtons" outlined rounded @click="login" class="ml-4">Log In</v-btn>
      <v-btn v-if="!isLoggedIn && !withoutButtons" outlined rounded @click="signup" class="ml-4" >Sign Up</v-btn
      >
    </v-container>
  </v-app-bar>
</template>

<script>
export default {
  name: "AppBar",
  props: {
    withoutButtons: {
      type: Boolean,
      default: false
    },
    includeDashboard: {
      type: Boolean,
      default: false
    },
    includeHome: {
      type: Boolean,
      default: false
    }
  },
  components: {},
  methods: {
    home: function() {
      this.$router.push("/");
    },
    signup: function() {
      this.$router.push("/signup");
    },
    login: function() {
      this.$router.push("/login");
    },
    logout: function() {
      this.$store.commit("logout");
      this.$router.push("/login");
    },
    dashboard: function() {
      this.$router.push("/dashboard");
    }
  },
  data: function() {
    return {
      loggedIn: false,
    };
  },
  computed: {
    isLoggedIn: {
      get: function() {
        return this.$store.state.accessToken != null ? true : false
      },
    },
  },
};
</script>
