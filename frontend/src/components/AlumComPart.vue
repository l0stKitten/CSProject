<template>
    <MenuCompAl/>
    <div class="card custom-margin">
        <div class="container">
            <h2>Participaciones</h2>
        </div>
        
        <DataTable :value="participaciones" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem">
            <Column field="asistencia" header="Asistencia"></Column>
            <Column field="cantidad" sortable header="Cantidad"></Column>
        </DataTable>
    </div>
</template>

<script>
    import axios from 'axios'
    import MenuCompAl from './MenuCompAl.vue';

    export default {
        components: {
            MenuCompAl
        }, data() {
        return {
            participaciones: [],
            postURL: 'http://127.0.0.1:5000',
            token: localStorage.getItem('access_token')
        }
    },
    created() {
        const config = {
            headers: {
                'Authorization': `Bearer ${this.token}`,
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        };

        axios.post(this.postURL + '/participaciones', null, config)
            .then((res) => { this.participaciones = res.data; })
            .catch((error) => { console.log(error) })
    }
};
</script>

<style scoped>
    .custom-margin {
        margin-top: 50px;
    }
    .container {
        display: flex;
        justify-content: space-between;
        margin-bottom: 10px;
    }

    .container h2 {
        margin: 0;
    }
</style>