<template>
    <MenuCompAd/>
    <div class="card custom-margin">
        <div class="container">
            <h2>Salones</h2>
            <div class="right-align">
                <PopUpFormSal/>
            </div>
        </div>
        
        <DataTable :value="salones" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem">
            <Column field="codigo" header="Código"></Column>
            <Column field="pabellon" sortable header="Pabellón"></Column>
            <Column field="numero" sortable header="Número"></Column>
            
            <Column header="Editar">
                <template #body="rowData">
                    <Button icon="pi pi-fw pi-pencil" label="" severity="warning" @click="agregarInput(rowData); visible = true"></Button>
                    <Dialog v-model:visible="visible" modal header="Editar Salon" :style="{ width: '50vw' }">
                    <form @submit="updateSalon" >
                        <div class="form-container">
                            <!--<div class="form-row">
                            <label for="codigo">Codigo</label>
                            <InputText id="codigo" v-model="actualizarSalon.codigo" required requiredMessage="Ingrese un codigo"/>
                            </div>-->
            
                            <div class="form-row">
                            <label for="numero">Numero</label>
                            <InputText id="numero" v-model="actualizarSalon.numero" required requiredMessage="Ingrese un número de aula" />
                            </div>
            
                            <div class="form-row">
                            <label for="pabellon">Pabellon</label>
                            <InputText id="pabellon" v-model="actualizarSalon.pabellon" required requiredMessage="Ingrese un pabellon"/>
                            </div>
                        </div>
                        
                        <div class="container">
                            <Button label="Actualizar" icon="pi pi-check" type="submit" />
                            <Button label="Cancelar" icon="pi pi-times" @click="visible = false" text />
                        </div>
                        
                        
                    </form>
                    </Dialog>
                </template>
            </Column>
                
            <Column header="Eliminar"> ¿
                <template #body="rowData">
                    <Button icon="pi pi-fw pi-trash" label="" severity="danger" @click="deleteSalon(rowData)"></Button>
                </template>
            </Column>
        </DataTable>
    </div>
</template>

<script>
    import axios from 'axios'
    import PopUpFormSal from './PopUpFormSal.vue';
    import MenuCompAd from './MenuCompAd.vue';
    import { ref } from "vue";

    export default {
        data() {
          return {
            salones: [],
            postURL: 'http://127.0.0.1:5000',
            token: localStorage.getItem('access_token'),
          };
    },
    setup() {
        const visible = ref(false);
        const selectedType = ref('');
        const selectedTypeValid = ref(true);
        let selected = '';
        const formData = ref({
          codigo: '',
          numero: '',
          pabellon: ''
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
          formData.value.codigo = '';
          formData.value.numero = '';
          formData.value.pabellon = '';
        }
  
        return { visible, selectedType, selectedTypeValid, formData, submitForm, handleDropdownChange, resetForm };
      },
    methods:{
        agregarInput(salon) {
          this.actualizarSalon = {
            codigo: salon.data.codigo,
            numero: salon.data.numero,
            pabellon: salon.data.pabellon,
          };
        },
        updateSalon(e) {
          //e.preventDefault();
          const config = {
                headers: {
                    'Authorization': `Bearer ${this.token}`,
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
            }
  
          axios
            .patch(this.postURL + '/salon', this.actualizarSalon, { headers: config.headers })
            .then(res => {
              const index = this.salones.findIndex(salon => salon.codigo === this.actualizarSalon.codigo);
              if (index !== -1) {
                this.salones[index] = this.actualizarSalon;
              }
              console.log(res.data);
            })
            .catch(error => {
              console.log(error);
            });
  
          this.actualizarSalon = {};
          this.visible = false;
        },
        deleteSalon(salon){  
          const config = {
                headers: {
                    'Authorization': `Bearer ${this.token}`,
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
            }
                    axios.delete(this.postURL + '/salon', {data: {codigo: salon.data.codigo},  headers: config.headers })
                        .then(res => {                      
                            this.salones.splice(this.salones.indexOf(salon), 1);
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

        axios.post(this.postURL + '/salones', null, config )
            .then((res) => { this.salones = res.data; })
            .catch((error) => { console.log(error) })
    },
    components: { PopUpFormSal, MenuCompAd }
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

    .form-container {
    display: grid;
    grid-template-columns: repeat(2, 5fr); /* Adjust the number of columns as needed */
    gap: 2rem;
    margin-bottom: 30px;
    }
    
    .form-row {
        display: grid;
        grid-column: span 1; /* Make the form-row span 2 columns */
    }


    .container {
        display: flex;
        justify-content: space-between;
        margin-bottom: 10px;
    }
</style>