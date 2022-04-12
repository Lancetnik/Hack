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
            <phoneInput v-model='phone'/>
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
              </v-card-text>
            </v-card>
      </v-col>
      <v-col md="9">
        <v-card class="ma-4">
          <Map :points='points' style='height: 650px; width: 100%'/>
        </v-card>
      </v-col>
    </v-row>
    </v-card>
</template>


<script>
import Map from "@/components/map/Map.vue";
import phoneInput from "@/components/phoneField.vue"

export default {
  name: "First",

  components: {
    Map,
    phoneInput
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
        this.points = [response.data.point]
      })
      .finally(()=>{
        this.load = false
      })
    }
  },

  data: () => ({
    phone: null,
    operator: "",
    country: "",
    region: "",
    city: "",
    location: '',
    load: false


  })
};
</script>


<style lang="scss">
</style>