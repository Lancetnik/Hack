<template>
  <v-card flat style="background: transparent">
    <v-row style="z-index: 20">
      <v-col md="3">
        <v-card>
          <v-card-title> Панель управления </v-card-title>
          <v-progress-linear
            v-if="this.load==true"
            indeterminate
            :color="$route.meta.theme"
          ></v-progress-linear>
          <v-file-input v-model="file" />
          <v-card-actions>
            <v-btn
              :color="$route.meta.theme"
              class="ma-2 white--text"
              @click="submitFile()"
            >
              Загрузить
              <v-icon right> mdi-cloud-upload </v-icon>
            </v-btn>
          </v-card-actions>
        </v-card>
        <br />
        <v-card>
          <v-card-title>Исходные данные {{ coordinates }}</v-card-title>
          <v-img :src="url" aspect-ratio="1.7"></v-img>
        </v-card>
      </v-col>

      <v-col md="9">
        <v-card flat style="background: transparent">
          <Map :points="points" :center="center" :zoom='zoom' style='height: 650px; width: 100%'/>
        </v-card>
      </v-col>
    </v-row>
  </v-card>
</template>



<script>
import Map from "@/components/map/Map.vue";

export default {
  components: {
    Map,
  },

  data() {
    return {
      file: null,
      points: '',
      coordinates:'',
      news: [
        "https://www.iguides.ru/upload/medialibrary/9f8/9f8fdff471b7d281f81f694c100b5adc.png",
      ],

      center: [59.937, 30.3089],
      zoom: 10,
      load: false,
    };
  },

  methods: {
    handleFilesUpload() {
      this.file = this.$refs.file.files[0];
    },
    async submitFile() {
      this.load = true
      let formData = new FormData();
      formData.append("file", this.file);
      this.$http
        .post("geo/single-file/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          this.points = [response.data];
          this.coordinates = response.data.geometry.coordinates
          this.center = response.data.geometry.coordinates;
          this.zoom = 12;
        })
        .finally(()=>{
          this.load = false
      })
    }
  },

  computed: {
    url() {
      if (!this.file) return;
      return URL.createObjectURL(this.file);
    },
  },
};
</script>


<style lang="scss">
</style>