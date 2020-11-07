<template>
  <v-app>
    <app-bar></app-bar>
    <v-main class="grey lighten-5">
      <v-progress-linear value="15"></v-progress-linear>
      <v-container height="800px" class="d-flex justify-center align-center">
        <div>
          <question-card :question="question" :answers="answers"
                         v-model="selection">
          </question-card>
          <v-btn class="float-left">Previous</v-btn>
          <v-btn class="primary float-right" @click="nextClick">Next</v-btn>
        </div>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>

import QuestionCard from "@/components/QuestionCard";
import AppBar from "@/components/AppBar";

export default {
  name: 'Questionnaire',
  components: {
    AppBar,
    QuestionCard
  },
  data: function () {
    return {
      question: "How are you feeling currently?",
      answers:
          [{
            'id': 1,
            'text': 'I am feeling really great!'
          },
            {
              'id': 2,
              'text': 'Fuck I have to do cocaine'
            },
          ],
      selection: 0
    }
  },
  methods: {
    nextClick: function () {
      console.log(this)
      console.log(this.selection)
    }
  }
}
</script>
