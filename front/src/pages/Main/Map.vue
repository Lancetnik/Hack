<template>
  <v-card flat style="background: transparent">
    <Map :points='points'/>
  </v-card>
</template>


<script>
import Map from "@/components/map/Map.vue";

export default {
  components: {
    Map,
  },

  data: () => ({
    points: [],
  }),

  async created() {
    this.$http.get('geo/position/1/').then((response) => {
      console.log(response.data)
      this.points.push(response.data)
    })
  }
};
</script>


<style lang="scss">
</style>