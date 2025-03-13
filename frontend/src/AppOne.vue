<script setup>
import { ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import { TransitionRoot } from '@headlessui/vue'

const show_mob_btn = ref(false)

function get_img_url(name, ext) {
  try {
    return new URL(`/src/assets/img/${name}.${ext}`, import.meta.url).href
  } catch (error) {
    return ''
  }
}
</script>

<template>
  <header>
    <div class="wrapper">
      <nav class="border-gray-200 bg-gray-50 dark:bg-gray-800 dark:border-gray-700">
        <div
          class="flex flex-wrap items-center justify-between mx-auto p-4"
          :class="{ is_active: show_mob_btn }"
        >
          <RouterLink to="/" class="flex items-center space-x-3 rtl:space-x-reverse">
            <img :src="get_img_url('logo', 'png')" class="h-12 w-auto sm:h-16" alt="logo" />
            <span
              class="self-center text-2xl sm:text-4xl font-semibold whitespace-nowrap dark:text-white hidden sm:block"
              >Djackets</span
            >
          </RouterLink>
          <button
            @click="show_mob_btn = !show_mob_btn"
            data-collapse-toggle="navbar-solid-bg"
            type="button"
            class="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
            aria-controls="navbar-solid-bg"
            :aria-expanded="show_mob_btn"
          >
            <span class="sr-only">Open main menu</span>
            <svg
              class="w-5 h-5"
              aria-hidden="true"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 17 14"
            >
              <path
                stroke="currentColor"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M1 1h15M1 7h15M1 13h15"
              />
            </svg>
          </button>
          <!-- Mobile Menu with Transition -->
          <TransitionRoot
            :show="show_mob_btn"
            appear
            as="div"
            class="w-full md:hidden"
            enter="transition duration-200 ease-out"
            enterFrom="transform scale-95 opacity-0"
            enterTo="transform scale-100 opacity-100"
            leave="transition duration-150 ease-in"
            leaveFrom="transform scale-100 opacity-100"
            leaveTo="transform scale-95 opacity-0"
          >
            <div id="navbar-solid-bg">
              <ul
                class="flex flex-col font-medium mt-4 rounded-lg bg-gray-50 rtl:space-x-reverse md:mt-0 md:border-0 md:bg-transparent dark:bg-gray-800 md:dark:bg-transparent dark:border-gray-700"
              >
                <li>
                  <RouterLink
                    to="/summer"
                    class="mt-2 block text-xl font-semibold py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white"
                  >
                    Summer</RouterLink
                  >
                </li>
                <li>
                  <RouterLink
                    to="/winter"
                    class="mt-2 block text-xl font-semibold py-2 px-3 text-gray-900 rounded-sm hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700 dark:hover:text-white"
                  >
                    Winter</RouterLink
                  >
                </li>
                <li>
                  <div class="flex flex-col space-y-4">
                    <RouterLink
                      to="/log-in"
                      class="inline-flex justify-center items-center py-3 px-5 text-base font-medium text-center text-white rounded-lg bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 dark:focus:ring-blue-900"
                    >
                      Log in
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
                    <RouterLink
                      to="/cart"
                      class="inline-flex justify-center hover:text-gray-900 items-center py-3 px-5 text-base font-medium text-center text-white rounded-lg border border-white hover:bg-gray-100 focus:ring-4 focus:ring-gray-400"
                    >
                      <i class="pi pi-shopping-cart"></i> &nbsp; Cart
                    </RouterLink>
                  </div>
                </li>
              </ul>
            </div>
          </TransitionRoot>

          <!-- Desktop Menu -->
          <div class="hidden md:block md:w-auto" id="navbar-solid-bg-desktop">
            <ul class="flex items-center space-x-8 rtl:space-x-reverse">
              <li>
                <RouterLink
                  to="/summer"
                  class="text-xl font-semibold text-gray-900 hover:text-blue-700 dark:text-white dark:hover:text-blue-500"
                >
                  Summer</RouterLink
                >
              </li>
              <li>
                <RouterLink
                  to="/winter"
                  class="text-xl font-semibold text-gray-900 hover:text-blue-700 dark:text-white dark:hover:text-blue-500"
                >
                  Winter</RouterLink
                >
              </li>
              <li>
                <div class="flex items-center space-x-4">
                  <RouterLink
                    to="/log-in"
                    class="inline-flex items-center py-2 px-4 text-base font-medium text-white rounded-lg bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 dark:focus:ring-blue-900"
                  >
                    Log in
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
                  <RouterLink
                    to="/cart"
                    class="inline-flex items-center py-2 px-4 text-base font-medium text-white rounded-lg border border-white hover:bg-gray-100 hover:text-gray-900 focus:ring-4 focus:ring-gray-400"
                  >
                    <i class="pi pi-shopping-cart"></i> &nbsp; Cart
                  </RouterLink>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
  </header>

  <section class="section">
    <RouterView />
  </section>

  <footer class="footer">
    <p class="text-center">Copyright (c) 2025</p>
  </footer>
</template>

<style scoped>
/* header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
} */
.transition {
  @apply transform transition-all;
}
</style>
