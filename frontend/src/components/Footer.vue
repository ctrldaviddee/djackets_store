<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
  <!-- Page Footer -->
  <footer id="page-footer" class="flex flex-none items-center bg-white dark:bg-gray-800">
    <div
      class="container mx-auto flex flex-col px-4 text-center text-sm md:flex-row md:justify-between md:text-left lg:px-8 xl:max-w-7xl"
    >
      <div class="pt-4 pb-1 md:pb-4">
        <a
          href="https://tailkit.com"
          class="font-medium text-blue-600 hover:text-blue-400 dark:text-blue-400 dark:hover:text-blue-300"
          target="_blank"
          >Copyight</a
        >
        © 2025
      </div>
      <div class="inline-flex items-center justify-center pt-1 pb-4 md:pt-4">
        <span>Crafted with</span>
        <!-- <svg fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"
            class="hi-solid hi-heart mx-1 inline-block size-4 text-red-600">
            <path fill-rule="evenodd"
              d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z"
              clip-rule="evenodd"></path>
          </svg> -->
        &nbsp;<span class="text-teal-500 font-extrabold">vue &nbsp;</span> and &nbsp;<span
          class="text-teal-500 font-extrabold"
          >dj</span
        >&nbsp;
        <span>
          by
          <a
            href="https://pixelcave.com"
            class="font-medium text-blue-600 hover:text-blue-400 dark:text-blue-400 dark:hover:text-blue-300"
            target="_blank"
            >Dave</a
          ></span
        >
      </div>
    </div>
  </footer>
  <!-- END Page Footer -->
</template>
