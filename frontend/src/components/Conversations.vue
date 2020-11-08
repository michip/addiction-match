<template>
  <div v-if="chats.length > 0">
    <v-card class="pa-3">
      <v-list two-line>
        <template v-for="item in chats">
          <v-list-item
              @click="openChat(item)"
              :key="item.name">
            <v-list-item-avatar>
              <v-img :src="item.picture"></v-img>
            </v-list-item-avatar>
            <v-list-item-content>
              <v-list-item-title v-html="item.name"></v-list-item-title>
              <v-list-item-subtitle v-if="item.msg">...
              </v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </template>
      </v-list>
    </v-card>
  </div>
</template>

<script>
export default {
  name: "Conversations",
  props: ['chats'],
  data: function () {
    return {}
  },
  methods: {
    openChat: function (item) {
      let id = 0
      this.$router.push({path: '/chat', query: {'id': item.pk}})
    }
  }
}
</script>

<style scoped>

</style>