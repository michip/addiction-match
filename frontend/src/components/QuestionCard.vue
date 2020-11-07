<template>
  <v-card round min-width="600px">
    <v-card-title>
      {{ question.text }}
    </v-card-title>
    <div class="ma-5">
      <v-expand-transition>
        <div v-if="question.style === 'radio'">
          <v-radio-group v-model="selected" @change="change">
            <v-radio
                v-for="answer in question.answers"
                :key="answer.pk"
                :label="answer.value"
                :value="answer.pk"
            ></v-radio>
          </v-radio-group>
        </div>
        <div v-else-if="question.style === 'slider'">
          <v-slider
              :max="question['max_value']"
              :min="question['min_value']"
              :step="question.step"
              ticks
              thumb-label
              v-model="selected"
              @input="change"
          ></v-slider>
        </div>
        <div v-else-if="question.style === 'multiple'">
          <v-radio-group multiple  :value="selected">
            <v-radio
                v-for="answer in question.answers"
                :key="answer.pk"
                @click="toggleMultiple(answer.pk)"
                :label="answer.value"
                :value="answer.pk"
            ></v-radio>
          </v-radio-group>
        </div>
        <div v-else>
          Unknown question type
        </div>
      </v-expand-transition>
    </div>
  </v-card>
</template>

<script>

export default {
  name: 'QuestionCard',
  components: {},
  props: ['question'],
  data: function () {
    return {
      'selected': this.question.result
    }
  },
  methods: {
    change: function () {
      this.question.result = this.selected
    },
    toggleMultiple: function (id) {
      if (this.selected.includes(id)) {
        this.selected = this.selected.filter((i) => {
          return i !== id;
        });
      } else {
        this.selected.push(id);
      }
      this.change()
    }
  },
  watch: {
    question: function (newVal, oldVal) { // watch it
      this.selected = newVal.result
    }
  }
}
</script>
