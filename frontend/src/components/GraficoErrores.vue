<template>
  <div class="p-4 bg-white rounded shadow mt-4">
    <h3 class="font-semibold mb-2">Error Chart</h3>
    <ul>
      <li v-for="(item, index) in data" :key="index">
        Status {{ item.status }}: {{ item.count }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'GraficoErrores',
  props: {
    data: {
      type: Array,
      default: () => []
    }
  }
}
</script>

<style scoped>
/* Opcional */
</style>
