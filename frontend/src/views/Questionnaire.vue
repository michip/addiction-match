<template>
  <v-app>
    <app-bar></app-bar>
    <v-main class="grey lighten-5">
      <v-progress-linear value="15"></v-progress-linear>
      <v-container style="height: 90%" class="d-flex justify-center align-center">
        <div>
          <question-card :question="question">
          </question-card>
          <v-btn class="float-left" disabled @click="previousClick">Previous</v-btn>
          <v-btn class="primary float-right" @click="nextClick">Next</v-btn>
        </div>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>

import QuestionCard from "@/components/QuestionCard";
import AppBar from "@/components/AppBar";
import questionsStore from "@/questionsStore";

export default {
  name: 'Questionnaire',
  components: {
    AppBar,
    QuestionCard
  },
  data: function () {
    return {
      questions: [],
      question: null
    }
  },

  created() {
    console.log(this.$store.state.answeredQuestions)
    this.nextQuestion()
  },
  methods: {
    nextClick: function () {
      this.nextQuestion()
    },
    previousClick: function () {
      this.nextQuestion()
    },
    nextQuestion: function () {
      if (this.question != null) {
        this.$store.commit('addQuestion', this.question)
      }
      let question = questionsStore.getNewQuestion()
      if (question.type === 'choice') {
        question.result = 0
      } else if (question.type === 'multiple-choice') {
        question.result = []
      } else if (question.type === 'slider') {
        question.result = question.min
      }
      this.question = question
    }
  }
}
</script>
