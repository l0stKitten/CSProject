<template>
    <MenuCompAd/>
    <div class="card custom-margin">
        <div class="container">
            <h2>Cursos</h2>
        </div>
        
        <DataTable :value="cursos" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem">
            <Column field="codigo" header="Código"></Column>
            <Column field="asig_nombre" sortable header="Nombre"></Column>
            <Column field="profesor" sortable header="DNI Profesor"></Column>
            <Column field="fullname" sortable header="Profesor"></Column>
            <Column header="Horarios">
                <template #body>
                    <Button icon="pi pi-fw pi-calendar" severity="help"></Button>
                </template>
            </Column>
            <Column header="Editar">
                <template #body>
                    <Button icon="pi pi-fw pi-pencil" label="" severity="warning"></Button>
                </template>
            </Column>
            <Column header="Eliminar"> ¿
                <template #body="rowData">
                    <Button icon="pi pi-fw pi-trash" label="" severity="danger" @click="deleteCurso(rowData)"></Button>
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
            cursos: [],
            postURL: 'http://127.0.0.1:5000',
            config_request: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
        };
    },
    methods:{
            
        deleteCurso(curso){  
                    var config_request={
                        'Content-Type': 'application/json',
                        'Access-Control-Allow-Origin': '*'
                    }
                    axios.delete(this.postURL + '/curso', {data: {codigo: curso.data.codigo},  config_request })
                        .then(res => {                      
                            this.cursos.splice(this.cursos.indexOf(curso), 1);
                            console.log(res.data);
                        })
                        .catch((error) => {
                            console.log(error)
                        }); 
                }
        },
    created() {
        axios.post(this.postURL + '/cursos')
            .then((res) => { this.cursos = res.data; })
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