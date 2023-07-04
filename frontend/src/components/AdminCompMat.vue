<template>
    <MenuCompAd/>
    <div class="card custom-margin">
        <div class="container">
            <h2>Matrículas</h2>
            <div class="right-align">
                <PopUpFormMat/>
            </div>
        </div>
        
        <DataTable :value="matriculas" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem">
            <Column field="fullname" sortable header="Alumno"></Column>
            <Column field="asig_nombre" sortable header="Curso"></Column>
            <Column field="estado" sortable header="Estado"></Column>
            <Column header="Editar">
                <template #body>
                    <Button icon="pi pi-fw pi-pencil" label="" severity="warning"></Button>
                </template>
            </Column>
            <Column header="Eliminar"> ¿
                <template #body="rowData">
                    <Button icon="pi pi-fw pi-trash" label="" severity="danger" @click="deleteMatricula(rowData)"></Button>
                </template>
            </Column>
        </DataTable>
    </div>
</template>

<script>
    import axios from 'axios'
    import PopUpFormMat from './PopUpFormMat.vue';
    import MenuCompAd from './MenuCompAd.vue';

    export default {
        data() {
        return {
            matriculas: [],
            postURL: 'http://127.0.0.1:5000',
            token: localStorage.getItem('access_token')
        };
    },
    methods:{
            
            deleteMatricula(matricula){  
                const config = {
                    headers: {
                        'Authorization': `Bearer ${this.token}`,
                        'Content-Type': 'application/json',
                        'Access-Control-Allow-Origin': '*'
                    }
                }
                axios.delete(this.postURL + '/matricula', {data: {codigo: matricula.data.codigo}, headers: config.headers})
                    .then(res => {                      
                        this.matriculas.splice(this.matriculas.indexOf(matricula), 1);
                        console.log(res.data);
                    })
                    .catch((error) => {
                        console.log(error)
                    }); 
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

        axios.post(this.postURL + '/matriculas', null, config)
            .then((res) => { this.matriculas = res.data; })
            .catch((error) => { console.log(error) })
    },
    components: { PopUpFormMat, MenuCompAd }
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

    .right-align {
        display: flex;
        justify-content: flex-end;
    }
</style>