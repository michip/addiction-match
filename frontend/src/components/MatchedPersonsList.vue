<template>
  <v-container fluid>
    <v-card max-width="1000" class="mx-auto justify-center">
      <v-expansion-panels three-line>
        <template v-for="(item, index) in copiedMatches">
          <v-expansion-panel :key="index">
            <v-expansion-panel-header>
              <v-row align="center" class="spacer" no-gutters>
                <v-col cols="1" sm="2" md="2">
                  <v-avatar>
                    <img
                      v-if="item.picture_url"
                      alt="Avatar"
                      :src="item.picture_url"
                    />
                  </v-avatar>
                </v-col>
                <v-col cols="9" sm="8" md="8">
                  <span
                    >{{ item.first_name }} ({{
                      calculate_age(item.birthday_year)
                    }}), {{ item.city }}</span
                  >
                </v-col>
                <v-col cols="2" sm="2" md="2">
                  <v-progress-circular
                    :rotate="360"
                    :size="50"
                    :width="7"
                    :value="item.percentage_match"
                    :color="percentToHex(item.percentage_match)"
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
                <v-btn elevation="2" color="primary" @click="contact(item)"
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
const tinycolor = require("tinycolor2");
const axios = require("axios").default;

export default {
  props: {
    matches: Array,
  },
  data: function() {
    return {
      copiedMatches: [],
    };
  },
  methods: {
    contact: function(item) {
      const isLoggedIn = this.$store.state.profileInfo !== undefined ? true : false;
      var pk;
      if(isLoggedIn) {
        pk = this.$store.state.profileInfo.pk;
      }

      axios
        .post("http://40.115.33.104:8000/conversations/create", {
          profile_id: isLoggedIn ? pk : undefined,
          first_name: isLoggedIn ? undefined : 'Guest',
          mentor: item.pk
        })
        .then((response) => {
          this.$router.push({ name: "chat", query: { id: response.data.id } });
          const profileId = response.data.profile_id
          this.$store.commit('addProfileInfo', {'pk': profileId})
        });
    },
    calculate_age: (birthday_year) => {
      var currentTime = new Date();
      return currentTime.getFullYear() - birthday_year;
    },
    percentToHex: function(percent) {
      percent = 100 - percent;
      if (percent === 100) {
        percent = 99;
      }
      var r, g, b;

      if (percent < 50) {
        // green to yellow
        r = Math.floor(255 * (percent / 50));
        g = 255;
      } else {
        // yellow to red
        r = 255;
        g = Math.floor(255 * ((50 - (percent % 50)) / 50));
      }
      b = 0;

      function componentToHex(c) {
        var hex = c.toString(16);
        return hex.length == 1 ? "0" + hex : hex;
      }

      const hex_value =
        "#" + componentToHex(r) + componentToHex(g) + componentToHex(b);
      return tinycolor(hex_value)
        .desaturate(60)
        .toString();
    },
    animateProgress: async function(matches) {
      function sleep(ms) {
        return new Promise((resolve) => setTimeout(resolve, ms));
      }

      function withZeroPercentageMatch(match) {
        match.percentage_match = 0;
        return match;
      }

      function withIncreasedPercentageMatch(match, initialMatches) {
        const initialMatch = initialMatches.filter(
          (aMatch) => aMatch.pk == match.pk
        )[0];
        if (initialMatch.percentage_match > match.percentage_match) {
          match.percentage_match = match.percentage_match + 1;
        }
        return match;
      }

      const initialMatches = JSON.parse(
        JSON.stringify(matches.map((match) => match))
      );

      this.copiedMatches = matches.map((match) =>
        withZeroPercentageMatch(match)
      );

      for (var i = 0; i < 101; i++) {
        await sleep(30);
        this.copiedMatches = matches.map((match) =>
          withIncreasedPercentageMatch(match, initialMatches)
        );
      }
    },
  },
};
</script>
