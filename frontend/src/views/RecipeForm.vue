<script setup>
import router from '@/router'
import { reactive, ref } from 'vue'
import { use_recipe_store } from '@/stores/recipeStore'

const recs = use_recipe_store()

const file_name = ref('or drag and drop')

const recipe_form = reactive({
  nom_r: '',
  description: '',
  ingredients: '',
  image: '',
})

const handle_image_upload = (event) => {
  const file = event.target.files[0]
  recipe_form.image = file.name
  file_name.value = file.name
}

const add_new_recipe = () => {
  if (
    !recipe_form.nom_r ||
    !recipe_form.description ||
    !recipe_form.ingredients ||
    !recipe_form.image
  )
    return

  recs.add_recipe({
    id: Date.now(),
    nom_r: recipe_form.nom_r,
    description: recipe_form.description,
    ingredients: recipe_form.ingredients,
    image: recipe_form.image,
  })

  recipe_form.nom_r = ''
  recipe_form.description = ''
  recipe_form.ingredients = ''
  recipe_form.image = ''
  file_name.value = 'or drag and drop'

  router.push('/')
}

const reset_form = () => {
  recipe_form.nom_r = ''
  recipe_form.description = ''
  recipe_form.ingredients = ''
  recipe_form.image = ''
  file_name.value = 'or drag and drop'
}
</script>

<template>
  <section>
    <div class="max-w-lg mx-auto p-6 shadow-lg rounded-lg">
      <h1 class="text-3xl font-bold mb-4 text-emerald-50">Ajouter une nouvelle recette 🍜</h1>
      <div class="my-5"></div>

      <form @submit.prevent="add_new_recipe">
        <label for="nomrec" class="block text-sm/6 font-bold text-gray-100 my-2"
          >Nom de la recette</label
        >
        <input
          v-model="recipe_form.nom_r"
          type="text"
          id="nomrec"
          placeholder="Nom de la recette"
          class="block w-full rounded-md px-3 py-1.5 text-base text-emerald-50 outline-1 -outline-offset-1 outline-gray-500 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-400 sm:text-sm/6 mb-5"
        />

        <div class="col-span-full"></div>

        <label for="about" class="block text-md/6 font-bold text-gray-100">À propos</label>
        <div class="mt-2"></div>
        <textarea
          v-model="recipe_form.description"
          id="about"
          placeholder="..."
          class="block w-full rounded-md px-3 py-1.5 text-base text-emerald-50 outline-1 -outline-offset-1 outline-gray-500 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-400 sm:text-sm/6"
          rows="3"
        >
        </textarea>
        <div>
          <p class="mt-3 text-sm/6 text-gray-300 mb-4">Description de la recete.</p>
        </div>

        <label for="ing" class="block text-sm/6 font-bold text-gray-100 my-2">Ingrédients</label>
        <input
          v-model="recipe_form.ingredients"
          type="text"
          id="ing"
          placeholder="séparées des vigules"
          class="block w-full rounded-md px-3 py-1.5 text-base text-emerald-50 outline-1 -outline-offset-1 outline-gray-500 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-400 sm:text-sm/6 mb-5"
        />

        <label for="photo" class="block text-sm/6 font-bold text-gray-100 my-2">Photo</label>
        <div class="text-center"></div>
        <div
          class="flex flex-col items-center justify-center p-6 border-2 border-dashed border-gray-300 rounded-lg bg-dark"
        >
          <!-- SVG Icon -->
          <svg
            v-if="recipe_form.image === ''"
            class="mx-auto h-12 w-12 text-gray-300"
            viewBox="0 0 24 24"
            fill="currentColor"
            aria-hidden="true"
          >
            <path
              fill-rule="evenodd"
              d="M1.5 6a2.25 2.25 0 0 1 2.25-2.25h16.5A2.25 2.25 0 0 1 22.5 6v12a2.25 2.25 0 0 1-2.25 2.25H3.75A2.25 2.25 0 0 1 1.5 18V6ZM3 16.06V18c0 .414.336.75.75.75h16.5A.75.75 0 0 0 21 18v-1.94l-2.69-2.689a1.5 1.5 0 0 0-2.12 0l-.88.879.97.97a.75.75 0 1 1-1.06 1.06l-5.16-5.159a1.5 1.5 0 0 0-2.12 0L3 16.061Zm10.125-7.81a1.125 1.125 0 1 1 2.25 0 1.125 1.125 0 0 1-2.25 0Z"
              clip-rule="evenodd"
            ></path>
          </svg>

          <!-- Upload Label -->
          <div class="mt-4 flex text-sm text-gray-600">
            <label
              for="file-upload"
              class="relative cursor-pointer rounded-md font-semibold text-emerald-50 focus-within:ring-2 focus-within:ring-indigo-600 focus-within:ring-offset-2 hover:text-indigo-500"
            >
              <span>Upload file</span>
              <input
                @change="handle_image_upload"
                id="file-upload"
                name="file-upload"
                type="file"
                class="sr-only"
              />
            </label>
            <p :class="{ 'pl-1': true, 'text-gray-300': file_name !== 'or drag and drop' }">
              {{ file_name }}
            </p>
          </div>

          <!-- File type info -->
          <p v-if="recipe_form.image === ''" class="text-xs text-gray-600 mt-1">
            PNG, JPG, GIF up to 10MB
          </p>
        </div>

        <div class="mt-6 flex items-center justify-end gap-x-6">
          <button @click="reset_form" type="button" class="text-sm/6 font-semibold text-gray-100">
            Annuler
          </button>
          <button
            type="submit"
            class="rounded-md bg-indigo-700 px-3 py-2 text-sm font-semibold text-white shadow-xs hover:bg-indigo-600 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          >
            Ajouter
          </button>
        </div>
      </form>
    </div>
  </section>
</template>
