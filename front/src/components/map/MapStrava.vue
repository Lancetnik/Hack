<template>

  <yandex-map
    id="map"
    :settings="settings"
    :coords="center"
    :zoom="10"
    :use-object-manager="true"
    :controls="['zoomControl']"
    @map-was-initialized="getMapInstance"
  >
  <ymap-marker 
      
      :coords="coords" 
      marker-id="123" 
      :hint-content="user"
      marker-type="polyline" 
      :marker-stroke="{width: '5px',
      color: '#FF0000', 
      }"
    />
  <ymap-marker 
      :coords="first_coord" 
      marker-id="124" 
      hint-content="some hint"
      :icon="markerIcon"
    />
  </yandex-map>
</template>


<script>
/* eslint-disable */
import { yandexMap, ymapMarker } from "vue-yandex-maps";
import { loadYmap } from "vue-yandex-maps";

export default {
  name: "Map",
  props: {
    points: Array,
    created: Array,
    coords: Array,
    first_coord: Array,
    user: String,
    center: {
      type: Array,
      default: () => { return [59.937, 30.3089] }
    },

    zoom:{
      type: Number,
      default: 30
    },
  },
    watch: {
    center(val) {
      this.clusterMap.setCenter(val, this.zoom)
    },

    zoom(val) {
      this.clusterMap.setCenter(this.center, val)
    },
    first_coord(val) {
      this.setPoints(val);
    },
  },
  components: {
    yandexMap, ymapMarker
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
    markerIcon: {
      layout: 'default#imageWithContent',
      imageHref: 'https://image.flaticon.com/icons/png/512/33/33447.png',
      imageSize: [70, 70],
      imageOffset: [0, 0],
      content: 'Объект',
      contentOffset: [0, 15],
      contentLayout: '<div style="background: red; border-radius: 10px; width: 50px; color: #FFFFFF; font-weight: bold;">$[properties.iconContent]</div>'
    },
    center: [59.937, 30.3089],
    clusterMap: null,
    objectManager: null,
    coords: [
        ]
    // coordinates: 
    
  }),
  

  methods: {
    async mounted() {
      const settings = { lang: 'en_US' };
      await loadYmap(settings);
      console.log(ymaps); 
  },
    async clickPoint(e) {
      let target = e.get("objectId");
      if (this.objectManager.clusters.getById(target)) {
        let cluster = this.objectManager.clusters.getById(target);
        console.log('cluster clicked')
        let objects = cluster.properties.geoObjects;
      } else {
        let point = this.objectManager.objects.getById(target);
        console.log('point clicked')
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
  width: 800px;
  height: 600px;
  margin: auto;
}
</style>