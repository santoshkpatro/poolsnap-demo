import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
    },
    {
        path: '/about',
        name: 'About',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
            import(/* webpackChunkName: "about" */ '../views/About.vue'),
    },
    {
        path: '/items/:item_id',
        name: 'Items',
        props: true,
        component: () => import('../views/Items.vue'),
    },
    {
        path: '/auth/login',
        name: 'Login',
        component: () => import('../views/auth/Login.vue'),
    },
    {
        path: '/auth/register',
        name: 'Register',
        component: () => import('../views/auth/Register.vue'),
    },
    {
        path: '/upload',
        name: 'Upload',
        meta: { requiresAuth: true },
        component: () => import('../views/Upload.vue'),
    },
    {
        path: '/license/:license_id',
        name: 'License',
        meta: { requiresAuth: true },
        props: true,
        component: () => import('../views/License.vue'),
    },
    {
        path: '/orders/:item_id/:type',
        name: 'Orders',
        meta: { requiresAuth: true },
        props: true,
        component: () => import('../views/orders/Orders.vue'),
    },
    {
        path: '/orders/payment/success',
        name: 'Success',
        meta: { requiresAuth: true },
        props: true,
        component: () => import('../views/orders/Success.vue'),
    },
    {
        path: '/orders/payment/:order_id',
        name: 'Payment',
        meta: { requiresAuth: true },
        props: true,
        component: () => import('../views/orders/Payment.vue'),
    },
    {
        path: '/inventory',
        name: 'Inventory',
        meta: { requiresAuth: true },
        component: () => import('../views/Inventory.vue'),
        children: [
            {
                path: 'uploads/',
                name: 'Uploads',
                meta: { requiresAuth: true },
                component: () => import('../views/inventory/Uploads.vue'),
            },
            {
                path: 'licenses/',
                name: 'Licenses',
                meta: { requiresAuth: true },
                component: () => import('../views/inventory/Licenses.vue'),
            },
            {
                path: 'orders/',
                name: 'PreviousOrders',
                meta: { requiresAuth: true },
                component: () =>
                    import('../views/inventory/PreviousOrders.vue'),
            },
        ],
    },
    {
        path: '/:username',
        name: 'Profile',
        props: true,
        component: () => import('../views/Profile.vue'),
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
})

router.beforeEach((to, from, next) => {
    const loggedIn = localStorage.getItem('user')

    if (to.matched.some(record => record.meta.requiresAuth)) {
        // this route requires auth, check if logged in
        // if not, redirect to login page.
        if (!loggedIn) {
            next({
                path: '/auth/login',
                query: { redirect: to.fullPath },
            })
        } else {
            next()
        }
    } else {
        next() // make sure to always call next()!
    }
})

export default router
