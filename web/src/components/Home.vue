<template>
    <v-container grid-list-md>
        <h4>Tree Classifier </h4>
        <p>This project aims to identify the type of tree in my 
        area using an ML algorithm.</p>
        <p>Classes: 1) Mango 2) Mahagony 3) Teak 4)Coconut 5) Eucalyptus 6) Jackfruit 7) Plantain 8) Teak</p>
        <v-img :src="forest" max-height="450" max-width="1200"></v-img>
        <div class="img-content">
            <template>
            <v-file-input
                label="File input"
                filled
                prepend-icon="mdi-camera"
            ></v-file-input>
            </template>
        </div>
        <div class="content text-center">
            <!-- submit button to accept image -->
            <v-btn rounded @click="submit" type="primary" dark>
                Predict Trees      
            </v-btn>
        </div>
    </v-container>
</template>

<script lang="ts">
import axios from 'axios';
import Vue from 'vue';

export default Vue.extend({
    name: 'Home',

    data: () => ({
        forest: 'https://user-images.githubusercontent.com/24592806/124379282-b3578680-dcd3-11eb-9927-f59ef29bf6b8.jpg',
    }),

    methods:  {
        submit: function() {
            const file = this.$refs.file.files[0];
            let params = new FormData();

            params.append('file', file);
            params.append('type', 'image');
            console.log(params);
            axios.post(`http://localhost:5000/api`)
        }   
    }
})
</script>