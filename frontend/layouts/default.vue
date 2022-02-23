<template>
  <div class="background">
    <navbar />
    <dashboard-content>
      <Nuxt />
    </dashboard-content>
  </div>
</template>

<script>
export default {
  name: 'DefaultLayout',
  mounted () {
    if (!this.$store.getters.hasLists) {
      this.$store.dispatch('getLists')
    }
  }
}
</script>

<style scoped>
.background {
  background-image: url("static/img/background.jpg");
  background-size: 100% 300%;
  background-attachment: fixed;
  background-repeat: no-repeat;
  width: 100vw;
  height: 100vh;
  background-position: center center;
  margin:auto;
  padding:0;
  overflow:auto;
}

</style>
