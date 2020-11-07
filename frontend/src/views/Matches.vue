<template>
  <v-app>
      <AppBar></AppBar>
    <v-content class="grey lighten-5">
      <MatchedPersonsList></MatchedPersonsList>
    </v-content>
  </v-app>
</template>

<script>
import MatchedPersonsList from "../components/MatchedPersonsList";
import AppBar from "../components/AppBar";

export default {
  name: "Matches",
  components: { MatchedPersonsList, AppBar },
};
</script>
