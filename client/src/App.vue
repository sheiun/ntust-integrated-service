<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <div class="headline">抽卡</div>
      <div class="d-flex align-center">
        <v-img
          alt="Logo"
          class="shrink mr-2"
          src=""
          transition="scale-transition"
          width="40"
        />

        <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src=""
          width="100"
        />
      </div>

      <v-spacer></v-spacer>

      <v-btn href="" target="_blank" text>
        <span class="mr-2">Join Us</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-content>
      <v-container fill-height grid-list-md text-xs-center>
        <v-layout column wrap align-center>
          <router-view />
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: 'App',
};
</script>
