<template>
  <div class="mb-6">
    <v-toolbar dark :style="'background: ' + $route.meta.theme">
      <v-tabs fixed-tabs>
        <v-tab v-for="header in headers" :key="header.route"
        :to="{ name: header.route }" v-text="header.name"></v-tab>
      </v-tabs>
    </v-toolbar>
  </div>
</template>



<script>
export default {
  name: "Navbar",

  data: () => ({
    headers: [
      { route: "first", name: "Отслеживание номера телефона" },
      { route: "map", name: "Карта" },
      { route: "photo", name: "Поиск места по фото" },
      { route: "findclone", name: "Поиск страницы по фото"}
    ]
  }),
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