<template>
  <div>
    <b-card>
      <h3> {{ list.name }}</h3>
    </b-card>

    <b-card class="mt-2">
      <b-list-group-item v-for="el in activeListTasks" :key="el.title">
        <b-row>
          <b-col>
            {{ el.title }}
          </b-col>
          <b-col>
            {{ el.description }}
          </b-col>
          <b-col>
            {{ el.due_date }}
          </b-col>
          <b-col>
            <b-button
              :variant="buttonVariant(el.complete)"
              @click="updateState(el.id, el.complete)"
            >
              <font-awesome-icon :icon="['fas', completedIcon(el.complete)]" />
            </b-button>
          </b-col>
        </b-row>
      </b-list-group-item>
    </b-card>
  </div>
</template>

<script>
export default {
  name: 'TasksPage',
  computed: {
    list () {
      return this.$store.getters.getActiveList
    },
    activeListTasks () {
      return this.$store.getters.getActiveListTasks
    }
  },
  methods: {
    buttonVariant (complete) {
      return complete ? 'success' : 'outline-primary'
    },
    completedIcon (complete) {
      return complete ? 'check' : 'times'
    },
    updateState (taskId, complete) {
      const isComplete = !complete
      this.$store.dispatch('completeTask', { taskId, complete: isComplete })
    }
  }
}
</script>

<style scoped>

</style>
