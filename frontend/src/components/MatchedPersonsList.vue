<template>
  <v-container fill-height fluid>
    <v-card max-width="1000" class="mx-auto justify-center">
      <v-expansion-panels three-line>
        <template v-for="(item, index) in matches">
          <v-expansion-panel :key="index">
            <v-expansion-panel-header>
              <v-row align="center" class="spacer" no-gutters>
                <v-col cols="1" sm="1" md="1">
                  <v-avatar>
                    <img
                      v-if="item.picture_url"
                      alt="Avatar"
                      :src="item.picture_url"
                    />
                  </v-avatar>
                </v-col>
                <v-col cols="9" sm="9" md="9">
                  <span
                    >{{ item.first_name }} ({{ calculate_age(item.birthday_year) }}), {{ item.city }}</span
                  >
                </v-col>
                <v-col cols="2" sm="2" md="2">
                  <v-progress-circular
                    :rotate="360"
                    :size="50"
                    :width="7"
                    :value="item.percentage_match"
                    color="teal"
                  >
                    {{ item.percentage_match }}%
                  </v-progress-circular>
                </v-col>
              </v-row>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-row align="center" class="spacer" no-gutters>
                <p>{{ item.story }}</p>
              </v-row>
              <div class="d-flex justify-end">
                <v-btn
                  elevation="2"
                  color="primary"
                  @click="() => contact(item.id)"
                  >CONTACT</v-btn
                >
              </div>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </template>
      </v-expansion-panels>
    </v-card>
  </v-container>
</template>

<script>
const axios = require("axios").default;
export default {
  mounted: function() {
    this.answers = this.$store.state.answeredQuestions.map(function(x) {
      return { question: x.pk, result: x.result };
    });
    this.getMatchedPersons();
  },
  data: () => ({
    matches: [],
    answers: Array,
  }),
  methods: {
    contact: (id) => {
      console.log(id);
    },
    calculate_age: (birthday_year) => {
      var currentTime = new Date();
      return currentTime.getFullYear() - birthday_year
    },
    getMatchedPersons: function() {
      axios
        .post("http://40.115.33.104:8000/questions/matchmake", this.answers)
        .then((response) => {
          console.log(response.data);
          this.matches = response.data;
        });
    },
  },
};
</script>
