<template>
  <div class="content">
    <NuxtChild />
  </div>
</template>

<script>
export default {
  name: 'DashboardContent'
}
</script>

<style scoped>
.content {
  width: 98vw;
  height: 100vh;
  margin: auto;
  padding-top: 2vh;
}
</style>
