<template>
  <div class="home">

<div class="container">
  <div class="row justify-content-md-center">

  <div class="col-3"></div>
  <h1 class="col-6 header">Lista wydatków</h1>
  <div class="col-3"></div>

  <div class="filter row">
    <label>Filtruj wydatki:
      <input type="text" v-model="filter" class="form-control">
    </label>
  </div>

      <table class="table table-bordered">
        <thead>
          <tr>
            <th>Id</th>
            <th>Nazwa</th>
            <th>Cena</th>
            <th>Kategoria</th>
            <th>Akcja</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(it, key) in tableItems" :key="key" v-bind="current">
            <td>#</td>
            <td><input type="text" class="form-control" :class="{'edited':it.name.e}" :value="it.name.v" @change="editedInput($event, key, 'name')"></td>
            <td><input type="text" class="form-control" :value="it.price.v" :class="{'edited':it.price.e}" @change="editedInput($event, key, 'price')"></td>
            <td><input type="text" class="form-control" :value="it.category.v" :class="{'edited':it.category.e}" @change="editedInput($event, key, 'category')"></td>
            <td>
            <button class="btn btn-danger btn-sm" @click="remove(it, key)"><i class="fa fa-trash" aria-hidden="true"></i></button>
            </td>
          </tr>
        </tbody>
      </table>

  <div class="col-12">
    <button class="btn btn-warning" @click="saveAllChanges">Save all changes</button>
  </div>
      <price-form @sentit="getData"></price-form>
  </div>
</div>



  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import PriceForm from '@/components/PriceForm.vue'
import axios from 'axios'

export default {
  name: 'home',
  components: {
    HelloWorld,
    PriceForm
  },
  created(){
    this.getData()
  },
  data(){
    return {
      tableItems:[
        {
          name: { v:'...', e:false },
          price: { v:'...', e:false },
          category: { v:'...', e:false },
        },
        {
          name: { v:'kromka', e:false },
          price: { v:'2.50', e:false },
          category: { v:'Jedzenie', e:false },
        },
        {
          name: { v:'dżem', e:false },
          price: { v:'8.50', e:false },
          category: { v:'Jedzenie', e:false },
        },
      ],
      originalData: [], // for backup
      current: '',
      pick: '/expenses_list'
    }
  },
  methods:{
    getData(){
      axios.get('expenses_list')
      .then(response => {
        this.tableItems = []
        let data = response.data
        console.log(data)

        for(let i=0; i<data.length; i++){
          let temp = data[i]
          data[i].name = {v:temp.name, e:false}
          data[i].price = {v:temp.price, e:false}
          data[i].category = {v:temp.category, e:false}
          console.log(data[i])
        }

        this.tableItems = data
      })
      .catch(error => {
        console.log(error)
      })
    },

    // remove item from list, perform DELETE
    remove(it, key){
      let primary_key = it.pk
      axios.delete(`expense/${primary_key}`)
        .then(response =>{
          console.log(response)
          this.getData()
        })
      // console.log(it.pk, key)
    },

    // post all changes to database
    saveAllChanges(){
      for(let key in this.tableItems){
        this.tableItems[key].name.e = false
        this.tableItems[key].price.e = false
        this.tableItems[key].category.e = false
      }

      axios.patch('expenses_list', this.tableItems)
        .then(response => {
          console.log(response)
          this.getData()
        })
          .catch(error =>{
            console.log(error)
        })
    },

    undoAllChanges(){
    },

    // method
    // if user echange field, color it blue, set e to true
    editedInput(e, key, typ){
      if(typ === 'name'){
        this.tableItems[key].name.v = e.target.value
        this.tableItems[key].name.e = true
      }
      if(typ === 'price'){
        this.tableItems[key].price.v = parseFloat(e.target.value)
        this.tableItems[key].price.e = true
      }
      if(typ === 'category'){
        this.tableItems[key].category.v = e.target.value
        this.tableItems[key].category.e = true
      }

    },

  },
  computed:{
    filter: {
      set(v){
        console.log('value', v)
        let filtered = this.tableItems.filter((value) => {
          return value.name.v.includes(v)
        })
        this.tableItems = filtered
        return v
      }
    }

  }
}
</script>

<style>

.edited {
  background-color: lightskyblue;
}

.header {
  color: rgb(58, 58, 158);
}

</style>
