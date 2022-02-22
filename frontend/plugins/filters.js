import Vue from 'vue'
import moment from 'moment'

Vue.filter('capitalize', val => val ? val[0].toUpperCase() + val.substring(1) : '')
Vue.filter('uppercase', val => val ? val.toUpperCase() : '')

Vue.filter('formatMonth', val => moment(val).format('MMM YY'))
Vue.filter('formatDate', val => moment(val).format('DD-MM-YYYY'))
