<template>
    <MenuCompAd/>
    <div class="card custom-margin">
        <div class="container">
            <h2>Administradores</h2>
        </div>
        
        <DataTable :value="administradores" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem">
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
                <template #body>
                    <Button icon="pi pi-fw pi-pencil" label="" severity="warning"></Button>
                </template>
            </Column>
            <Column header="Eliminar">
                <template #body="rowData">
                <Button icon="pi pi-fw pi-pencil" label="" severity="warning" @click="agregarInput(rowData); visible = true"></Button>
                <Dialog v-model:visible="visible" modal header="Editar Administrador" :style="{ width: '50vw' }">
                <form @submit="updateAdministrador" class="form-container">
                    <div class="form-row">
                    <label for="nombres">Nombres</label>
                    <InputText id="nombres" v-model="actualizarAdministrador.nombres" required requiredMessage="Ingrese los nombres"/>
                    </div>
                    <div class="form-row">
                    <label for="apellido_paterno">Apellido Paterno</label>
                    <InputText id="apellido_paterno" v-model="actualizarAdministrador.apellido_paterno" required requiredMessage="Ingrese un apellido paterno" />
                    </div>
                    <div class="form-row">
                    <label for="apellido_materno">Apellido Materno</label>
                    <InputText id="apellido_materno" v-model="actualizarAdministrador.apellido_materno" required requiredMessage="Ingrese un Apellido materno" />
                    </div>
                    <div class="form-row">
                    <label for="fecha_nacimiento">Fecha Nacimiento</label>
                    <InputText id="fecha_nacimiento" v-model="actualizarAdministrador.fecha_nacimiento" required requiredMessage="Ingrese una fecha nacimiento" />
                    </div>
    
                    <div class="form-row">
                    <label for="correo_institucional">Correo Institucional</label>
                    <InputText id="correo_institucional" v-model="actualizarAdministrador.correo_institucional" required requiredMessage="Ingrese un correo institucional"/>
                    </div>
                    <div class="container">
                    <Button label="Actualizar" icon="pi pi-check" type="submit" />
                    <Button label="Cancelar" icon="pi pi-times" @click="visible = false" text />
                    </div>
                </form>
                </Dialog>
            </template>
            </Column>
            <Column header="Eliminar">
                <template #body="rowData">
                    <Button icon="pi pi-fw pi-trash" label="" severity="danger" @click="deleteAdministrador(rowData)"></Button>
                </template>
            </Column>
        </DataTable>
    </div>
</template>

<script>
    import axios from 'axios'
    import MenuCompAd from './MenuCompAd.vue';
    import { ref } from "vue";

    export default {
    data() {
        return {
        administradores: [],
        actualizarAdministrador: {},
        postURL: 'http://127.0.0.1:5000',
        token: localStorage.getItem('access_token')
        };
    },
    setup() {
        const visible = ref(false);
        const selectedType = ref('');
        const selectedTypeValid = ref(true);
        let selected = '';
        const formData = ref({
            dni: '',
            nombres: '',
            apellido_paterno: '',
            apellido_materno: '',
            fecha_nacimiento: '',
            correo_institucional: ''
        });

        function submitForm() {
            if (!selectedType.value) {
                selectedTypeValid.value = false; // Set validation state to false if no value is selected
            } else {
                selectedTypeValid.value = true;
                // Handle form submission logic here
                console.log(formData.value);
                visible.value = false;
                resetForm();
            }
        }

        const handleDropdownChange = () => {
        selected = selectedType.value.name
        selectedTypeValid.value = true;
        }

        function resetForm() {
            formData.value.dni = '';
            formData.value.nombres = '';
            formData.value.apellido_paterno = '';
            formData.value.apellido_materno = '';
            formData.value.fecha_nacimiento = '';
            formData.value.correo_institucional = '';
        }

        return { visible, selectedType, selectedTypeValid, formData, submitForm, handleDropdownChange, resetForm };
    },
    methods: {
        agregarInput(administrador) {
        this.actualizarAdministrador = {
            dni: administrador.data.dni,
            nombres: administrador.data.nombres,
            apellido_paterno: administrador.data.apellido_paterno,
            apellido_materno: administrador.data.apellido_materno,
            fecha_nacimiento: administrador.data.fecha_nacimiento,
            correo_institucional: administrador.data.correo_institucional,
        };
        },
        updateAdministrador(e) {
            //e.preventDefault();
            var config_request = {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            };

            axios
                .patch(this.postURL + '/administrador', this.actualizarAdministrador, { config_request })
                .then(res => {
                const index = this.administradores.findIndex(administrador => administrador.dni === this.actualizarAdministrador.dni);
                if (index !== -1) {
                    this.administradores[index] = this.actualizarAdministrador;
                }
                console.log(res.data);
                })
                .catch(error => {
                console.log(error);
                });

            this.actualizarAdministrador = {};
            this.visible = false;
        },
        deleteAdmin(administrador){  
            const config = {
                headers: {
                'Authorization': `Bearer ${this.token}`,
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
                }
            };

                    axios.delete(this.postURL + '/administrador', {data: {dni: administrador.data.dni}, headers: config.headers })
                        .then(res => {                      
                            this.administradores.splice(this.administradores.indexOf(administrador), 1);
                            console.log(res.data);
                        })
                        .catch((error) => {
                            console.log(error)
                        }); 
                }
    },
    created() {
        const token = localStorage.getItem('access_token');
        const config = {
            headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
            }
        };
        axios.post(this.postURL + '/administradores', null, config)
            .then((res) => { this.administradores = res.data; })
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
    components: {MenuCompAd}
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
