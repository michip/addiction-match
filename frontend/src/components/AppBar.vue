<template>
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
      <slot>
      </slot>
    </v-container>
  </v-app-bar>
</template>

<script>
export default {
  name: 'AppBar',
  components: {},
}
</script>