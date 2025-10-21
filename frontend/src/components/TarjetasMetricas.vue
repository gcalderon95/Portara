<template>
  <div class="p-4 bg-white rounded shadow">
    <h3 class="font-semibold">{{ title }}</h3>
    <p class="text-2xl">{{ value }}</p>
  </div>
</template>

<script>
export default {
  name: 'TarjetasMetricas',
  props: {
    title: String,
    value: [String, Number]
  }
}
</script>

<style scoped>
/* Estilos opcionales */
</style>
