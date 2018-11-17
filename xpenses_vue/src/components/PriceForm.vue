<template>
    <form class='form-inline'>
        <input type="text" class="form-control" placeholder="Nazwa" v-model="form.name.v">
        <input type="text" class="form-control" placeholder="Cena" v-model.number="form.price.v">
        <input type="text" class="form-control" placeholder="Kategoria" v-model="form.category.v">
        <button type="submit" class="btn btn-primary" @click='postExpense'>Dodaj</button>
    </form>
</template>


<script>
import axios from 'axios'
import uuid from 'uuid/v4'

export default {
    data(){
        return {
            form:{
                name: { v:'', e:false },
                price: { v:0, e:false },
                category: { v:'', e:false },
            }
        }
    },

    methods: {
        postExpense(){
            axios.post('expense.json', this.form)
                .then(response => {
                    console.log(response);
                    this.$emit('sentit')
                })
            this.form = {
                name: { v:'', e:false },
                price: { v:'', e:false },
                category: { v:'', e:false },
            }


        }
    }
}
    
</script>


<style lang="scss" scoped>
    input{
        margin-left: 10px;
    }
    button{
        margin-left: 12px;
    }
</style>
