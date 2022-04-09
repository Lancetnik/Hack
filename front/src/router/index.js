import Vue from 'vue'
import VueRouter from 'vue-router'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: () => import('../pages/Main.vue'),
    redirect: {name: 'map'},
    name: 'main',
    children: [
      {
        path: '/map',
        component: () => import('../pages/Main/Map.vue'),
        name: 'map',
        meta: { theme: '#55884F' }
      },
      {
        path: '/scraper',
        component: () => import('../pages/Main/Scraper.vue'),
        name: 'scraper',
        meta: { theme: '#544F88' }
      },  
      {
        path: '/page3',
        component: () => import('../pages/Main/Page3.vue'),
        name: 'page3',
        meta: { theme: '#37889A' }
      },  
      {
        path: '/page4',
        component: () => import('../pages/Main/Page4.vue'),
        name: 'page4',
        meta: { theme: '#374D9A' }
      }  
    ]
  },
]

const router = new VueRouter({
  routes
})

export default router
