<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';

const route = useRoute();

const quantity = ref(1);

const product = ref({});

onMounted( async () => {
  try{
    const category_slug = route.params.category_slug
    const product_slug = route.params.product_slug
    const response =  await axios.get(`/api/v1/products/${category_slug}/${product_slug}/`);
    product.value = response.data;
    console.log(product.value)
  }catch(error){
    console.log('Failed to get data');
    console.log(error)
  }
})



</script>

<template>

<section class="py-8 bg-white md:py-16 dark:bg-gray-900 antialiased">
    <div class="max-w-screen-xl px-4 mx-auto 2xl:px-0">
      <div class="lg:grid lg:grid-cols-2 lg:gap-8 xl:gap-16">
        <div class="shrink-0 max-w-md lg:max-w-lg mx-auto">
          <!-- <img class="w-full dark:hidden" :src="product.get_image" alt="" /> -->
          <img class="w-full hidden dark:block" :src="product.get_image" alt="" />
          <p class="text-md font-extrabold text-gray-900 sm:text-3xl dark:text-white mt-3"> {{  product.name }}</p>
          <p class="mb-6 mt-3 text-gray-500 dark:text-gray-400">
            {{ product.description }}
          </p>
        </div>

        <div class="mt-6 sm:mt-8 lg:mt-0">
          <h1
            class="text-xl font-semibold text-gray-900 sm:text-2xl dark:text-white"
          >
           Information
          </h1>
          <div class="mt-4 sm:items-center sm:gap-4 sm:flex">
            <p class="text-md font-bold text-gray-900 sm:text-3xl dark:text-white">
              Price:
            </p> <p class="text-lg font-medium font-mono"> ${{ product.price }} </p>


          </div>

          <div class="mt-6 sm:gap-4 sm:items-center sm:flex sm:mt-8">


              <input type="number" class="block w-full p-2 px-5 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-xs focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" v-model="quantity">





          </div>

          <hr class="my-6 md:my-8 border-gray-200 dark:border-gray-800" />




        </div>
      </div>
    </div>
  </section>


</template>
