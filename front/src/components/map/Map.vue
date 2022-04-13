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
    :icon="markerIcon"
    hint-content="some hint"
    marker-type="polyline" 
    :marker-stroke="{width: '5px', color: '#FF0000'}"
  />
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
    markerIcon: {
      layout: 'default#imageWithContent',
      imageHref: 'https://masterprintspb.ru/wp-content/uploads/2014/10/Map-Marker-PNG-File.png',
      imageSize: [43, 43],
      imageOffset: [0, 0],
      content: '123 v12',
      contentOffset: [0, 15],
      contentLayout: '<div style="background: red; width: 50px; color: #FFFFFF; font-weight: bold;">$[properties.iconContent]</div>'
    },
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
  width: 100%;
  height: 100%;
  margin: auto;
}
</style>