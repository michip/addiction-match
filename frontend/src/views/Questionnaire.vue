<template>
  <v-app>
    <app-bar></app-bar>
    <v-main class="grey lighten-5">
      <v-progress-linear value="15"></v-progress-linear>
      <v-container style="height: 90%" class="d-flex justify-center align-center">
        <div>
          <question-card v-if="question" :question="question">
          </question-card>
          <v-btn class="float-left" :disabled="!previousAvailable" @click="previousClick">Previous</v-btn>
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

const axios = require("axios").default;


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
    this.nextQuestion()
  },
  methods: {
    nextClick: function () {
      this.nextQuestion()
    },
    previousClick: function () {
      this.question = this.$store.state.answeredQuestions.pop()
    },
    nextQuestion: async function () {
      if (this.question != null) {
        this.$store.commit('addQuestion', this.question)
      }
      console.log(this.question)
      let pastQuestions = this.$store.state.answeredQuestions.map(function (x) {
        return {'question': x.pk, 'result': x.result}
      })
      console.log(pastQuestions)
      let response = await axios.post('http://40.115.33.104:8000/questions/next-question', pastQuestions)
      let question = response.data
      console.log(question)
      if (question['last_question']) {
        this.$router.push('/')
      }
      if (question.style === 'choice') {
        question.result = question.answers[0].pk
      } else if (question.style === 'multiple') {
        question.result = []
      } else if (question.style === 'slider') {
        question.result = question.min
      }
      this.question = question
    }
  },
  computed: {
    previousAvailable: function () {
      return this.$store.state.answeredQuestions.length > 0
    }
  }
}
</script>
