<template>
  <v-card round min-width="600px">
    <v-card-title>
      {{ question.text }}
    </v-card-title>
    <div class="ma-5">
      <v-expand-transition>
        <div v-if="question.type === 'choice'">
          <v-radio-group v-model="selected"
                         v-on:change="change">
            <v-radio
                v-for="answer in question.answers"
                :key="answer.id"
                :label="answer.text"
            ></v-radio>
          </v-radio-group>
        </div>
        <div v-else-if="question.type === 'slider'">
          <v-slider
              :max="question.max"
              :min="question.min"
              :step="question.step"
              ticks
              thumb-label
          ></v-slider>
        </div>
        <div v-else-if="question.type === 'multiple-choice'">
          <v-radio-group multiple v-model="selected"
                         v-on:change="change">
            <v-radio
                v-for="answer in question.answers"
                :key="answer.id"
                :label="answer.text"
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
  props: ['question', 'value'],
  data: function () {
    return {
      'selected': this.value,
    }
  },
  methods: {
    change: function () {
      this.$emit('input', this.selected)
    }
  }
}
</script>
