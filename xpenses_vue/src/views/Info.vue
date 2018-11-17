<template>
  <div class="about">
    <h1>Ta strona jest testopa</h1>
    <div>Testinig content print here .... {{ hello }} </div>
    <div>Testinig content print here .... {{ getExpensesList() }} </div>
    <div></div>
  </div>
</template>

<script>
export default {
  data(){
    return {
      hello: 'tomek'

    }
  },

  methods: {
    getExpensesList(){
      return {1: 'e1', 2:'e2'}
    }
  }

}
</script>
