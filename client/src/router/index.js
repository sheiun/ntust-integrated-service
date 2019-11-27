import Vue from 'vue';
import VueRouter from 'vue-router';
import Student from '../components/Student.vue';
import SwingCard from '../components/SwingCard.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/student',
    name: 'Student',
    component: Student,
  },
  {
    path: '/card',
    name: 'card',
    component: SwingCard,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
