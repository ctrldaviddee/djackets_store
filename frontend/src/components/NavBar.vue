<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'

const mobileNavOpen = ref(false)
</script>

<template>
  <!-- Page Header -->
  <header
    id="page-header"
    class="z-1 flex flex-none items-center bg-white shadow-xs dark:bg-gray-800"
  >
    <div class="container mx-auto px-4 lg:px-8 xl:max-w-7xl">
      <div class="flex justify-between py-4">
        <!-- Left Section -->
        <div class="flex items-center gap-2 lg:gap-6">
          <!-- Logo -->
          <RouterLink
            to="/"
            class="group inline-flex items-center gap-2 text-lg font-bold tracking-wide text-gray-900 hover:text-gray-600 dark:text-gray-100 dark:hover:text-gray-300"
          >
            <svg
              class="hi-mini hi-cube-transparent inline-block size-5 text-blue-600 transition group-hover:scale-110 dark:text-blue-400"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 20 20"
              fill="currentColor"
              aria-hidden="true"
            >
              <path
                fill-rule="evenodd"
                d="M9.638 1.093a.75.75 0 01.724 0l2 1.104a.75.75 0 11-.724 1.313L10 2.607l-1.638.903a.75.75 0 11-.724-1.313l2-1.104zM5.403 4.287a.75.75 0 01-.295 1.019l-.805.444.805.444a.75.75 0 01-.724 1.314L3.5 7.02v.73a.75.75 0 01-1.5 0v-2a.75.75 0 01.388-.657l1.996-1.1a.75.75 0 011.019.294zm9.194 0a.75.75 0 011.02-.295l1.995 1.101A.75.75 0 0118 5.75v2a.75.75 0 01-1.5 0v-.73l-.884.488a.75.75 0 11-.724-1.314l.806-.444-.806-.444a.75.75 0 01-.295-1.02zM7.343 8.284a.75.75 0 011.02-.294L10 8.893l1.638-.903a.75.75 0 11.724 1.313l-1.612.89v1.557a.75.75 0 01-1.5 0v-1.557l-1.612-.89a.75.75 0 01-.295-1.019zM2.75 11.5a.75.75 0 01.75.75v1.557l1.608.887a.75.75 0 01-.724 1.314l-1.996-1.101A.75.75 0 012 14.25v-2a.75.75 0 01.75-.75zm14.5 0a.75.75 0 01.75.75v2a.75.75 0 01-.388.657l-1.996 1.1a.75.75 0 11-.724-1.313l1.608-.887V12.25a.75.75 0 01.75-.75zm-7.25 4a.75.75 0 01.75.75v.73l.888-.49a.75.75 0 01.724 1.313l-2 1.104a.75.75 0 01-.724 0l-2-1.104a.75.75 0 11.724-1.313l.888.49v-.73a.75.75 0 01.75-.75z"
                clip-rule="evenodd"
              />
            </svg>
            <span class="text-2xl">Djackets</span>
          </RouterLink>
          <!-- END Logo -->

          <!-- Desktop Navigation -->
          <nav class="hidden items-center gap-2 lg:flex">
            <RouterLink
              to="/summer"
              class="group flex items-center gap-2 rounded-lg border border-transparent px-3 py-2 text-lg font-bold text-gray-800 hover:bg-blue-50 hover:text-blue-600 active:border-blue-100 dark:text-gray-200 dark:hover:bg-gray-700 dark:hover:text-white dark:active:border-gray-600"
            >
              <span>Summer</span>
            </RouterLink>
            <RouterLink
              to="/winter"
              class="group flex items-center gap-2 rounded-lg border border-transparent px-3 py-2 text-lg font-bold text-gray-800 hover:bg-blue-50 hover:text-blue-600 active:border-blue-100 dark:text-gray-200 dark:hover:bg-gray-700 dark:hover:text-white dark:active:border-gray-600"
            >
              <span>Winter</span>
            </RouterLink>
          </nav>
          <!-- END Desktop Navigation -->
        </div>
        <!-- END Left Section -->

        <!-- Right Section -->
        <div class="flex items-center gap-2">
          <!-- Login -->

          <RouterLink
            to="/log-in"
            class="hidden lg:inline-flex items-center justify-center gap-1 rounded-lg border border-blue-700 bg-blue-700 px-3 py-2 text-base font-semibold text-white hover:border-blue-600 hover:bg-blue-600 hover:text-white focus:ring-3 focus:ring-blue-400/50 active:border-blue-700 active:bg-blue-700 dark:focus:ring-blue-400/90"
          >
            <span>Login</span>
            <svg
              class="w-3.5 h-3.5 ms-2 rtl:rotate-180"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 14 10"
            >
              <path
                stroke="currentColor"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M1 5h12m0 0L9 1m4 4L9 9"
              />
            </svg>
          </RouterLink>
          <!-- END Login -->

          <!-- Cart -->
          <RouterLink
            to="/cart"
            class="hidden lg:inline-flex gap-1 justify-center hover:text-gray-900 items-center py-2 px-5 text-base font-medium text-center text-white rounded-lg border border-white hover:bg-gray-100 focus:ring-4 focus:ring-gray-400"
          >
            <span>Cart</span>
            <i class="pi pi-shopping-cart"></i>
          </RouterLink>
          <!-- End cart -->

          <!-- Toggle Mobile Navigation -->
          <div class="lg:hidden">
            <button
              @click="mobileNavOpen = !mobileNavOpen"
              type="button"
              class="inline-flex items-center justify-center gap-2 rounded-lg border border-gray-200 bg-white px-3 py-2 text-sm leading-5 font-semibold text-gray-800 hover:border-gray-300 hover:text-gray-900 hover:shadow-xs focus:ring-3 focus:ring-gray-300/25 active:border-gray-200 active:shadow-none dark:border-gray-700 dark:bg-gray-800 dark:text-gray-300 dark:hover:border-gray-600 dark:hover:text-gray-200 dark:focus:ring-gray-600/40 dark:active:border-gray-700"
            >
              <svg
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
                class="hi-solid hi-menu inline-block size-5"
              >
                <path
                  fill-rule="evenodd"
                  d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
                  clip-rule="evenodd"
                ></path>
              </svg>
            </button>
          </div>
          <!-- END Toggle Mobile Navigation -->
        </div>
        <!-- END Right Section -->
      </div>

      <!-- Mobile Navigation -->
      <div
        class="lg:hidden"
        :class="{
          hidden: !mobileNavOpen,
        }"
      >
        <nav class="flex flex-col gap-2 border-t border-gray-200 py-4 dark:border-gray-700">
          <RouterLink
            to="/summer"
            class="group text-lg font-bold flex items-center gap-2 rounded-lg border border-transparent px-3 py-2 text-gray-800 hover:bg-blue-50 hover:text-blue-600 active:border-blue-100 dark:text-gray-200 dark:hover:bg-gray-700 dark:hover:text-white dark:active:border-gray-600"
          >
            <span>Summer</span>
          </RouterLink>

          <RouterLink
            to="/winter"
            class="group text-lg font-bold flex items-center gap-2 rounded-lg border border-transparent px-3 py-2 text-gray-800 hover:bg-blue-50 hover:text-blue-600 active:border-blue-100 dark:text-gray-200 dark:hover:bg-gray-700 dark:hover:text-white dark:active:border-gray-600"
          >
            <span>Winter</span>
          </RouterLink>

          <RouterLink
            to="/log-in"
            class="inline-flex items-center justify-center gap-2 rounded-lg border border-blue-700 bg-blue-700 px-3 py-2 text-lg leading-5 font-semibold text-white hover:border-blue-600 hover:bg-blue-600 hover:text-white focus:ring-3 focus:ring-blue-400/50 active:border-blue-700 active:bg-blue-700 dark:focus:ring-blue-400/90"
          >
            <span>Login</span>
          </RouterLink>

          <RouterLink
            to="/cart"
            class="inline-flex justify-center hover:text-gray-900 items-center py-2 px-5 text-base font-medium text-center text-white rounded-lg border border-white hover:bg-gray-100 focus:ring-4 focus:ring-gray-400"
          >
            <i class="pi pi-shopping-cart"></i>&nbsp; Cart
          </RouterLink>
        </nav>
      </div>
      <!-- END Mobile Navigation -->
    </div>
  </header>
  <!-- END Page Header -->
</template>
