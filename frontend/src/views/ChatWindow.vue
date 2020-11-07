<template>
  <v-app>
    <app-bar>
      <v-spacer></v-spacer>
      <v-responsive max-width="260">
        <v-btn outlined rounded @click="login">Log Out</v-btn>
      </v-responsive>
    </app-bar>
    <v-main class="grey lighten-5">
      <v-container class="d-flex justify-center">
        <Chat v-if="visible"
              style="height: 700px; max-width: 800px"
              :participants="participants"
              :myself="myself"
              :messages="messages"
              :chat-title="chatTitle"
              :placeholder="placeholder"
              :colors="colors"
              :border-style="borderStyle"
              :hide-close-button="hideCloseButton"
              :submit-icon-size="submitIconSize"
              :submit-image-icon-size="submitImageIconSize"
              :load-more-messages="toLoad.length > 0 ? loadMoreMessages : null"
              :async-mode="asyncMode"
              :scroll-bottom="scrollBottom"
              :display-header="true"
              :send-images="false"
              :profile-picture-config="profilePictureConfig"
              :timestamp-config="timestampConfig"
              @onMessageSubmit="onMessageSubmit"
              @onType="onType"
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
      chatTitle: 'Discussing with my guardian angel',
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
      toLoad: [
        {
          content: 'Hey, John Doe! How are you today?',
          myself: false,
          participantId: 2,
          timestamp: {year: 2011, month: 3, day: 5, hour: 10, minute: 10, second: 3, millisecond: 123},
          uploaded: true,
          viewed: true,
          type: 'text'
        },
        {
          content: "Hey, Adam! I'm feeling really fine this evening.",
          myself: true,
          participantId: 3,
          timestamp: {year: 2010, month: 0, day: 5, hour: 19, minute: 10, second: 3, millisecond: 123},
          uploaded: true,
          viewed: true,
          type: 'text'
        },
      ],
      scrollBottom: {
        messageSent: true,
        messageReceived: true
      },
      displayHeader: false,
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
    onType: function (event) {
      //here you can set any behavior
    },
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