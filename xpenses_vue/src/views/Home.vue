<template>
  <div class="home">

<div class="container">
  <div class="row justify-content-md-center">

  <div class="col-3"></div>
  <h1 class="col-6">Lista wydatków</h1>
  <div class="col-3"></div>

  <div class="filter row">
    <label>Nazwa:
      <input type="text" class="form-control">
    </label>
  </div>


  <div>
    <label for="">Wszystkie
      <input type="radio" name="a" id="" value="expense.json" v-model="pick" @change="getData">
    </label>
    <label for="">Zwinięte
      <input type="radio" name="a" id="" value="expense_zipped.json" v-model="pick" @change="getData">
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
    <button class="btn btn-primary" @click="undoAllChanges">Undo</button>
    <button class="btn btn-secondary" @click="zip">Zwiń po kategorii</button>
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
      ],
      originalData: [], // for backup
      current: '',
      pick: 'expense.json'
    }
  },
  methods:{
    getData(){
      axios.get(this.pick)
        .then(response => {
          this.tableItems = response.data
          // const copy = JSON.parse(JSON.stringify(response.data))
          this.originalData = JSON.parse(JSON.stringify(response.data))
        })
         .catch(error => {
           console.log(error)
         })
    },
    remove(it, key){
      let dic = {}
      dic[key] = null
      axios.patch(this.pick, dic)
        .then(response => {
          console.log(response);
          this.getData()
        })

    },
    saveAllChanges(){
      // let dic = {}
      // dic[key] = it
      // dic[key].name = 'test'
      for(let key in this.tableItems){
        this.tableItems[key].name.e = false
        this.tableItems[key].price.e = false
        this.tableItems[key].category.e = false
      }
      axios.patch(this.pick, this.tableItems)
        .then(response => {
          console.log(response);
          this.getData()
        })
    },
    undoAllChanges(){
      this.tableItems = JSON.parse(JSON.stringify(this.originalData)) //not assign pointer but data
      // this.getData()

    },
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
    zip(){

      const categorySum = {}
      const keysToDelete = []
      // extract categories
      for(let key in this.tableItems){
        let categoryName = this.tableItems[key].category.v
        let categoryPrice = this.tableItems[key].price.v
        if(categorySum[categoryName] === undefined){
          categorySum[categoryName] = 0
        }
        categorySum[categoryName] += categoryPrice
        keysToDelete.push(key)
      }

      /// post zipped entrys
      const entrysList = createZippedEntrys(categorySum)
        axios.put('expense_zipped.json', {})
          .then(response =>{
            entrysList.forEach(ent => {
              console.log(ent);
              axios.post('expense_zipped.json', ent)
            })
          })
    }
  }
}


const deleteKeys = (keys) => {
  const entrys = {}
  keys.forEach(element => {
    entrys[element] = null
  });
  return entrys
}

/// creates zipped entrys list 
const createZippedEntrys = (categories) => {
  const entrys = []
  for(let key in categories){
      entrys.push({
          name: { v:'-', e:false },
          price: { v:categories[key], e:false },
          category: { v:key, e:false },
      })
  }
  return entrys
}

</script>

<style>

.edited {
  background-color: lightskyblue;
}

</style>
