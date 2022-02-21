export default $axios => ({
  async getLists (token) {
    return await $axios.$get('/list/', {
      token
    })
  }
})
