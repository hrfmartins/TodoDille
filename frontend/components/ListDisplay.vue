<template>
  <div class="clickable-area" @click="clickArea">
    <b-row v-if="iconName !== '' ">
      <b-col cols="1">
        <font-awesome-icon class="fa-3x" :icon="['fas', iconName]" />
      </b-col>
      <b-col>
        <h4 class="m-0">
          {{ item.name }}
        </h4>
      </b-col>
    </b-row>

    <b-row v-else>
      <b-col cols="9">
        <h4 class="m-0">
          {{ item.name }}
        </h4>
      </b-col>
      <b-col>
        <p>Created on {{ $moment(item.date_created).format('YYYY-MM-D') }}</p>
      </b-col>
    </b-row>
  </div>
</template>

<script>
export default {
  name: 'ListDisplay',
  props: {
    item: {
      type: Object,
      default () {
        return {}
      }
    },
    iconName: {
      type: String,
      default () {
        return ''
      }
    }

  },
  methods: {
    clickArea () {
      this.$store.dispatch('setActiveList', this.item)
      this.$router.push('tasks')
    }
  }
}
</script>

<style scoped>
.clickable-area {
  width: 100%;
  margin: auto;
}

.list-icon {
  width: 50px;
}

</style>
