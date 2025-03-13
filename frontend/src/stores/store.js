import { defineStore } from 'pinia'

export const use_recipe_store = defineStore('djackets_store', {
  state: () => ({
    recipes: JSON.parse(localStorage.getItem('recipes')) || [],
  }),

  actions: {
    add_recipe(recipe) {
      this.recipes.push(recipe)
      localStorage.setItem('recipes', JSON.stringify(this.recipes))
    },

    // del_recipe(id) {
    //   this.recipes = this.recipes.filter((r) => r.id !== r.id)
    //   localStorage.setItem('recipes', JSON.stringify(this.recipes))
    // },
  },

  getters: {},
})
