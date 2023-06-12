<template>
    <MenuCompAl/>
    <div class="card custom-margin">
        <div class="container">
            <h2>Asistencias</h2>
        </div>
        
        <DataTable :value="asistencias" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem">
            <Column field="estado" header="Estado"></Column>
            <Column field="fecha_asistencia" sortable header="Fecha Asistencia"></Column>
            <Column field="matricula" sortable header="matricula"></Column>
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
            asistencias: [],
            postURL: 'http://127.0.0.1:5000',
            config_request: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
        }
    },
    created() {
        axios.post(this.postURL + '/asistencias')
            .then((res) => { this.asistencias = res.data; })
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