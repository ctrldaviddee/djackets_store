<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
  <section class="bg-white dark:bg-gray-900">
    <div class="py-8 px-4 mx-auto max-w-screen-xl lg:py-16 lg:px-6">
      <div class="mx-auto max-w-screen-sm text-center">
        <h1
          class="mb-4 text-7xl tracking-tight font-extrabold lg:text-9xl text-gray-500 dark:text-gray-500"
        >
          404
        </h1>
        <p class="mb-4 text-3xl tracking-tight font-bold text-gray-900 md:text-4xl dark:text-white">
          Something's missing.
        </p>
        <p class="mb-4 text-lg font-light text-gray-500 dark:text-gray-400">
          Sorry, we can't find that page. You'll find lots to explore on the home page.
        </p>
        <RouterLink
          to="/"
          class="inline-flex text-white bg-gray-600 hover:bg-gray-800 focus:ring-4 focus:outline-none focus:ring-gray-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:focus:ring-gray-900 my-4"
          >Retourner à la page d'accueuil</RouterLink
        >
      </div>
    </div>
  </section>
</template>
