<script setup>
import { RouterLink } from 'vue-router';

const prop = defineProps({
  latest_prod_obj: Object,
})

</script>

<template>

  <div
    class="flex flex-col items-center bg-white border border-gray-200 rounded-lg shadow-sm md:flex-row md:max-w-xl hover:bg-gray-100 dark:border-gray-700 dark:bg-gray-800 dark:hover:bg-gray-700">

    <RouterLink :to="latest_prod_obj.get_absolute_url">
      <img class="object-cover w-full rounded-t-lg h-96 md:h-auto md:w-48 md:rounded-none md:rounded-s-lg"
        :src="latest_prod_obj.get_thumbnail" alt="">
    </RouterLink>

    <div class="flex flex-col justify-between p-4 leading-normal">
      <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">{{ latest_prod_obj.name }}</h5>
      <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">${{ latest_prod_obj.price }}</p>

      <RouterLink :to="latest_prod_obj.get_absolute_url"
        class="px-4 py-2 text-md font-medium tracking-tight text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
        View details
      </RouterLink>

    </div>
  </div>
</template>

<style scoped>
.image {
  margin-top: -1.25rem;
  margin-right: -1.25rem;
  margin-left: -1.25rem;
}
</style>
