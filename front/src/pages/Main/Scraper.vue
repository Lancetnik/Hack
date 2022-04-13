<template>
  <v-card>
    <h1>WebSocke Chat</h1>

    <v-text-field v-model="text"></v-text-field>
    <v-btn @click="sendMessage(text)">Send</v-btn>

    <ul>
      <li v-for="(message, i) in messages" :key="i">
        {{ message }}
      </li>
    </ul>
  </v-card>
</template>



<script>
export default {
  data: () => ({
    ws: null,
    text: "",
    messages: [],
  }),

  methods: {
    sendMessage(text) {
      this.ws.send(text);
      this.text = "";
    },
  },

  created() {
    this.ws = new WebSocket("ws://localhost:8001/ws/test/1");

    this.ws.onopen = () => {
      console.log('connected')
    };

    this.ws.onmessage = (event) => {
      this.messages.push(event.data);
    };

    this.ws.onerror = () => {
      this.ws.close();
    };
  },
};
</script>


<style lang="scss">
</style>