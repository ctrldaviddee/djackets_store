<script setup>
import NavBar from './components/NavBar.vue'
import Footer from './components/Footer.vue'
import { RouterView } from 'vue-router'
</script>

<template>
  <NavBar />

  <!-- Page Container -->
  <div
    id="page-container"
    class="mx-auto flex min-h-dvh w-full min-w-80 flex-col bg-gray-100 dark:bg-gray-900 dark:text-gray-100"
  >
    <!-- Page Content -->
    <main id="page-content" class="flex max-w-full flex-auto flex-col">
      <div class="container mx-auto p-4 lg:p-8 xl:max-w-7xl">
        <!--

        ADD YOUR MAIN CONTENT BELOW

        -->

        <RouterView />

        <!--

        ADD YOUR MAIN CONTENT ABOVE

        -->
      </div>
    </main>
    <!-- END Page Content -->

    <Footer />
    <!-- END Page Footer -->
  </div>
  <!-- END Page Container -->
</template>
