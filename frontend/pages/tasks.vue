<template>
  <div>
    <b-card>
      <b-row>
        <b-col cols="10">
          <h3> {{ list.name }}</h3>
        </b-col>
        <b-col align-self="right">
          <h6> {{ list.date_created | formatDate }}</h6>
        </b-col>
      </b-row>
      <b-button @click="newTaskModal = !newTaskModal">New Task</b-button>
    </b-card>

    <b-card class="mt-2">
      <b-list-group-item class="list-header">
        <b-row>
          <b-col cols="2">
            Title
          </b-col>
          <b-col cols="6">
            Description
          </b-col>
          <b-col cols="2">
            Due Date
          </b-col>
          <b-col>
            Edit
          </b-col>
          <b-col>
            Completed
          </b-col>
        </b-row>
      </b-list-group-item>
      <b-list-group-item v-for="el in activeListTasks" :key="el.title">
        <b-row>
          <b-col cols="2">
            {{ el.title }}
          </b-col>
          <b-col cols="6">
            {{ el.description }}
          </b-col>
          <b-col :id="'target-' + el.id" ref="button" cols="2" @click="togglePopover(el.id, el.due_date)">
            <font-awesome-icon :class="expired(el.due_date, el.complete)" :icon="['fas', 'clock']"/>
            <span :class="expired(el.due_date, el.complete)">{{ el.due_date | formatDate }}</span>
          </b-col>
          <b-col>
            <b-button>
              <font-awesome-icon :icon="['fas', 'pencil']"></font-awesome-icon>
            </b-button>
          </b-col>
          <b-col>
            <b-button
              :variant="buttonVariant(el.complete)"
              @click="updateState(el.id, el.complete)"
            >
              <font-awesome-icon :icon="['fas', completedIcon(el.complete)]"/>
            </b-button>
          </b-col>
        </b-row>
      </b-list-group-item>
      <b-modal v-model="pop" @ok="onOk" @cancel="onCancel" title="Due date">
        <b-form-datepicker id="example-datepicker" v-model="date" class="mb-2"></b-form-datepicker>
      </b-modal>

      <b-modal v-model="newTaskModal" title="New Task" @ok="onNewTaskOk" @cancel="onCancel">
        <div>
          <span>Title</span>
          <b-form-input v-model="newTask.title" placeholder="Your title"/>
        </div>
        <div class="mt-3">
          <span>Description</span>
          <b-form-input v-model="newTask.description" placeholder="Your Description"/>
        </div>
        <div class="mt-3">
          <p>Due Date</p>
          <b-form-datepicker
            id="example-datepicker"
            v-model="newTask.due_date"
          />
        </div>
      </b-modal>
    </b-card>
  </div>
</template>

<script>
import moment from 'moment/moment'

export default {
  name: 'TasksPage',
  data () {
    return {
      pop: false,
      targetTask: 0,
      date: '',
      newTaskModal: false,
      newTask: {
        title: '',
        description: '',
        due_date: null,
        list_id: 0
      }
    }
  },
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
      this.$store.dispatch('completeTask', {
        taskId,
        complete: isComplete
      })
    },

    expired (dueDate, completed) {
      if ((moment() > moment(dueDate)) && !completed) {
        return 'text-danger'
      } else {
        return 'text-black-50'
      }
    },

    togglePopover (id, dueDate) {
      this.targetTask = id
      this.date = dueDate
      this.pop = !this.pop
    },

    onCancel () {
      this.targetTask = 0
      this.date = ''
      this.pop = false
    },

    onOk () {
      const task = this.activeListTasks.filter(faTasks => faTasks.id === this.targetTask)[0]
      task.due_date = this.date
      this.$store.dispatch('changeTask', task)
    },

    onNewTaskOk () {
      this.newTask.due_date = moment(this.newTask.due_date)
      this.newTask.list_id = this.list.id
      this.$store.dispatch('createTask', this.newTask)
      this.newTask = {
        title: '',
        description: '',
        due_date: null,
        list_id: 0
      }
    }
  }
}
</script>

<style scoped>
.list-header {
  background: rgba(95, 158, 160, 0.86);
  color: white;
}
</style>
