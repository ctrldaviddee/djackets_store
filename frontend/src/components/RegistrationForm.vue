<script setup>
import { computed, reactive, ref } from 'vue'

const form = reactive({
  nom: '',
  prenom: '',
  email: '',
  mdp: '',
})

const submitted = ref(false)

const isvalid_surname = computed(() => /[a-zA-Z\s]{2,}/.test(form.nom))
const isvalid_name = computed(() => /[a-zA-Z\s]{2,}/.test(form.prenom))
const isvalid_password = computed(() => /[A-Za-z\d@#$%^&]{8,}/.test(form.mdp))
const isvalid_email = computed(() => /\S+@\S+\.\S+/.test(form.email))

const handle_regisration = () => {
  if (
    isvalid_surname.value &&
    isvalid_name.value &&
    isvalid_email.value &&
    isvalid_password.value
  ) {
    submitted.value = true
    alert('Reussi')
  }
}
</script>

<template>
  <form @submit.prevent="handle_regisration">
    <label for="nom">Nom</label>
    <input v-model="form.nom" type="text" id="nom" />
    <div v-if="submitted && !isvalid_surname" class="error_div'">
      Remplissez proprement ce champ
    </div>
    <br />

    <label for="prenom">Prénom</label>
    <input v-model="form.prenom" type="text" id="prenom" />
    <div v-if="submitted && !isvalid_name" class="error_div">Remplissez proprement ce champ</div>
    <br />

    <label for="email">E-mail</label>
    <input v-model="form.email" type="email" id="email" />
    <div v-if="submitted && !isvalid_email" class="error_div">E-mail incorrecte</div>
    <br />

    <label for="mdp">Mot de passe</label>
    <input v-model="form.mdp" type="text" id="mdp" />
    <div v-if="submitted && !isvalid_password" class="error_div">Ce champ est requis</div>
    <br />

    <button type="submit">Soumettre</button>
  </form>
</template>

<style scoped>
.error_div {
  color: rgb(211, 8, 8);
}
</style>
