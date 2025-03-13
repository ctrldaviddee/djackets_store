<script setup>
import JacketCardListings from '@/components/JacketCardListings.vue';

function get_mage_url(name, ext) {
  try {
    return new URL(`../assets/media/${name}.${ext}`, import.meta.url).href
  } catch (error) {
    return ''
  }
}
</script>

<template>
  <!-- Cards: User -->
  <div
    class="flex flex-col overflow-hidden rounded-lg bg-white shadow-xs dark:bg-gray-800 dark:text-gray-100"
  >
    <!-- Card Cover/Avatar -->
    <div
      class="mb-8 bg-cover"
      style="
        background-image: url('https://cdn.tailkit.com/media/placeholders/photo-JgOeRuGD_Y4-800x400.jpg');
      "
    >
      <div class="flex h-32 items-end justify-center">
        <div class="-mb-12 rounded-full bg-gray-200/50 p-2 dark:bg-gray-600/50">
          <img
            :src="get_mage_url('avatarjacket', 'jpeg')"
            alt="User Avatar"
            class="inline-block size-30 rounded-full"
          />
        </div>
      </div>
    </div>
    <!-- END Card Cover/Avatar -->

    <!-- Card Body -->
    <div class="grow p-5 text-center">
      <h3 class="mt-3 mb-1 lg:text-6xl text-4xl font-semibold">
        Welcome to Djack
        <svg
          class="hi-mini hi-cube-transparent inline-block size-9 text-blue-600 transition dark:text-gray-400"
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
        ts
      </h3>
      <p class="mt-5 md:text-lg text-md font-medium text-gray-600 dark:text-gray-400">
        One of the best jacket store online
      </p>
    </div>
    <!-- END Card Body -->
  </div>
  <!-- END Cards: User -->

  <JacketCardListings :limit="3"/>

</template>
