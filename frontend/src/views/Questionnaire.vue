<template>
  <v-app>
    <app-bar :withoutButtons="true"></app-bar>
    <v-main class="grey lighten-5">
      <v-progress-linear :value="progress"></v-progress-linear>
      <v-container
        style="height: 90%"
        class="d-flex justify-center align-center"
      >
        <transition name="fade">
          <div>
            <question-card v-if="question" :question="question">
            </question-card>
            <v-btn
              class="float-left"
              :disabled="!previousAvailable"
              @click="previousClick"
              >Previous</v-btn
            >
            <v-btn
              class="primary float-right"
              :disabled="!nextAvailable"
              @click="nextClick"
              >Next</v-btn
            >
          </div>
        </transition>
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
  name: "Questionnaire",
  components: {
    AppBar,
    QuestionCard,
  },
  data: function() {
    return {
      questions: [],
      question: null,
      progress: 0,
    };
  },

  created() {
    this.progress = this.$store.state.answeredQuestions.length * 10;
    this.nextQuestion();
  },
  methods: {
    nextClick: function() {
      this.nextQuestion();
    },
    previousClick: function() {
      this.question = this.$store.state.answeredQuestions.pop();
      console.log(this.question);
      this.progress -= 10;
    },
    nextQuestion: async function() {

      const isLoggedIn = this.$store.state.profileInfo !== null
      var pk;
      if(isLoggedIn) {
        pk = this.$store.state.profileInfo.pk;
      }

      if (this.question != null) {
        this.$store.commit("addQuestion", this.question);
      }
      let pastQuestions = this.$store.state.answeredQuestions.map(function(x) {
        return { question: x.pk, result: x.result };
      });
      let response = await axios.post(
        "http://40.115.33.104:8000/questions/next-question", {profile_id: isLoggedIn ? pk : undefined, answer: pastQuestions}
      );
      let question = response.data;
      if (question["last_question"]) {
        this.$router.push({ name: "matches" });
      }
      this.progress = this.progress + 10;
      if (question.style === "radio") {
        question.result = null;
      } else if (question.style === "multiple") {
        question.result = [];
      } else if (question.style === "slider") {
        question.result = question["min_value"];
      }
      this.question = question;
    },
  },
  computed: {
    previousAvailable: function() {
      return this.$store.state.answeredQuestions.length > 0;
    },
    nextAvailable: function() {
      if (this.question == null || this.question.result == null) {
        return false;
      }
      return !(
        this.question.style === "multiple" && this.question.result.length <= 0
      );
    },
  },
};
</script>

<style lang="scss" scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
