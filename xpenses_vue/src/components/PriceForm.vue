<template>
    <form class='form-inline'>
        <input type="text" class="form-control" placeholder="Nazwa" v-model="form.name">
        <input type="text" class="form-control" placeholder="Cena" v-model.number="form.price">
        <input type="text" class="form-control" placeholder="Kategoria" v-model="form.category">
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
                name: '',
                price: '',
                category: '',
            }
        }
    },

    methods: {
        postExpense(){
            axios.post('expenses_list', this.form)
                .then(response => {
                    console.log(response);
                    this.$emit('sentit')
                })
            this.form = {
                name: '',
                price: '',
                category: '',
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
