<script setup>
import { reactive } from 'vue'
import { RouterLink } from 'vue-router'
import RecipeCard from './RecipeCard.vue'
import { use_recipe_store } from '@/stores/'
import { storeToRefs } from 'pinia'

const recs = use_recipe_store()
const { recipes } = storeToRefs(recs)

const state = reactive({
  recipes: recipes,
})
</script>

<template>
  <h1 class="text-3xl font-bold mb-6 text-gray-100 text-center">Recettes 🍽️</h1>
  <div class="text-center">
    <RouterLink
      to="/add-recipe"
      class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
    >
      Nouvelle recette
    </RouterLink>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 text-gray-100">
    <RecipeCard v-for="recipe in state.recipes" :key="recipe.id" :recipe_obj="recipe" />
  </div>
</template>
