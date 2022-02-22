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
    commit('setActiveList', list)
    await this.$repositories.repo.getListInfo(list.id).then((response) => {
      commit('setActiveListTasks', response)
    })
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
