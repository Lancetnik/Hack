<template>
<v-card flat style="background: transparent">
    <v-row style="z-index: 20">
      <v-col md="3">
        <v-card class="ma-4">
          <v-card-title>
            Настройки поиска
          </v-card-title>
          <v-progress-linear
            v-if="this.load==true"
            indeterminate
            color="success"
          ></v-progress-linear>
          <v-card-text>
            <v-text-field
            label = 'Номер телефона'
             v-model='phone'>
            </v-text-field>
            <v-btn
              :color="$route.meta.theme"
              class=" white--text"
              @click="submitNumber"
            >
              Запустить
            <v-icon right>
              mdi-cloud-upload
            </v-icon>
            </v-btn>
          </v-card-text>
        </v-card>
        <v-card class="ma-4">
              <v-card-title>
                Данные смартфона:
              </v-card-title>
              <v-card-text>
                Оператор: {{ this.operator }}
                <v-progress-circular
                  v-if="this.load==true"
                  indeterminate
                  color="green"
                ></v-progress-circular>
              </v-card-text>
              <v-card-text>
                Страна: {{ this.country }}
                <v-progress-circular
                  v-if="this.load==true"
                  indeterminate
                  color="green"
                ></v-progress-circular>
              </v-card-text>
              <v-card-text>
                Регион: {{ this.region }}
                <v-progress-circular
                  v-if="this.load==true"
                  indeterminate
                  color="green"
                ></v-progress-circular>
              </v-card-text>
              <v-card-text>
                Город: {{ this.city }}
                <v-progress-circular
                  v-if="this.load==true"
                  indeterminate
                  color="green"
                ></v-progress-circular>
              </v-card-text>
              <v-card-text>
                Долгота: {{ this.longitude }}
                <v-progress-circular
                  v-if="this.load==true"
                  indeterminate
                  color="green"
                ></v-progress-circular>
              </v-card-text>
                <v-card-text>
                Широта: {{ this.latitude }}
                <v-progress-circular
                  v-if="this.load==true"
                  indeterminate
                  color="green"
                ></v-progress-circular>
                    <v-btn 
                        v-if="city != ''"
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
        <v-card class="ma-4">
          <Map :points='points' :center='center' :zoom='zoom' style='height: 650px; width: 100%'/>
        </v-card>
      </v-col>
    </v-row>
    </v-card>
</template>


<script>
import Map from "@/components/map/MapPhone.vue";
import { saveExcel } from '@progress/kendo-vue-excel-export';

export default {
  name: "First",

  components: {
    Map
  },

  methods: {
    submitNumber() {
      this.load = true
      this.$http.post("social_users/find/phone/", {'phone':this.phone})
      .then((response) => {
        this.operator = response.data.location.operator,
        this.country = response.data.location.country,
        this.region = response.data.location.region,
        this.city = response.data.location.city,
        this.latitude = response.data.location.geo_city.latitude,
        this.longitude = response.data.location.geo_city.longitude,
        this.center = [response.data.location.geo_city.latitude, response.data.location.geo_city.longitude]
        this.points = [response.data.point]
        this.zoom = 20
        this.dataexcel=[{
                        'Телефон': this.phone, 
                        'Оператор':this.operator, 
                        'Город':this.city, 
                        'Широта':this.latitude,
                        'Долгота':this.longitude
                        }]
      })
      .finally(()=>{
        this.load = false
      })
      
    },
    exportExcel () {
      console.log(this.dataexcel);
            saveExcel({
                data: this.dataexcel,
                fileName: "Phonelocation.xlsx",
                columns: [
                  { field: 'Телефон'},
                  { field: 'Оператор'},
                  { field: 'Город'},
                  { field: 'Широта'},
                  { field: 'Долгота'},
              ]
            });
        },
    
  },

  data: () => ({
    phone: null,
    operator: "",
    country: "",
    region: "",
    city: "",
    location: '',
    load: false,
    center: [59.937, 30.3089],
    zoom: 10,
    dataexcel: []


  })
};
</script>


<style lang="scss">
</style>