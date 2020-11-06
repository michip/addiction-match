
<template>
  <v-app>
    <MatchedPersonsList></MatchedPersonsList>
  </v-app>
</template>

<script>

import MatchedPersonsList from '../components/MatchedPersonsList'

export default {
  name: 'Matches',
  components: { MatchedPersonsList }
}
</script>
