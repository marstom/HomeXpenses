<template>
  <div class="about">
    <h1>Ta strona jest testopa</h1>
    <div>Testinig content print here .... {{ hello }} </div>
    <hr>

    <div v-for="e in expenses"> {{ e }} </div>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  created(){
    this.getExpensesList()
  },

  data(){
    return {
      hello: 'tomek',
      expenses: ''

    }
  },

  methods: {
    getExpensesList(){
      axios.get('expenses_list')
      .then(response => {
        this.data = response.data
        this.expenses = response.data
      })
    }
  }

}
</script>
