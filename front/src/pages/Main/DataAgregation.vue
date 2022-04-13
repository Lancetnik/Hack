<template>
  <v-stepper class="step" v-model="e1">
    <v-stepper-header>
      <v-stepper-step
        :complete="e1 > 1"
        step="1"
      >
        Поиск места по фото
      </v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step
        :complete="e1 > 2"
        step="2"
      >
        Поиск страницы по фото
      </v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step
      :complete="e1 > 3"
       step="3">
        Отслеживание номера телефона
      </v-stepper-step>

      <v-divider></v-divider>

      <v-stepper-step
      :complete="e1 > 4"
      step="4">
        Досье
      </v-stepper-step>

    </v-stepper-header>

    <v-stepper-items>
      <v-stepper-content step="1">
        <v-card
          class="mb-12"
          height="700px"
        >
        <photosearch/>
        </v-card>

        <v-btn
          color="primary"
          @click="e1 = 2"
        >
          Следующий шаг
        </v-btn>
      </v-stepper-content>

      <v-stepper-content step="2">
        <v-card
          class="mb-12"
          height="700px"
        >
        <findclone/>
        </v-card>

        <v-btn
          color="primary"
          @click="e1 = 3"
        >
          Следующий шаг
        </v-btn>

      </v-stepper-content>

      <v-stepper-content step="3">
        <v-card
          class="mb-12"
          height="700px"
        >
        <phonesearch/>
        </v-card>

        <v-btn
          color="primary"
          @click="e1 = 4; get_cache();"
        >
          Следующий шаг
        </v-btn>
      </v-stepper-content>

      <v-stepper-content step="4">
        <v-card
          class="mb-12"
          height="700px"
        >
            <v-row>
                <v-col md="4">
                    <v-card>
                    <v-card-title>
                        Поиск места по фото
                    </v-card-title>
                    <v-card-text>
                        Координаты: {{ photo_coordinate}}
                    </v-card-text>
                    </v-card>
                </v-col>
                <v-col md="4">
                <v-card>
                    <v-card-title>
                        Поиск страницы по фото
                    </v-card-title>
                    <v-card-text>
                        URL: {{ url }}
                        <br>
                        Схожесть: {{ score }}
                        <br>
                        Имя: {{ name }}
                        <br>
                        Найденная фотография
                        <v-img :src="image_src">
                        </v-img>
                    </v-card-text>
                </v-card>
                </v-col>
                <v-col md="4">
                    <v-card>
                    <v-card-title>
                        Отслеживание номера телефона
                    </v-card-title>
                    <v-card-text>
                        Координаты: {{ phone_coordinate }}
                    </v-card-text>
                    </v-card>
                </v-col>
            </v-row>
        </v-card>

        <v-btn
          color="primary"
          @click="e1 = 1; clean_cache()"
        >
          Закончить
        </v-btn>
        
        <v-btn     
          color="primary"
          class="mx-4 white--text color"
          @click="exportExcel"
                  >
            Экспортировать
          <v-icon right>
            mdi-apple-keyboard-caps
          </v-icon>
        </v-btn>
        
        
      </v-stepper-content>
        
    </v-stepper-items>
  </v-stepper>
</template>



<script>
import photosearch from "./PhotoSearch.vue"
import findclone from "./FindClone.vue"
import phonesearch from "./PhoneSearch.vue"
import { saveExcel } from '@progress/kendo-vue-excel-export';

export default {
    components: {
    photosearch,
    findclone,
    phonesearch,
  },
  data: () => ({
       user_data: [],
       e1: 1,
       photo_coordinate: 'Отсутствует',
       phone_coordinate: 'Отсутствует',
       url: 'Отсутствует',
       score: 'Отсутствует',
       name: 'Имя',
       image_src: 'https://img.freepik.com/free-vector/photo-frame-icon-empty-photo-blank-vector-on-isolated-transparent-background-eps-10_399089-1290.jpg?w=740'
  }),

  methods: {
      get_cache() {
          this.$http
          .get('/social_users/get_cache/')
          .then(response => {
              if (response.data.photo_coordinates.length > 0) {
              this.photo_coordinate = response.data.photo_coordinates
              }
              else {
                this.photo_coordinate = 'Отсутсвует'
              }
              if (response.data.phone_coordinates.length > 0) {
              this.phone_coordinate = response.data.phone_coordinates
              }
              else {
                 this.phone_coordinate = 'Отсутсвует' 
              }
              if (response.data.social_vk.length > 0){
              this.url = response.data.social_vk.url
              this.score = response.data.social_vk.score
              this.name = response.data.social_vk.name
              this.image_src = response.data.social_vk.photo
              }
              else {
                this.url = 'Отсутсвует'
                this.score = 'Отсутсвует'
                this.name = 'Отсутсвует'
                this.image_src = 'Отсутсвует'
              } 
              this.user_data=[{
                'Имя':this.name,
                'Совпадение':this.score,
                'Ссылка':this.url,
                'Координаты фото': String(this.photo_coordinate),
                'Координаты телефон': String(this.phone_coordinate)
              }]
              
          })

      },
      clean_cache() {
          this.$http
          .get('/social_users/clean_cache/')
      },
          exportExcel () {
            console.log(this.name)
            saveExcel({
                data: this.user_data,
                fileName: "User_data.xlsx",
                columns: [
                  { field: 'Имя'},
                  { field: 'Совпадение'},
                  { field: 'Ссылка'},
                  { field: 'Координаты фото'},
                  { field: 'Координаты телефон'},
              ]
            });
        },
  },

  created() {
  },
};
</script>


<style lang="scss">
</style>