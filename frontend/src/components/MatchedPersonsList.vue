<template>
  <v-container fill-height fluid>
    <v-card max-width="1000" class="mx-auto justify-center">
      <v-expansion-panels three-line>
        <template v-for="(item,index) in matches">
          <v-expansion-panel :key="index">
            <v-expansion-panel-header>
              <v-row align="center" class="spacer" no-gutters>
                <v-col cols="1" sm="1" md="1">
                  <v-avatar>
                    <img v-if="item.avatar" alt="Avatar" :src="item.avatar" />
                  </v-avatar>
                </v-col>
                <v-col cols="9" sm="9" md="9">
                  <span>{{ item.first_name }}, {{ item.birthday_year}}, {{item.city}}</span>
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
    this.getMatchedPersons();
  },
  data: () => ({
    matches: [],
    // matches: [
    //   {
    //     id: 1,
    //     avatar: "https://cdn.vuetifyjs.com/images/lists/1.jpg",
    //     name: "Piotr Proszowski",
    //     age: "23",
    //     story:
    //       "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a dui eleifend, molestie erat et, porttitor nisl. In vulputate accumsan suscipit. In non ante sit amet mauris accumsan pellentesque. Fusce pharetra sodales mattis. Fusce aliquet, urna et eleifend viverra, orci orci faucibus augue, eu bibendum dui lectus non purus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Maecenas tempor urna eros, at pharetra massa suscipit ac. Nullam tempor turpis justo, ac dapibus erat mattis at. Curabitur sagittis commodo lacus, id pharetra purus scelerisque eget. Vestibulum pharetra, mi sed fermentum ultricies, nibh eros varius nunc, fermentum pretium est ligula in lorem. Mauris eget tortor eget lacus volutpat dictum. Praesent quis erat ligula. Donec lectus lorem, facilisis ac congue vel, suscipit sed nisi. In hac habitasse platea dictumst. Nam ut gravida massa. Sed tempus et mauris a pharetra.",
    //     percentageMatch: 97,
    //   },
    //   {
    //     id: 2,
    //     avatar: "https://cdn.vuetifyjs.com/images/lists/2.jpg",
    //     name: "Oscar Che",
    //     age: `26`,
    //     story:
    //       "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a dui eleifend, molestie erat et, porttitor nisl. In vulputate accumsan suscipit. In non ante sit amet mauris accumsan pellentesque. Fusce pharetra sodales mattis. Fusce aliquet, urna et eleifend viverra, orci orci faucibus augue, eu bibendum dui lectus non purus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Maecenas tempor urna eros, at pharetra massa suscipit ac. Nullam tempor turpis justo, ac dapibus erat mattis at. Curabitur sagittis commodo lacus, id pharetra purus scelerisque eget. Vestibulum pharetra, mi sed fermentum ultricies, nibh eros varius nunc, fermentum pretium est ligula in lorem. Mauris eget tortor eget lacus volutpat dictum. Praesent quis erat ligula. Donec lectus lorem, facilisis ac congue vel, suscipit sed nisi. In hac habitasse platea dictumst. Nam ut gravida massa. Sed tempus et mauris a pharetra.",
    //     percentageMatch: 63,
    //   },
    //   {
    //     id: 3,
    //     avatar: "https://cdn.vuetifyjs.com/images/lists/3.jpg",
    //     name: "Ali Connors",
    //     age: "23",
    //     story:
    //       "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a dui eleifend, molestie erat et, porttitor nisl. In vulputate accumsan suscipit. In non ante sit amet mauris accumsan pellentesque. Fusce pharetra sodales mattis. Fusce aliquet, urna et eleifend viverra, orci orci faucibus augue, eu bibendum dui lectus non purus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Maecenas tempor urna eros, at pharetra massa suscipit ac. Nullam tempor turpis justo, ac dapibus erat mattis at. Curabitur sagittis commodo lacus, id pharetra purus scelerisque eget. Vestibulum pharetra, mi sed fermentum ultricies, nibh eros varius nunc, fermentum pretium est ligula in lorem. Mauris eget tortor eget lacus volutpat dictum. Praesent quis erat ligula. Donec lectus lorem, facilisis ac congue vel, suscipit sed nisi. In hac habitasse platea dictumst. Nam ut gravida massa. Sed tempus et mauris a pharetra.",
    //     percentageMatch: 54,
    //   },
    //   {
    //     id: 4,
    //     avatar: "https://cdn.vuetifyjs.com/images/lists/4.jpg",
    //     name: "Jonas Dippel",
    //     age: "25",
    //     story:
    //       "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a dui eleifend, molestie erat et, porttitor nisl. In vulputate accumsan suscipit. In non ante sit amet mauris accumsan pellentesque. Fusce pharetra sodales mattis. Fusce aliquet, urna et eleifend viverra, orci orci faucibus augue, eu bibendum dui lectus non purus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Maecenas tempor urna eros, at pharetra massa suscipit ac. Nullam tempor turpis justo, ac dapibus erat mattis at. Curabitur sagittis commodo lacus, id pharetra purus scelerisque eget. Vestibulum pharetra, mi sed fermentum ultricies, nibh eros varius nunc, fermentum pretium est ligula in lorem. Mauris eget tortor eget lacus volutpat dictum. Praesent quis erat ligula. Donec lectus lorem, facilisis ac congue vel, suscipit sed nisi. In hac habitasse platea dictumst. Nam ut gravida massa. Sed tempus et mauris a pharetra.",
    //     percentageMatch: 13,
    //   },
    //   {
    //     id: 5,
    //     avatar: "https://cdn.vuetifyjs.com/images/lists/5.jpg",
    //     name: "Michael Perk",
    //     age: "26",
    //     story:
    //       "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a dui eleifend, molestie erat et, porttitor nisl. In vulputate accumsan suscipit. In non ante sit amet mauris accumsan pellentesque. Fusce pharetra sodales mattis. Fusce aliquet, urna et eleifend viverra, orci orci faucibus augue, eu bibendum dui lectus non purus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Maecenas tempor urna eros, at pharetra massa suscipit ac. Nullam tempor turpis justo, ac dapibus erat mattis at. Curabitur sagittis commodo lacus, id pharetra purus scelerisque eget. Vestibulum pharetra, mi sed fermentum ultricies, nibh eros varius nunc, fermentum pretium est ligula in lorem. Mauris eget tortor eget lacus volutpat dictum. Praesent quis erat ligula. Donec lectus lorem, facilisis ac congue vel, suscipit sed nisi. In hac habitasse platea dictumst. Nam ut gravida massa. Sed tempus et mauris a pharetra.",
    //     percentageMatch: 1,
    //   },
    // ],
  }),
  methods: {
    contact: (id) => {
      console.log(id);
    },
    getMatchedPersons: function() {
      axios
        .post("http://40.115.33.104:8000/questions/matchmake", {})
        .then((response) => {
          console.log(response.data)
          this.matches = response.data
        });
    },
  },
};
</script>
