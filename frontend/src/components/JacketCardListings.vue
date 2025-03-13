<script setup>
import { reactive, onMounted} from 'vue';
import { RouterLink } from 'vue-router';
import JacketCardListing from './JacketCardListing.vue';
import RingLoader from 'vue-spinner/src/RingLoader.vue';
import axios from 'axios';

const props = defineProps({
  limit: Number,
})

const state = reactive({
  latest_products: [],
  is_loading: true,
})

onMounted(async ()=> {
  try {
    const response = await axios.get('/api/v1/latest-products/');
    state.latest_products = response.data;
    console.dirxml
  } catch (error) {
    console.log('Error fetching data', error);
  }finally{
    state.is_loading = false;

  }
})
</script>

<template>
<section class=" px-4 py-10 mt-7">
    <div class="container-xl lg:container m-auto">
      <h2 class="text-3xl font-bold text-white mb-6 text-center">
        Latest Products
      </h2>
      <!-- Show loading spinner while loading is true -->
      <div v-if="state.is_loading" class="text-center text-gray-500 py-6">
        <RingLoader />
      </div>

      <!-- Shoe job listing when done loading -->
      <div v-else class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <JacketCardListing
          v-for="product in state.latest_products.slice(0, limit || state.latest_products.length)"
          :key="product.name"
          :latest_prod_obj="product"
        />
      </div>
    </div>
  </section>
</template>
