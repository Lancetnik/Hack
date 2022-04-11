<template>
  <v-card color="gren">
  <v-row style="z-index: 20;">
    <v-col fluid>
      <v-card md="12">
        <v-card-title>
          Введите номер телефона, чье местоположение устройства необходимо отследить:
        </v-card-title>
        <v-card-text>
          <v-row>
            <v-col>
            <phoneInput v-model='phone'/>
            </v-col>
            <v-col>
            <v-btn
              :color="$route.meta.theme"
              class="ma-2 white--text"
              @click="submitNumber"
            >
              Запустить
            <v-icon right>
              mdi-cloud-upload
            </v-icon>
            </v-btn>
            </v-col>
            <v-progress-linear
              v-if="this.load==true"
              indeterminate
              color="success"
            ></v-progress-linear>
          </v-row>
        </v-card-text>
        <br>
        <v-row>
          <v-col md="4">
            <v-card>
              <v-card-title>
                Данные смартфона
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
                Местоположение: {{ this.location }}
                <v-progress-circular
                  v-if="this.load==true"
                  indeterminate
                  color="green"
                ></v-progress-circular>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col>
            <v-card>
            <Map :points='points' style='height: 600px; width: 100%'/>
            </v-card>
          </v-col>
        </v-row>
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
      this.$http.post("geo/phone/", this.post).then((response) => {
        this.operator = response.data.operator,
        this.country = response.data.country,
        this.region = response.data.region,
        this.city = response.data.city,
        this.location = `${response.data.location[0]}-${response.data.location[1]}`
      })
      .finally(()=>{
        this.load = false
      }
      )
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