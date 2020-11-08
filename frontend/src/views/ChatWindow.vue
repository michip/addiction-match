<template>
  <v-app>
    <app-bar :includeDashboard="true">
    </app-bar>
    <v-main class="grey lighten-5">
      <v-container class="d-flex justify-center" style="height: 100%">
        <Chat v-if="visible"
              style="height: 100%;"
              :participants="participants"
              :myself="user"
              :messages="messages"
              :placeholder="placeholder"
              :colors="colors"
              :border-style="borderStyle"
              :hide-close-button="hideCloseButton"
              :submit-icon-size="submitIconSize"
              :async-mode="asyncMode"
              :scroll-bottom="scrollBottom"
              :display-header="false"
              :send-images="false"
              :profile-picture-config="profilePictureConfig"
              :timestamp-config="timestampConfig"
              @onMessageSubmit="onMessageSubmit"/>
      </v-container>
    </v-main>
  </v-app>
</template>


<script>
import {Chat} from 'vue-quick-chat';
import 'vue-quick-chat/dist/vue-quick-chat.css';
import AppBar from "@/components/AppBar";
import config from "@/config";

const axios = require("axios").default;

export default {
  components: {
    Chat,
    AppBar
  },
  props: ['id'],
  data() {
    return {
      visible: true,
      participants: [],
      user: {
        name: '',
        id: 0,
        profilePicture: ''
      },
      messages: [],
      placeholder: 'Say something',
      colors: {
        header: {
          bg: '#d30303',
          text: '#fff'
        },
        message: {
          myself: {
            bg: '#fff',
            text: '#000000'
          },
          others: {
            bg: '#fb4141',
            text: '#ffff'
          },
          messagesDisplay: {
            bg: '#f7f3f3'
          }
        },
        submitIcon: '#b91010',
        submitImageIcon: '#b91010',
      },
      borderStyle: {
        topLeft: "10px",
        topRight: "10px",
        bottomLeft: "10px",
        bottomRight: "10px",
      },
      hideCloseButton: true,
      submitIconSize: 25,
      closeButtonIconSize: "20px",
      asyncMode: false,
      scrollBottom: {
        messageSent: true,
        messageReceived: true
      },
      profilePictureConfig: {
        others: true,
        myself: true,
        styles: {
          width: '50px',
          height: '50px',
          borderRadius: '50%'
        }
      },
      timestampConfig: {
        format: 'YYYHH:mm',
        relative: false
      },
    }
  },
  mounted: function () {
    this.initialize()
    window.setInterval(this.updateMessages, 5000);
  },
  methods: {
    initialize: async function () {
      const url = config.baseUrl + '/conversations/' + this.id + '/'
      let response = await axios.get(url)
      const data = response.data
      const userId = this.$store.state.profileInfo.pk
      let user = null;
      let participant = null;
      if (data.inquire.pk === userId) {
        user = data.inquire
        participant = data.mentor
      } else {
        user = data.mentor
        participant = data.inquire
      }

      function mapUser(data) {
        return {
          'profilePicture': data['picture_url'],
          'name': data['first_name'],
          'id': data.pk,
          'timestamp': data.time
        }
      }
      this.user = mapUser(user)
      this.participants = [mapUser(participant)]
      this.updateMessages()
    },
    updateMessages: async function () {
      const url = config.baseUrl + '/conversations/' + this.id + '/'
      let response = await axios.get(url)
      this.messages = response.data['messages'].map(function (msg) {
        return {
          'content': msg.text,
          'participantId': msg.sender,
          'uploaded': true,
          'type': 'text',
        }
      })
    },
    onMessageSubmit: async function (message) {
      /*
      * example simulating an upload callback.
      * It's important to notice that even when your message wasn't send
      * yet to the server you have to add the message into the array
      */
      console.log(message)
      const url = config.baseUrl + '/conversations/messages/send'
      const values = {
        'sender': message.participantId,
        'conversation': parseInt(this.id),
        'text': message.content
      }
      console.log(values)
      let response = await axios.post(url, values)
      if (response.status === 200) {
        message.uploaded = true
        this.messages.push(message);
      }
      /*
      * you can update message state after the server response
      */
      // timeout simulating the request
      setTimeout(() => {
        message.uploaded = true
      }, 2000)
    },
  }
}
</script>