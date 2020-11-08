<template>
  <div v-if="chats.length > 0">
    <v-card class="pa-3">
      <v-list two-line>
        <template v-for="item in chats">
          <v-list-item
              @click="openChat"
              :key="item.title">
            <v-list-item-avatar>
              <v-img :src="item.mentor['picture_url']"></v-img>
            </v-list-item-avatar>
            <v-list-item-content>
              <v-list-item-title v-html="item.mentor['first_name']"></v-list-item-title>
              <v-list-item-subtitle v-if="item.mentor['story']" v-html="item.mentor['story'].substring(0, 100)">...</v-list-item-subtitle>
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
    openChat: function () {
      console.log('test')
      let id = 0
      this.$router.push({path: '/chat', query: {'id': id}})
    }
  }
}
</script>

<style scoped>

</style>