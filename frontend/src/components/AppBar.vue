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
            src="require('../assets/logo_navbar.png')">
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