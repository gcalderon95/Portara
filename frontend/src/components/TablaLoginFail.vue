<template>
  <div class="p-4 bg-white rounded shadow mt-4">
    <h3 class="font-semibold mb-2">Login Failures</h3>
    <table class="w-full border-collapse">
      <thead>
        <tr>
          <th class="border px-2 py-1">User</th>
          <th class="border px-2 py-1">Fails</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in data" :key="index">
          <td class="border px-2 py-1">{{ item.user }}</td>
          <td class="border px-2 py-1">{{ item.fails }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'TablaLoginFail',
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
