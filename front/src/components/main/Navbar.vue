<template>
  <div class="mb-6">
    <v-toolbar flat dark class='transparent-navbar'>
      <v-tabs fixed-tabs>
        <v-tab :to="{ name: 'first' }"> Первая </v-tab>
        <v-tab :to="{ name: 'map' }">Карта</v-tab>
        <v-tab :to="{ name: 'scraper' }">Соцсети </v-tab>
        <v-tab :to="{ name: 'photo' }">Поиск места по фото</v-tab>
        <v-tab :to="{ name: 'findclone' }">Поиск страницы по фото</v-tab>
      </v-tabs>
    </v-toolbar>

    <div
      class="color-row"
      :style="'background: ' + $route.meta.theme"
    ></div>
  </div>
</template>


<script>
export default {
  name: "Navbar",
};
</script>


<style lang="scss" scoped >
$navbar-height: 64px;

.color-row {
  height: 500px;
  width: 100%;
  position: absolute;
  margin-top: -$navbar-height;
  z-index: 1;
}

.transparent-navbar {
  background: transparent !important;
  z-index: 2;
  height: $navbar-height;
}
</style>