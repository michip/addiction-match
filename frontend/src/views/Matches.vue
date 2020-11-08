<template>
  <v-app>
    <AppBar></AppBar>
    <v-content class="grey lighten-5">
      <v-container fill-height>
        <MatchedPersonsList ref="matches" :matches="matches"></MatchedPersonsList>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import MatchedPersonsList from "../components/MatchedPersonsList";
import AppBar from "../components/AppBar";
const axios = require("axios").default;

export default {
  name: "Matches",
  components: { MatchedPersonsList, AppBar },
  mounted: function() {
    console.log("matches: ", this.matches)
    this.answers = this.$store.state.answeredQuestions.map(function(x) {
      return { question: x.pk, result: x.result };
    });
    this.getMatchedPersons();
  },
  data: function() {
    return {
      matches: [],
      answers: Array
    };
  },
  methods: {
    getMatchedPersons: function() {
      const isLoggedIn = this.$store.state.profileInfo !== null
      var pk;
      if(isLoggedIn) {
        pk = this.$store.state.profileInfo.pk;
      }
      axios
        .post("http://40.115.33.104:8000/questions/matchmake", {profile_id: isLoggedIn ? pk : undefined, answers: this.answers})
        .then((response) => {
          console.log(response.data);
          this.matches = response.data;
          this.$refs.matches.animateProgress(this.matches);
        });
    },
  },
};
</script>
