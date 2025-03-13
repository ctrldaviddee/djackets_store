<script setup>
import { RouterLink } from 'vue-router'
import { ref, computed } from 'vue'

const full_description = ref(false)

const toggle_full_description = () => {
  full_description.value = !full_description.value
}

const props = defineProps({
  recipe_obj: Object,
})

const shorten_description = computed(() => {
  let description = props.recipe_obj.description
  if (!full_description.value) {
    description = description.substring(0, 95) + '...'
  }
  return description
})

function get_image_url(name, ext) {
  return new URL(`../assets/img/${name}.${ext}`, import.meta.url).href
}

function get_image_url_1(name) {
  return new URL(`../assets/img/${name}`, import.meta.url).href
}
</script>

<template>
  <div class="rounded-xl shadow-md relative">
    <div class="p-4">
      <div class="mb-6">
        <div class="text-gray-300 text-xl font-bold my-2">{{ recipe_obj.nom_r }}</div>
      </div>

      <div class="mb-2">
        <div>{{ shorten_description }}</div>
        <button
          @click="toggle_full_description"
          class="text-gray-400 hover:text-teal-600 mb-5 my-3"
        >
          {{ full_description ? 'Lire moins' : 'Lire plus' }}
        </button>
      </div>

      <div class="text-white">
        <img
          class="max-w-xs max-h-fit rounded-lg"
          :src="get_image_url_1(recipe_obj.image)"
          alt="image"
        />
      </div>

      <div class="mb-3">
        <p class="text-md/6 font-bold text-gray-100">Ingrédients</p>
        <h3 class="text-blue-400">{{ recipe_obj.ingredients }}</h3>
      </div>

      <RouterLink
        :to="`/recette/${recipe_obj.nom_r}`"
        class="inline-flex justify-center items-center py-2.5 px-5 text-base font-medium text-center text-white rounded-lg bg-teal-700 hover:bg-teal-800 focus:ring-4 focus:ring-blue-300 dark:focus:ring-blue-900"
      >
        En savoir plus
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
    </div>
  </div>
</template>
