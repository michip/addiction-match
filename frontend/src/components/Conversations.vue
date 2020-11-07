<template>
  <v-card class="pa-3">
    <v-list two-line>
      <template v-for="item in chats">
        <v-list-item
            :key="item.title">
          <v-list-item-avatar>
            <v-img :src="item.avatar"></v-img>
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title v-html="item.name"></v-list-item-title>
            <v-list-item-subtitle v-html="item.chat"></v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </template>
    </v-list>
  </v-card>
</template>

<script>
export default {
  name: "Conversations",
  props: ['chats'],
  data: function () {
    return {
    }
  }
}
</script>

<style scoped>

</style>