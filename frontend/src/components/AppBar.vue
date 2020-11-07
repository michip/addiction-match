<template>
  <v-app-bar
      app
      color="white"
      flat>
    <v-container class="py-0 fill-height">
        <v-img
            max-width="200px"
            src="/logo_navbar.png">
        </v-img>
      <slot>
      </slot>
    </v-container>
  </v-app-bar>
</template>

<script>
export default {
  name: 'AppBar',
  components: {},
  methods: {
    home: function () {
      this.$router.push('/')
    }
  }
}
</script>