import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'

import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'
import vueDevTools from 'vite-plugin-vue-devtools'


// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueJsx(),
    vueDevTools(),
    tailwindcss(),
  ],
  server: {
    port: 3000,
    proxy:{
      '/api':{ // Intercepts any request that starts with "/api"
        target: 'http://127.0.0.1:8000/', // Backend server to forward requests to
        changeOrigin: true, // Changes the origin of the request to match the target
        // rewrite: (path) => path.replace(/^\/api/, '') // Removes "/api" from the request pat
      }

        // target: 'http://127.0.0.1:8000/', // Backend server to forward requests to
        // changeOrigin: true, // Changes the origin of the request to match the target
        // // rewrite: (path) => path.replace(/^\/api/, '') // Removes "/api" from the request pat

    }
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
})
