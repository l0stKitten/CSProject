<template>
    <MenuCompAl/>
    <div class="card custom-margin">
        <div class="container">
            <h2>Justificaciones</h2>
            <div class="right-align">
                <PopUpFormJust/>
            </div>
        </div>
        
        <DataTable :value="justificaciones" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem">
            <Column field="asistencia" header="Asistencia"></Column>
            <Column field="titulo" sortable header="Titulo"></Column>
            <Column field="descripcion" sortable header="Descripcion"></Column>
            <Column field="archivo" sortable header="Archivo"></Column>
        </DataTable>
    </div>
</template>

<script>
    import axios from 'axios'
    import MenuCompAl from './MenuCompAl.vue';
    import PopUpFormJust from './PopUpFormJust.vue';

    export default {
        components: {
            MenuCompAl, PopUpFormJust
        }, data() {
        return {
            justificaciones: [],
            postURL: 'http://127.0.0.1:5000',
            config_request: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
        }
    },
    created() {
        axios.post(this.postURL + '/justificaciones')
            .then((res) => { this.justificaciones = res.data; })
            .catch((error) => { console.log(error) })
    },
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