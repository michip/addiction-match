<template>
  <v-app>
    <app-bar> </app-bar>
    <v-main class="grey lighten-5">
      <v-container class="d-flex justify-center" style="height: 100%">
        <Chat v-if="visible"
              style="height: 100%;"
              :participants="participants"
              :myself="myself"
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
              @onMessageSubmit="onMessageSubmit"
              @onClose="onClose"/>
      </v-container>
    </v-main>
  </v-app>
</template>


<script>
import {Chat} from 'vue-quick-chat';
import 'vue-quick-chat/dist/vue-quick-chat.css';
import AppBar from "@/components/AppBar";

export default {
  components: {
    Chat,
    AppBar
  },
  props: ['partner'],
  data() {
    return {
      visible: true,
      participants: [
        {
          name: 'Arnaldo',
          id: 1,
          profilePicture: 'https://upload.wikimedia.org/wikipedia/en/thumb/a/a1/NafSadh_Profile.jpg/768px-NafSadh_Profile.jpg'
        },
      ],
      myself: {
        name: 'Matheus S.',
        id: 3,
        profilePicture: 'https://lh3.googleusercontent.com/-G1d4-a7d_TY/AAAAAAAAAAI/AAAAAAAAAAA/AAKWJJPez_wX5UCJztzEUeCxOd7HBK7-jA.CMID/s83-c/photo.jpg'
      },
      messages: [
        {
          content: 'Hello there, can I talk to you?',
          myself: false,
          participantId: 1,
          timestamp: {year: 2019, month: 3, day: 5, hour: 20, minute: 10, second: 3, millisecond: 123},
          type: 'text'
        },
        {
          content: 'Of course ! Feel free to talk to me',
          myself: true,
          participantId: 3,
          timestamp: {year: 2019, month: 4, day: 5, hour: 19, minute: 10, second: 3, millisecond: 123},
          type: 'text'
        },
      ],
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
          width: '30px',
          height: '30px',
          borderRadius: '50%'
        }
      },
      timestampConfig: {
        format: 'HH:mm',
        relative: false
      },
    }
  },
  methods: {
    loadMoreMessages(resolve) {
      setTimeout(() => {
        resolve(this.toLoad); //We end the loading state and add the messages
        //Make sure the loaded messages are also added to our local messages copy or they will be lost
        this.messages.unshift(...this.toLoad);
        this.toLoad = [];
      }, 1000);
    },
    onMessageSubmit: function (message) {
      /*
      * example simulating an upload callback.
      * It's important to notice that even when your message wasn't send
      * yet to the server you have to add the message into the array
      */
      this.messages.push(message);

      /*
      * you can update message state after the server response
      */
      // timeout simulating the request
      setTimeout(() => {
        message.uploaded = true
      }, 2000)
    },
    onClose() {
      this.visible = false;
    },

  }
}
</script>