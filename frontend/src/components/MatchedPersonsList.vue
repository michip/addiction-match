<template>
  <v-container fill-height fluid>
    <v-card max-width="1000" class="mx-auto justify-center">
      <v-expansion-panels three-line>
        <template v-for="item in matches">
          <v-expansion-panel :key="item.name">
            <v-expansion-panel-header>
              <v-row align="center" class="spacer" no-gutters>
                <v-col cols="1" sm="1" md="1">
                  <v-avatar>
                    <img v-if="item.avatar" alt="Avatar" :src="item.avatar" />
                  </v-avatar>
                </v-col>
                <v-col cols="9" sm="9" md="9">
                  <span>{{ item.name }}, {{ item.age }}</span>
                </v-col>
                <v-col cols="2" sm="2" md="2">
                  <v-progress-circular
                    :rotate="360"
                    :size="50"
                    :width="7"
                    :value="item.percentageMatch"
                    color="teal"
                  >
                    {{ item.percentageMatch }}
                  </v-progress-circular>
                </v-col>
              </v-row>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-row align="center" class="spacer" no-gutters>
                <p>{{ item.story }}</p>
              </v-row>
              <div class="d-flex justify-end">
                <v-btn elevation="2" color="primary">CONTACT</v-btn>
              </div>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </template>
      </v-expansion-panels>
    </v-card>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    matches: [
      {
        avatar: "https://cdn.vuetifyjs.com/images/lists/1.jpg",
        name: "Piotr Proszowski",
        age: "23",
        story:
          "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a dui eleifend, molestie erat et, porttitor nisl. In vulputate accumsan suscipit. In non ante sit amet mauris accumsan pellentesque. Fusce pharetra sodales mattis. Fusce aliquet, urna et eleifend viverra, orci orci faucibus augue, eu bibendum dui lectus non purus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Maecenas tempor urna eros, at pharetra massa suscipit ac. Nullam tempor turpis justo, ac dapibus erat mattis at. Curabitur sagittis commodo lacus, id pharetra purus scelerisque eget. Vestibulum pharetra, mi sed fermentum ultricies, nibh eros varius nunc, fermentum pretium est ligula in lorem. Mauris eget tortor eget lacus volutpat dictum. Praesent quis erat ligula. Donec lectus lorem, facilisis ac congue vel, suscipit sed nisi. In hac habitasse platea dictumst. Nam ut gravida massa. Sed tempus et mauris a pharetra.",
        percentageMatch: 97,
      },
      {
        avatar: "https://cdn.vuetifyjs.com/images/lists/2.jpg",
        name: "Oscar Che",
        age: `26`,
        story:
          "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a dui eleifend, molestie erat et, porttitor nisl. In vulputate accumsan suscipit. In non ante sit amet mauris accumsan pellentesque. Fusce pharetra sodales mattis. Fusce aliquet, urna et eleifend viverra, orci orci faucibus augue, eu bibendum dui lectus non purus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Maecenas tempor urna eros, at pharetra massa suscipit ac. Nullam tempor turpis justo, ac dapibus erat mattis at. Curabitur sagittis commodo lacus, id pharetra purus scelerisque eget. Vestibulum pharetra, mi sed fermentum ultricies, nibh eros varius nunc, fermentum pretium est ligula in lorem. Mauris eget tortor eget lacus volutpat dictum. Praesent quis erat ligula. Donec lectus lorem, facilisis ac congue vel, suscipit sed nisi. In hac habitasse platea dictumst. Nam ut gravida massa. Sed tempus et mauris a pharetra.",
        percentageMatch: 63,
      },
      {
        avatar: "https://cdn.vuetifyjs.com/images/lists/3.jpg",
        name: "Ali Connors",
        age: "23",
        story:
          "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a dui eleifend, molestie erat et, porttitor nisl. In vulputate accumsan suscipit. In non ante sit amet mauris accumsan pellentesque. Fusce pharetra sodales mattis. Fusce aliquet, urna et eleifend viverra, orci orci faucibus augue, eu bibendum dui lectus non purus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Maecenas tempor urna eros, at pharetra massa suscipit ac. Nullam tempor turpis justo, ac dapibus erat mattis at. Curabitur sagittis commodo lacus, id pharetra purus scelerisque eget. Vestibulum pharetra, mi sed fermentum ultricies, nibh eros varius nunc, fermentum pretium est ligula in lorem. Mauris eget tortor eget lacus volutpat dictum. Praesent quis erat ligula. Donec lectus lorem, facilisis ac congue vel, suscipit sed nisi. In hac habitasse platea dictumst. Nam ut gravida massa. Sed tempus et mauris a pharetra.",
        percentageMatch: 54,
      },
      {
        avatar: "https://cdn.vuetifyjs.com/images/lists/4.jpg",
        name: "Jonas Dippel",
        age: "25",
        story:
          "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a dui eleifend, molestie erat et, porttitor nisl. In vulputate accumsan suscipit. In non ante sit amet mauris accumsan pellentesque. Fusce pharetra sodales mattis. Fusce aliquet, urna et eleifend viverra, orci orci faucibus augue, eu bibendum dui lectus non purus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Maecenas tempor urna eros, at pharetra massa suscipit ac. Nullam tempor turpis justo, ac dapibus erat mattis at. Curabitur sagittis commodo lacus, id pharetra purus scelerisque eget. Vestibulum pharetra, mi sed fermentum ultricies, nibh eros varius nunc, fermentum pretium est ligula in lorem. Mauris eget tortor eget lacus volutpat dictum. Praesent quis erat ligula. Donec lectus lorem, facilisis ac congue vel, suscipit sed nisi. In hac habitasse platea dictumst. Nam ut gravida massa. Sed tempus et mauris a pharetra.",
        percentageMatch: 13,
      },
      {
        avatar: "https://cdn.vuetifyjs.com/images/lists/5.jpg",
        name: "Michael Perk",
        age: "26",
        story:
          "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a dui eleifend, molestie erat et, porttitor nisl. In vulputate accumsan suscipit. In non ante sit amet mauris accumsan pellentesque. Fusce pharetra sodales mattis. Fusce aliquet, urna et eleifend viverra, orci orci faucibus augue, eu bibendum dui lectus non purus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Maecenas tempor urna eros, at pharetra massa suscipit ac. Nullam tempor turpis justo, ac dapibus erat mattis at. Curabitur sagittis commodo lacus, id pharetra purus scelerisque eget. Vestibulum pharetra, mi sed fermentum ultricies, nibh eros varius nunc, fermentum pretium est ligula in lorem. Mauris eget tortor eget lacus volutpat dictum. Praesent quis erat ligula. Donec lectus lorem, facilisis ac congue vel, suscipit sed nisi. In hac habitasse platea dictumst. Nam ut gravida massa. Sed tempus et mauris a pharetra.",
        percentageMatch: 1,
      },
    ],
    interval: {},
    value: 0
  })
  };
</script>
