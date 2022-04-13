<template>
<v-card flat style="background: transparent"> 
    <v-row>
        <v-col>
            <v-card class="ma-3">
                <v-card-title>
                    Настройка:
                </v-card-title>
                <v-card-text>
                  <v-text-field
                      label="Левая широта"
                      hide-details="auto"
                      class="ma-2"
                      :value="latitude_1"
                      >
                      </v-text-field>
                  <v-text-field
                      label="Левая долгота"
                      hide-details="auto"
                      class="ma-2"
                      :value="longitude_1"
                      ></v-text-field>
                  <v-text-field
                      label="Правая широта"
                      hide-details="auto"
                      class="ma-2"
                      :value="latitude_2"
                      ></v-text-field>
                  <v-text-field
                      label="Правая долгота"
                      hide-details="auto"
                      class="ma-2"
                      :value="longitude_2"
                      ></v-text-field>
                </v-card-text>
                <v-card-actions>
                    <v-btn
                    :color="$route.meta.theme"
                    class="ma-2 white--text"
                    @click="get_coordinates"
                    >
                    Загрузить
                    <v-icon right>
                    mdi-animation-outline
                    </v-icon>
                    </v-btn>
                </v-card-actions>
              <v-data-table
                :headers="headers"
                :items="users_info"
                item-key="name"
                class="elevation-1"
                :search="search"
                v-if="users_info.length>0"
              >
                <template v-slot:top>
                  <v-text-field
                    v-model="search"
                    label="Поиск (ЗАГЛАВНЫМИ БУКВАМИ)"
                    class="mx-4"
                  ></v-text-field>
                </template>
                <template v-slot:[`item.actions`]="{ item }">
                  <v-icon
                    small
                    class="mr-2"
                    @click="getroute(item)"
                  >
                    mdi-pencil
                  </v-icon>
                </template>
              </v-data-table>
            </v-card>
        </v-col>
      <v-col md="9">
        <v-card flat style="background: transparent">
          <Map :coords="coords" :first_coord="first_coord"
           :user="user" :center="center" :zoom="zoom" style='height: 650px; width: 100%'/>
        </v-card>
      </v-col>
    </v-row>
</v-card>
</template>


<script>
import Map from "@/components/map/MapStrava.vue";

export default {
    props: {
      latitude_1: {
      default: () => { return 59.937 }
    },
      longitude_1:  {
      default: () => { return 30.3089 }
      },
      latitude_2: {
      default: () => { return '' }
    },
      longitude_2:  {
      default: () => { return '' }
      },
    },
    components: {
    Map,
  },

  data: () => ({
    coords: [],
    user:'',
    users_info: [],
    center: [59.937, 30.3089],
    first_coord: [],
    zoom: 10,
    // Таблица
    search: '',
    headers: [
          {
            text: 'Ф.И.О.',
            align: 'start',
            sortable: false,
            value: 'name',
          },
          { text: 'Маршрут', value: 'actions', sortable: false },
        ],
  }),

  watch: {
    title(val) {
      this.lot = val;
    },
  },
methods: {
    get_coordinates() {
    this.$http.get('strava/polyline/').then((response) => {
        this.users_info = response.data
    })
  },
    getroute(route){
      this.coords = route.coordinates
      this.user = route.name
      console.log(this.coords)
      this.center = this.coords[0]
      this.zoom = 16
  },
  },
created() {
  this.center = [this.latitude_1, this.longitude_1]
  this.first_coord = [this.latitude_1+0.005, this.longitude_1+0.005]
},
  computed: {
    url() {
      if (!this.points[0]['2']['codingline']) return;
      return URL.createObjectURL(this.points[0]['2']['codingline']);
    }
  },
};
</script>