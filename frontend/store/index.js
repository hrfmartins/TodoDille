export const state = () => ({
  lists: [],
  activeList: {}
})

export const mutations = {
  setLists (state, lists) {
    state.lists = lists
  },

  setActiveList (state, list) {
    state.activeList = list
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

  setActiveList ({ state, commit }, list) {
    commit('setActiveList', list)
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
  }
}
