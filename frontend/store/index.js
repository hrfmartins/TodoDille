export const state = () => ({
  lists: [],
  activeList: {},
  activeListTasks: {}
})

export const mutations = {
  setLists (state, lists) {
    state.lists = lists
  },

  setActiveList (state, list) {
    state.activeList = list
  },

  setActiveListTasks (state, list) {
    state.activeListTasks = list
  },

  setTaskComplete (state, {
    taskId,
    complete
  }) {
    const task = state.activeListTasks.filter(task => task.id === taskId)[0]
    task.complete = complete
  },

  changeTask (state, _task) {
    const ogTask = state.activeListTasks.filter(task => task.id === _task.id)[0]
    ogTask.complete = _task.complete
    ogTask.date_created = _task.date_created
    ogTask.description = _task.description
    ogTask.title = _task.title
    ogTask.due_date = _task.due_date
  },

  addTask (state, task) {
    state.activeListTasks.push(task)
  }
}

export const actions = {
  setLists (state, lists) {
    state.commit('setLists', lists)
  },

  async getLists ({ state, commit }) {
    await this.$repositories.repo.getLists().then((response) => {
      commit('setLists', response)
    })
  },

  async setActiveList ({ state, commit }, list) {
    if (list.name === 'Today') {
      commit('setActiveList', list)
      await this.$repositories.repo.getTodayTasks().then((response) => {
        commit('setActiveListTasks', response)
      })
    } else {
      commit('setActiveList', list)
      await this.$repositories.repo.getListInfo(list.id).then((response) => {
        commit('setActiveListTasks', response)
      })
    }
  },

  async completeTask ({ state, commit }, {
    taskId,
    complete
  }) {
    await this.$repositories.repo.completeTask(state.activeList.id, taskId, complete).then(() => {
      commit('setTaskComplete', {
        taskId,
        complete
      })
    })
  },

  async changeTask ({ state, commit }, task) {
    await this.$repositories.repo.changeTask(task).then(() => {
      commit('changeTask', task)
    })
  },

  async createTask ({ state, commit }, task) {
    await this.$repositories.repo.createTask(task).then((response) => {
      commit('addTask', response)
    })
  }
}

export const getters = {
  getLists (state) {
    return state.lists
  },

  hasLists (state) {
    return state.lists.length !== 0
  },

  getActiveList (state) {
    return state.activeList
  },

  getActiveListTasks (state) {
    return state.activeListTasks
  }
}
