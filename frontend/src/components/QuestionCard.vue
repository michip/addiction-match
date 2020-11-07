<template>
  <v-card round min-width="600px">
    <v-card-title>
      {{ question }}
    </v-card-title>
    <div class="ma-5">
      <v-radio-group v-model="selected"
                     v-on:change="change">
        <v-radio
            v-for="answer in answers"
            :key="answer.id"
            :label="answer.text"
        ></v-radio>
      </v-radio-group>
    </div>
  </v-card>
</template>

<script>

export default {
  name: 'QuestionCard',
  components: {},
  props: ['question', 'answers', 'value'],
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
