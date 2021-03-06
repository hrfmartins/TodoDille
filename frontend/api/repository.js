export default $axios => ({
  async getLists () {
    return await $axios.$get('/list/')
  },

  async getListInfo (listId) {
    return await $axios.$get('/tasks/', { params: { list_id: listId } })
  },

  async completeTask (listId, taskId, complete) {
    const dto = { list_id: listId, task_id: taskId, complete }
    return await $axios.$put('/tasks/complete',
      dto)
  },

  async changeTask (task) {
    return await $axios.$put('/tasks/update', task)
  },

  async createTask (task) {
    return await $axios.$post('/tasks/create', task)
  },

  async getTodayTasks (task) {
    return await $axios.$get('/tasks/today', task)
  }
})
