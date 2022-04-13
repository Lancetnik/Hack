<template>
  <yandex-map
    id="map"
    :settings="settings"
    :coords="center"
    :zoom="zoom"
    :use-object-manager="true"
    :controls="['zoomControl']"
    @map-was-initialized="getMapInstance"
  >
  <ymap-marker 
    :coords="coords" 
    marker-id="123" 
    hint-content="some hint"
    marker-type="polyline" 
    :icon="markerIcon"
    :marker-stroke="{width: '5px', color: '#FF0000'}"
    @click="dialog=true"
  >
    <v-row justify="center">
      <v-dialog
        v-model="dialog"
        persistent
        max-width="330px"
      >
        <v-card>
          <v-card-title>
            Данные о точке:
          </v-card-title>
          <v-card-actions>
            <v-btn class="mr-4" type="submit" @click="analyze_strava(points)" dark color="green">
              Анализ Strava
            </v-btn>
            <v-btn class="mr-4" type="submit" right @click="dialog=false" dark color="green">
              Закрыть
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
  </ymap-marker>
  </yandex-map>
</template>


<script>
/* eslint-disable */
import { yandexMap } from "vue-yandex-maps";
import { loadYmap } from "vue-yandex-maps";

export default {
  name: "Map",

  

  props: {
    points: Array,
    coords: Array,

    center: {
      type: Array,
      default: () => { return [59.937, 30.3089] }
    },

    zoom:{
      type: Number,
      default: 10
    },
  },

  components: {
    yandexMap,
  },

  watch: {
    points(val) {
      this.setPoints(val);
    },

    center(val) {
      this.clusterMap.setCenter(val, this.zoom)
    },

    zoom(val) {
      this.clusterMap.setCenter(this.center, val)
    }
  },

  data: () => ({
    settings: {
      apiKey: "e70694c3-ce7f-4459-b7f6-be3d53e2cc8e",
      lang: "ru_RU",
      coordorder: "latlong",
      enterprise: false,
      version: "2.1",
    },
    dialog: false,
    clusterMap: null,
    objectManager: null,
    markerIcon: {
      layout: 'default#imageWithContent',
      imageHref: 'https://masterprintspb.ru/wp-content/uploads/2014/10/Map-Marker-PNG-File.png',
      imageSize: [43, 43],
      imageOffset: [0, 0],
      content: '123 v12',
      contentOffset: [0, 15],
      contentLayout: '<div style="background: red; width: 50px; color: #FFFFFF; font-weight: bold;">$[properties.iconContent]</div>'
    },
  }),

  methods: {
    async clickPoint(e) {
      let target = e.get("objectId");
      if (this.objectManager.clusters.getById(target)) {
        let cluster = this.objectManager.clusters.getById(target);
        console.log("cluster clicked");
        let objects = cluster.properties.geoObjects;
      } else {
        let point = this.objectManager.objects.getById(target);
        console.log("point clicked");
        this.dialog = true
      }
    },

    async getMapInstance(map) {
      if (map) {
        try {
          this.clusterMap = map;
          this.clusterMap.geoObjects.events.add("click", (e) =>
            this.clickPoint(e)
          );

          this.objectManager = new ymaps.ObjectManager({
            clusterize: true,
            gridSize: 32,
            clusterDisableClickZoom: true,
          });
          this.clusterMap.geoObjects.add(this.objectManager);

          this.setPoints(this.points);
        } catch (error) {
          console.log(error);
        }
      }
    },

    setPoints(points) {
      if (this.clusterMap) {
        this.objectManager.removeAll()
        try {
          this.objectManager.add(points);
        } catch (error) {
          console.log("no points!");
        }
      }
    },
    analyze_strava(points) {
      this.$router.push({name: 'strava', params:{
        latitude_1: points[0].geometry.coordinates[0] - 0.005, 
        longitude_1: points[0].geometry.coordinates[1] - 0.005,
        latitude_2: points[0].geometry.coordinates[0] + 0.005,
        longitude_2: points[0].geometry.coordinates[1] + 0.005  
          },
        center: [points[0].geometry.coordinates[0], points[0].geometry.coordinates[1]]
        }
      ); 
    }
  },

  async mounted() {
    await loadYmap({ ...this.settings, debug: true });
  },
};
</script>

<style scoped>
#map {
  width: 100%;
  height: 100%;
  margin: auto;
}
</style>