<template>
  <VueSwing @throwoutright="like" @throwoutleft="dislike" :config="config">
    <!-- TODO: pass like / dislike function to every card -->
    <div v-for="card in cards" :key="card" :student="card" class="swing-card">
      <Student></Student>
    </div>
  </VueSwing>
</template>

<script>
import VueSwing from 'vue-swing';

import Student from './Student.vue';

export default {
  name: 'SwingCard',
  components: { Student },
  data: () => ({
    cards: [],
    config: {
      allowedDirections: [VueSwing.Direction.LEFT, VueSwing.Direction.RIGHT],
    },
  }),
  methods: {
    like({ target }) {
      //  TODO: send request to backend with auth
      // if not auth / login show alert dialog to announce to login
      console.log(target);
      this.remove();
    },
    dislike({ target }) {
      // TODO:　same as like
      console.log(target);
      this.remove();
    },
    remove() {
      //
      setTimeout(() => {
        this.cards.pop();
      }, 100);
    },
  },
  created() {
    // TODO: push 5 students to card
    this.cards.push();
  },
};
</script>

<style scoped>
.swing-card {
  position: absolute;
  position: absolute;
  left: calc(50% - 172px);
  top: calc(50% - 300px);
}
</style>
