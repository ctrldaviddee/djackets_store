// import HomeView from '@/views/HomeView.vue'
// import NotFound from '@/views/NotFound.vue'

// import { createRouter, createWebHistory } from 'vue-router'

// const router = createRouter({
//   history: createWebHistory(import.meta.env.BASE_URL),
//   routes: [
//     {
//       path: '/',
//       name: 'home',
//       component: HomeView,
//     },
//     {
//       path: '/add-recipe',
//       name: 'add_recipe',
//       component: () => import('@/views/RecipeForm.vue'),
//     },
//     {
//       path: '/:catchAll(.*)',
//       name: 'not-found',
//       component: NotFound,
//     },

//     // {
//     //   path: '/about',
//     //   name: 'about',
//     //   // route level code-splitting
//     //   // this generates a separate chunk (About.[hash].js) for this route
//     //   // which is lazy-loaded when the route is visited.
//     //   component: () => import('../views/AboutView.vue'),
//     // },
//   ],
// })

// export default router

import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ProductView from '@/views/ProductView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/:category_slug/:product_slug',
      name:'product',
      component: ProductView,
    }
  ],
})

export default router
