<template>
    <MenuCompAd/>
    <div class="card custom-margin">
        <div class="container">
            <h2>Asistencias</h2>
        </div>
        
        <DataTable :value="asistencias" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem">
            <Column field="nombre" header="Curso"></Column>
            <Column field="full_name" sortable header="Alumno"></Column>
            <Column field="fecha_asistencia" sortable header="Fecha Asistencia">
                <template #body="rowData">
                    {{ formatDate(rowData.data.fecha_asistencia) }}
                </template>
            </Column>
            <Column field="estado" header="Estado" dataType="boolean" bodyClass="text-center" style="min-width: 8rem">
                <template #body="{ data }">
                    <i class="pi" :class="{ 'pi-check-circle text-green-500 ': data.estado, 'pi-times-circle text-red-500': !data.estado }"></i>
                </template>
                <template #filter="{ filterModel }">
                    <label for="estado-filter" class="font-bold"> Asistió </label>
                    <TriStateCheckbox v-model="filterModel.value" inputId="estado-filter" />
                </template>
            </Column>
            <Column header="Editar">
                <template #body>
                    <Button icon="pi pi-fw pi-pencil" label="" severity="warning"></Button>
                </template>
            </Column>
            <Column header="Eliminar"> ¿
                <template #body="rowData">
                    <Button icon="pi pi-fw pi-trash" label="" severity="danger" @click="deleteAsistencia(rowData)"></Button>
                </template>
            </Column>
        </DataTable>
    </div>
</template>

<script>
    import axios from 'axios'
    import PopUpFormAsis from './PopUpFormAsis.vue';
    import MenuCompAd from './MenuCompAd.vue';

    export default {
        data() {
        return {
            asistencias: [],
            postURL: 'http://127.0.0.1:5000',
            token: localStorage.getItem('access_token')
        };
    },
    methods:{
            
        deleteAsistencia(asistencia){  
            const config = {
                headers: {
                    'Authorization': `Bearer ${this.token}`,
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
            }

                axios.delete(this.postURL + '/asistencia', {data: {codigo: asistencia.data.codigo},  headers: config.headers })
                    .then(res => {                      
                        this.asistencias.splice(this.asistencias.indexOf(asistencia), 1);
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

        axios.post(this.postURL + '/asistencias', null, config)
            .then((res) => { this.asistencias = res.data; })
            .catch((error) => { console.log(error) })
    }, computed: {
        formatDate() {
        return (dateString) => {
            const date = new Date(dateString);
            const day = date.getDate().toString().padStart(2, "0");
            const month = (date.getMonth() + 1).toString().padStart(2, "0");
            const year = date.getFullYear();
            return `${day}/${month}/${year}`;
        };
        },
    },
    components: { PopUpFormAsis, MenuCompAd }
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