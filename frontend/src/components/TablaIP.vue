<template>
  <div class="p-4 bg-white rounded shadow mt-4">
    <h3 class="font-semibold mb-2">IPs</h3>
    <table class="w-full border-collapse">
      <thead>
        <tr>
          <th class="border px-2 py-1">IP</th>
          <th class="border px-2 py-1">Count</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in data" :key="index">
          <td class="border px-2 py-1">{{ item.ip }}</td>
          <td class="border px-2 py-1">{{ item.count }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'TablaIP',
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
