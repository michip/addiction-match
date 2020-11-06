<template>
  <v-container fill-height fluid>
    <v-card max-width="1000" class="mx-auto justify-center">
      <v-expansion-panels three-line>
        <template v-for="(item, index) in items">
          <v-subheader
            v-if="item.header"
            :key="item.header"
            v-text="item.header"
          ></v-subheader>

          <v-divider
            v-else-if="item.divider"
            :key="index"
            :inset="item.inset"
          ></v-divider>

          <v-expansion-panel v-else :key="item.name">
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
              </v-row>
            </v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-row align="center" class="spacer" no-gutters>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                enim ad minim veniam, quis nostrud exercitation ullamco laboris
                nisi ut aliquip ex ea commodo consequat.
              </v-row>
              <div class="d-flex justify-end">
                <v-btn elevation="2">CONTACT</v-btn>
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
    items: [
      {
        avatar: "https://cdn.vuetifyjs.com/images/lists/1.jpg",
        name: "Piotr Proszowski",
        age: "23",
      },
      { divider: true, inset: true },
      {
        avatar: "https://cdn.vuetifyjs.com/images/lists/2.jpg",
        name: "Oscar Che",
        age: `26`,
      },
      { divider: true, inset: true },
      {
        avatar: "https://cdn.vuetifyjs.com/images/lists/3.jpg",
        name: "Ali Connors",
        age: "23",
      },
      { divider: true, inset: true },
      {
        avatar: "https://cdn.vuetifyjs.com/images/lists/4.jpg",
        name: "Jonas Dippel",
        age: "25",
      },
      { divider: true, inset: true },
      {
        avatar: "https://cdn.vuetifyjs.com/images/lists/5.jpg",
        name: "Michael Perk",
        age: "26",
      },
    ],
  }),
};
</script>
