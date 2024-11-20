<template>
  <div id="app">
    <h1>Flashcard App</h1>
    <button @click="fetchPong">Ping Backend</button>
    <p v-if="message">{{ message }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      message: "",
    };
  },
  methods: {
    async fetchPong() {
      try {
        const response = await axios.get("http://127.0.0.1:5000/api/ping");
        this.message = response.data.message;
      } catch (error) {
        console.error("Error fetching from backend:", error);
        this.message = "Failed to connect to backend!";
      }
    },
  },
};
</script>

<style>
#app {
  text-align: center;
}
</style>
