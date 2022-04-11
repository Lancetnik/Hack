<template>
  <v-card flat style="background: transparent">
    <v-container grid-list-xl>
      <v-row>
        <v-col md="3">
          <v-card>
            <v-card-title> Настройка поиска: </v-card-title>
            <v-card-text>
              <v-select :items="['Вк', 'Instagram']" label="Социальная сеть">
              </v-select>
              <v-file-input
                truncate-length="15"
                label="Фотка"
                v-model="photo"
              ></v-file-input>
            </v-card-text>
            <v-card-actions>
              <v-btn class="primary" @click="find_user"> Найти страницу </v-btn>
            </v-card-actions>
          </v-card>
          <br />
          <v-card>
            <v-card-title> Исходное фото </v-card-title>
            <v-card-text>
              <v-img height="250" :src="url"> </v-img>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col md="9" v-if="load == true">
          <div class="text-center" justify-center>
            <v-progress-circular
              :size="70"
              :width="7"
              color="purple"
              indeterminate
            ></v-progress-circular>
          </div>
        </v-col>
        <v-col md="9" v-if="load == false">
          <v-data-iterator
            :items="items"
            :items-per-page.sync="itemsPerPage"
            :page.sync="page"
            :search="search"
            :sort-by="sortBy.toLowerCase()"
            :sort-desc="sortDesc"
            hide-default-footer
          >
            <template v-slot:header>
              <v-toolbar dark color="blue darken-3" class="mb-1">
                <v-text-field
                  v-model="search"
                  clearable
                  flat
                  solo-inverted
                  hide-details
                  prepend-inner-icon="mdi-magnify"
                  label="Поиск"
                ></v-text-field>
                <template v-if="$vuetify.breakpoint.mdAndUp">
                  <v-spacer></v-spacer>
                  <v-spacer></v-spacer>
                  <v-btn-toggle v-model="sortDesc" mandatory>
                    <v-btn large depressed color="blue" :value="false">
                      <v-icon>mdi-arrow-up</v-icon>
                    </v-btn>
                    <v-btn large depressed color="blue" :value="true">
                      <v-icon>mdi-arrow-down</v-icon>
                    </v-btn>
                  </v-btn-toggle>
                </template>
              </v-toolbar>
            </template>
            <v-spacer></v-spacer>
            <template v-slot:default="props">
              <v-row>
                <v-col
                  v-for="item in props.items"
                  :key="item.title"
                  cols="12"
                  sm="6"
                  md="4"
                  lg="3"
                >
                  <v-card
                    :href="item.url"
                    target="_blank"
                    hover
                    height="100%"
                    class="card-outter"
                  >
                    <v-img height="250" :src="item.photo"></v-img>
                    <v-card-title class="subheading font-weight-bold">
                      {{ item.name }}
                    </v-card-title>
                    <v-divider class="mx-4"></v-divider>
                    <v-card-text> Cходство: {{ item.score }} </v-card-text>
                  </v-card>
                </v-col>
              </v-row>
            </template>

            <template v-slot:footer>
              <v-row class="mt-2" align="center" justify="center">
                <span class="grey--text">Items per page</span>
                <v-menu offset-y>
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn
                      dark
                      text
                      color="primary"
                      class="ml-2"
                      v-bind="attrs"
                      v-on="on"
                    >
                      {{ itemsPerPage }}
                      <v-icon>mdi-chevron-down</v-icon>
                    </v-btn>
                  </template>
                  <v-list>
                    <v-list-item
                      v-for="(number, index) in itemsPerPageArray"
                      :key="index"
                      @click="updateItemsPerPage(number)"
                    >
                      <v-list-item-title>{{ number }}</v-list-item-title>
                    </v-list-item>
                  </v-list>
                </v-menu>

                <v-spacer></v-spacer>

                <span class="mr-4 grey--text">
                  Page {{ page }} of {{ numberOfPages }}
                </span>
                <v-btn
                  fab
                  dark
                  color="blue darken-3"
                  class="mr-1"
                  @click="formerPage"
                >
                  <v-icon>mdi-chevron-left</v-icon>
                </v-btn>
                <v-btn
                  fab
                  dark
                  color="blue darken-3"
                  class="ml-1"
                  @click="nextPage"
                >
                  <v-icon>mdi-chevron-right</v-icon>
                </v-btn>
              </v-row>
            </template>
          </v-data-iterator>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>



<script>
export default {
  data() {
    return {
      // Таблица с новостями
      itemsPerPageArray: [4, 8, 12],
      search: "",
      filter: {},
      sortDesc: false,
      page: 1,
      itemsPerPage: 12,
      sortBy: "name",
      keys: ["Война", "Политика", "Общественность"],
      items: [],
      // Настройка сбора данных
      photo: "",
      // загрузка
      load: false,
    };
  },
  computed: {
    numberOfPages() {
      return Math.ceil(this.items.length / this.itemsPerPage);
    },
    filteredKeys() {
      return this.keys.filter((key) => key !== "Name");
    },
    url() {
      if (!this.photo) return;
      return URL.createObjectURL(this.photo);
    },
  },
  methods: {
    nextPage() {
      if (this.page + 1 <= this.numberOfPages) this.page += 1;
    },
    formerPage() {
      if (this.page - 1 >= 1) this.page -= 1;
    },
    updateItemsPerPage(number) {
      this.itemsPerPage = number;
    },
    find_user() {
      this.load = true;
      let formData = new FormData();
      formData.append("image", this.photo);
      this.$http.post("social_users/find/", formData).then((response) => {
        this.items = response.data;
        this.load = false;
      });
    },
  },
};
</script>


<style lang="scss">
</style>