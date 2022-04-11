import Vue from 'vue'
import VueRouter from 'vue-router'


Vue.use(VueRouter)

const routes = [{
    path: '/',
    component: () =>
        import ('../pages/Main.vue'),
    redirect: { name: 'map' },
    name: 'main',
    children: [{
            path: '/first',
            component: () =>
                import ('../pages/Main/First.vue'),
            name: 'first',
            meta: { theme: '#55884F' }
        },
        {
            path: '/map',
            component: () =>
                import ('../pages/Main/Map.vue'),
            name: 'map',
            meta: { theme: '#55884F' }
        },
        {
            path: '/scraper',
            component: () =>
                import ('../pages/Main/Scraper.vue'),
            name: 'scraper',
            meta: { theme: '#544F88' }
        },
        {
            path: '/findclone',
            component: () =>
                import ('../pages/Main/FindClone.vue'),
            name: 'findclone',
            meta: { theme: '#37889A' }
        },
        {
            path: '/photo-seacrh',
            component: () =>
                import ('../pages/Main/PhotoSearch.vue'),
            name: 'photo',
            meta: { theme: '#374D9A' }
        }
    ]
}, ]

const router = new VueRouter({
    routes
})

export default router