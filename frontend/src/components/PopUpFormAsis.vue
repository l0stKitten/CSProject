<template>
    <div class="card flex justify-content-center">
      <Button label="Agregar Asistencia" icon="pi pi-plus" severity="success" @click="visible = true" />
      <Dialog v-model:visible="visible" modal header="Agregar Asistencia" :style="{ width: '50vw' }">
        <form @submit.prevent="createAsistencia" class="form-container">
          <div class="form-row">
            <label for="dni">DNI Alumno</label>
            <InputText id="dni" v-model="formData.dni" required requiredMessage="Ingrese el DNI del alumno"/>
          </div>
  
          <div class="form-row">
            <label for="fecha_asistencia">Fecha asistencia</label>
            <div class="p-inputgroup flex-1">
                <span class="p-inputgroup-addon">
                    <i class="pi pi-calendar"></i>
                </span>
                <Calendar id="fecha_asistencia" v-model="formData.fecha_asistencia" touchUI required />
            </div>
            
          </div>
  
          <div class="form-row">
            <label for="matricula">Matricula</label>
            <InputText id="matricula" v-model="formData.matricula" required requiredMessage="Ingrese el codigo de matricula"/>
          </div>
  
          <div class="form-row">
            <label for="path">Foto</label>
            <FileUpload id="path" mode="basic" name="demo[]" url="/api/upload" accept="image/*" customUpload @uploader="customBase64Uploader" />
          </div>

          <div class="container">
            <Button label="Agregar" icon="pi pi-plus" type="submit" />
            <Button label="Cancelar" icon="pi pi-times" @click="visible = false" text />
          </div>
          
        </form>
      </Dialog>
    </div>
</template>

<script>
  import axios from 'axios';
  import { ref } from 'vue';

  export default {
    data() {
        return {
          asistencias: [],
          newAsistencia: {},
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
        fecha_asistencia: '',
        matricula: '',
        path: '',
      });
  const customBase64Uploader = async (event) => {
        const file = event.files[0];
        const reader = new FileReader();
        let blob = await fetch(file.objectURL).then((r) => r.blob()); //blob:url

        reader.readAsDataURL(blob);

        reader.onloadend = function () {
            const base64data = reader.result;
            this.formData.path = reader.result;
        };
    };
  
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
          formData.value.fecha_asistencia = '';
          formData.value.matricula = '';
          formData.value.path = '';
        }
  
        return { visible, selectedType, selectedTypeValid, formData, submitForm, handleDropdownChange, resetForm };
      },
      methods: {
        createAsistencia() {
          const config = {
                headers: {
                    'Authorization': `Bearer ${this.token}`,
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
            }
          axios
            .put(this.postURL + "/asistencia", this.formData, { headers: config.headers })
            .then(res => {
              this.asistencias.push(res.data);
              console.log(res.data);
            })
            .catch(error => {
              console.log(error);
            });

          this.visible = false;
          this.resetForm();
        },
      },
      created() {
        axios.post(this.postURL + '/asistencias')
          .then((res) => { this.asistencias = res.data; })
          .catch((error) => { console.log(error) })
      },
    };
</script>

<style scoped>
    .form-container {
    display: grid;
    grid-template-columns: repeat(2, 5fr); /* Adjust the number of columns as needed */
    gap: 2rem;
    }
    
    .form-row {
        display: grid;
        grid-column: span 1; /* Make the form-row span 2 columns */
    }

    label {
    display: block;
    margin-bottom: 0.5rem;
    }

    .container {
        display: flex;
        justify-content: space-between;
        margin-bottom: 10px;
    }
</style>