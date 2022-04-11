<template>
  <v-row style="z-index: 20;">
    <v-col md="3">
      <v-card>
        <v-card-title>
          Панель управления
        </v-card-title>
        <v-file-input v-model='file'/>
        <v-divider />
        <v-card-actions>
          <v-btn
            color="blue-grey"
            class="ma-2 white--text"
            @click="submitFile()"
          >
            Загрузить
            <v-icon right>
              mdi-cloud-upload
            </v-icon>
          </v-btn>
        </v-card-actions>
      </v-card>
      <br>
      <v-card>
        <v-card-text>Location: {{points}}</v-card-text>
        <v-img
          :src="url"
          aspect-ratio="1.7"
        ></v-img>
      </v-card>
      </v-col>
      
      <v-col md="4">
        <v-card flat style="background: transparent">
          <Map :points='points'/>
        </v-card>
      </v-col>
  </v-row>
</template>



<script>
import Map from "@/components/map/Map.vue";
import axios from 'axios';

export default {
  name: "Page4",
  components: {
    Map,
  },

  data() {
    return {
      // points: [59.937, 30.3089],
      file: '',
      points: [],
      news: ["https://www.iguides.ru/upload/medialibrary/9f8/9f8fdff471b7d281f81f694c100b5adc.png"],
    }
  },

  methods: {
    handleFilesUpload() {
      this.file = this.$refs.file.files[0];
    },
    async submitFile() {
      let formData = new FormData();
      formData.append('file', this.file);
      axios.post('http://127.0.0.1:8000/geo/single-file/',
        formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }
      ).then((response) => {
        this.points.push(response.data)
      })
      console.log(this.points)
    },
  },
  computed: {
    url() {
        if (!this.file) return;
        return URL.createObjectURL(this.file);
    }
  }
};
</script>


<style lang="scss">
</style>