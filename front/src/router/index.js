import Vue from 'vue'
import VueRouter from 'vue-router'


Vue.use(VueRouter)

const routes = [{
    path: '/',
    component: () =>
        import ('../pages/Main.vue'),
    redirect: { name: 'phonesearch' },
    name: 'main',
    children: [{
            path: '/phonesearch',
            component: () =>
                import ('../pages/Main/PhoneSearch.vue'),
            name: 'phonesearch',
            meta: { theme: '#55884F' },
            props: true
        },
        {
            path: '/strava',
            component: () =>
                import ('../pages/Main/Strava.vue'),
            name: 'strava',
            meta: { theme: '#1976D2' },
            props: true
        },
        {
            path: '/scraper',
            component: () =>
                import ('../pages/Main/Scraper.vue'),
            name: 'scraper',
            meta: { theme: '#544F88' },
            props: true
        },
        {
            path: '/findclone',
            component: () =>
                import ('../pages/Main/FindClone.vue'),
            name: 'findclone',
            meta: { theme: '#37889A' },
            props: true
        },
        {
            path: '/photo-seacrh',
            component: () =>
                import ('../pages/Main/PhotoSearch.vue'),
            name: 'photo',
            meta: { theme: '#374D9A' },
            props: true
        },
        {
            path: '/data_agregation',
            component: () =>
                import ('../pages/Main/DataAgregation.vue'),
            name: 'dataAgregation',
            meta: { theme: '#8E24AA'}
        }
    ]
}, ]

const router = new VueRouter({
    routes
})

export default router