<template>
    <MenuCompAd/>
    <div class="card custom-margin">
        <div class="container">
            <h2>Alumnos</h2>
        </div>
        
        <DataTable :value="alumnos" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem">
            <Column field="dni" header="DNI"></Column>
            <Column field="nombres" sortable header="Nombres"></Column>
            <Column field="apellido_paterno" sortable header="Apellido Paterno"></Column>
            <Column field="apellido_materno" sortable header="Apellido Materno"></Column>
            <Column field="fecha_nacimiento" sortable header="Fecha Nacimiento">
                <template #body="rowData">
                    {{ formatDate(rowData.data.fecha_nacimiento) }}
                </template>
            </Column>
            <Column field="correo_institucional" sortable header="Email"></Column>
            <Column header="Editar">
                <template #body="rowData">
                    <Button icon="pi pi-fw pi-pencil" label="" severity="warning"></Button>
                </template>
            </Column>
            <Column header="Eliminar"> ¿
                <template #body="rowData">
                    <Button icon="pi pi-fw pi-trash" label="" severity="danger" @click="deleteAlumno(rowData)"></Button>
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
            alumnos: [],
            postURL: 'http://127.0.0.1:5000',
            token: localStorage.getItem('access_token')
        }
    },
    methods:{
            
            deleteAlumno(alumno){  
                const config = {
                    headers: {
                        'Authorization': `Bearer ${this.token}`,
                        'Content-Type': 'application/json',
                        'Access-Control-Allow-Origin': '*'
                    }
                }
                console.log(alumno.data.dni)
                axios.delete(this.postURL + '/alumno', {data: {dni: alumno.data.dni},  headers: config.headers })
                    .then(res => {                      
                        this.alumnos.splice(this.alumnos.indexOf(alumno), 1);
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

        axios.post(this.postURL + '/alumnos', null, config)
            .then((res) => { this.alumnos = res.data; })
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