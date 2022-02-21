<template>
  <div>
    <b-list-group>
      <div class="mb-3">
        <b-list-group-item class="list-group-item">
          <ListDisplay class="display-inside" :item="preLists[0]" icon-name="calendar-day" />
        </b-list-group-item>
      </div>
      <div class="mb-3">
        <b-list-group-item class="list-group-item">
          <ListDisplay class="display-inside" :item="preLists[1]" icon-name="inbox" />
        </b-list-group-item>
      </div>
      <div class="mb-3">
        <b-list-group-item class="list-group-item">
          <ListDisplay class="display-inside" :item="preLists[2]" icon-name="list" />
        </b-list-group-item>
      </div>
    </b-list-group>

    <hr>

    <b-list-group class="mt-4">
      <div v-for="item in lists" :key="item.id" class="mb-3">
        <b-list-group-item class="list-group-item">
          <ListDisplay class="display-inside" :item="item" />
        </b-list-group-item>
      </div>
    </b-list-group>
  </div>

</template>

<script>
import ListDisplay from '@/components/ListDisplay'

export default {
  name: 'ListsPage',
  components: [
    ListDisplay
  ],
  data () {
    return {
      preLists: [
        { name: 'Today' },
        { name: 'Inbox' },
        { name: 'All' }
      ]
    }
  },
  computed: {
    lists () {
      return this.$store.getters.getLists
    }
  }
}
</script>

<style scoped>
.list-group-item {
  display: flex;
  padding: 0;
  height: 10vh;
  background: rgba(255, 255, 255, 0.86);
  border-radius: 10px;
}

.list-group-item:hover {
  background: lightgrey;
  transition: 0.3s;
}

.display-inside {
  margin-left: 20px;
}

hr {
  margin-top: 1rem;
  margin-bottom: 1rem;
  border: 0;
  border-top: 1px solid rgba(255, 255, 255, 1);
}
</style>
