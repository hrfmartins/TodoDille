<template>
  <div class="clickable-area" @click="clickArea">
    <b-row>
      <b-col cols="1">
        <font-awesome-icon class="fa-3x" :icon="['fas', iconName]" />
      </b-col>
      <b-col>
        <h2>{{ item.name }}</h2>
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
      console.log('HEY!')
    }
  }
}
</script>

<style scoped>
.clickable-area {
  width: 95vw;
  margin: auto;
}

.list-icon {
  width: 50px;
}

</style>
