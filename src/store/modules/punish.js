import punishService from '../../services/punishService'
import {cloneDeep} from "lodash";
import {baseState, baseMutations} from "../state";

const state = {
  ...cloneDeep(baseState),
  penalty: []
}

const getters = {
  penalties: state => {
    return state.penalties
  }
}

const actions = {
  getAllPenalty ({ commit }) {
    punishService.fetchAllPenalty()
    .then(penalty => {
        console.log(penalty);
      commit('setPenalty', penalty)
    })
  },
}

const mutations = {
  ...cloneDeep(baseMutations),
  setPenalty (state, penalty) {
    state.penalty = penalty
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
