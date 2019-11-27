<template>
  <v-card width="344" class="mx-auto" shaped elevation="5" :loading="loading">
    <v-img :src="getImageSrc()" @error="setDefaultImage" height="450"></v-img>
    <v-card-title>{{ student.name }}</v-card-title>
    <v-card-subtitle>{{ student.id }}</v-card-subtitle>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn @click="getRandomStudent" large icon>
        <v-icon>mdi-heart-off</v-icon>
      </v-btn>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-btn @click="getRandomStudent" large icon color="primary">
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <v-spacer></v-spacer>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: 'Student',
  // TODO: props loading / user data / image
  data: () => ({
    loading: true,
    student: { id: '', name: '', image: '' },
  }),
  methods: {
    getRandomStudent() {
      this.loading = true;
      fetch('http://localhost:5000/api/ntust/student/')
        .then((res) => res.json())
        .then((json) => {
          this.student = json;
          this.loading = false;
        });
    },
    getImageSrc() {
      if (!this.student.image) {
        this.setDefaultImage();
      }
      if (this.student.id + '.jpg' != this.student.image) {
        return this.student.image;
      }
      return `http://localhost:5000/static/images/ntust/${this.student.image}`;
    },
    setDefaultImage() {
      this.student.image = require('@/assets/default.png');
    },
  },
  created() {
    this.getRandomStudent();
  },
};
</script>
