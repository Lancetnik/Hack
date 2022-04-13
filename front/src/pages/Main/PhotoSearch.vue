<template>
  <v-card flat style="background: transparent">
    <v-row style="z-index: 20">
      <v-col md="3">
        <v-card>
          <v-card-title> Настройки поиска </v-card-title>
          <v-progress-linear
            v-if="this.load==true"
            indeterminate
            :color="$route.meta.theme"
          ></v-progress-linear>
          <v-file-input
            v-model="file"
            class="ma-4"
            truncate-length="15"
            label="Фотка"/>
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
          <v-img :src="url" aspect-ratio="1.7"></v-img>
          <v-card-text>
            <v-btn 
              v-if="points != ''"
              :color="$route.meta.theme"
              class="mt-5 white--text"
              @click="exportExcel"
            >
              Экспортировать
            <v-icon right>
              mdi-apple-keyboard-caps
            </v-icon>
          </v-btn>
          </v-card-text>
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
import { saveExcel } from '@progress/kendo-vue-excel-export';

export default {
  name: "photosearch",
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
      dataphoto: []
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
          this.dataphoto =[{
            'Файл': this.file.name,
            'Широта': this.coordinates[0],
            'Долгота': this.coordinates[1],
          }]
        })
        .finally(()=>{
          this.load = false
      })
    },
    exportExcel () {
      console.log(this.dataphoto);
            saveExcel({
                data: this.dataphoto,
                fileName: "Photolocation.xlsx",
                columns: [
                  { field: 'Файл'},
                  { field: 'Широта'},
                  { field: 'Долгота'},
              ]
            });
        },
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