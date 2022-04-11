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

    clusterMap: null,
    objectManager: null,
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
  },

  async mounted() {
    await loadYmap({ ...this.settings, debug: true });
  },
};
</script>

<style scoped>
#map {
  width: 1200px;
  height: 600px;
  margin: auto;
}
</style>