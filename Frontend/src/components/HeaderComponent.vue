<template>
  <div class="header">
    <input type="text" placeholder="Enter text here" maxlength="1000" v-model="inputText" class="input-field" @keyup.enter="sendData">
    <button @click="sendData" class="button">Submit</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      inputText: ""
    };
  },
  methods: {
    async sendData() {
      const data = { message: this.inputText };
      try {
        const response = await axios.post('http://localhost:8000/message', data);
        console.log(response);
        // Do something with the response from the server
      } catch (error) {
        console.error(error);
        // Handle the error from the server
      }
    }
  }
};
</script>

<style>
/* CSS styling for header component */
</style>
