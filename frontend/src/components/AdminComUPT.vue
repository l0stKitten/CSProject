<template>
    <MenuCompAd/>
    <div class="card custom-margin">
        <div class="container">
            <h2>Profesores</h2>
        </div>
        
        <DataTable :value="profesores" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem">
            <Column field="dni" header="DNI"></Column>
            <Column field="nombres" sortable header="Nombres"></Column>
            <Column field="apellido_paterno" sortable header="Apellido Paterno"></Column>
            <Column field="apellido_materno" sortable header="Apellido Materno"></Column>
            <Column field="fecha_nacimiento" sortable header="Fecha Nacimiento"></Column>
            <Column field="correo_institucional" sortable header="Email"></Column>
            <Column header="Editar">
                <template #body>
                    <Button label="Editar" severity="warning"></Button>
                </template>
            </Column>
            <Column header="Eliminar"> ¿
                <template #body>
                    <Button label="Eliminar" severity="danger"></Button>
                </template>
            </Column>
        </DataTable>
    </div>
</template>

<script>
    import axios from 'axios'
    import MenuCompAd from './MenuCompAd.vue';
    

    export default {
        components: {
            MenuCompAd
        }, data() {
        return {
            profesores: [],
            postURL: 'http://127.0.0.1:5000',
            config_request: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
        };
    },
    created() {
        axios.post(this.postURL + '/profesores')
            .then((res) => { this.profesores = res.data; })
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