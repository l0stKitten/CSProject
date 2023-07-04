<template>
  <div class="card flex justify-content-center">
    <Button label="Agregar Justificación" icon="pi pi-plus" severity="success" @click="visible = true" />
    <Dialog v-model:visible="visible" modal header="Agregar Justificación" :style="{ width: '50vw' }">
      <form @submit.prevent="createJustificacion" class="form-container">
        <div class="form-row">
          <label for="asistencia">Asistencia</label>
          <InputText id="asistencia" v-model="formData.asistencia" required requiredMessage="Ingrese el código de asistencia" />
        </div>

        <div class="form-row">
          <label for="titulo">Titulo</label>
          <InputText id="titulo" v-model="formData.titulo" required requiredMessage="Ingrese un titulo" />
        </div>

        <div class="form-row">
          <label for="descripcion">Descripción</label>
          <InputText id="descripcion" v-model="formData.descripcion" required requiredMessage="Ingrese una descripción" />
        </div>

        <div class="form-row">
          <label for="archivo">Archivo</label>
          <FileUpload
            id="archivo"
            mode="basic"
            name="demo[]"
            url="/api/upload"
            accept="image/*"
            customUpload
            @uploader="customBase64Uploader"
          />
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
          justificaciones: [],
          newJustificacion: {},
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
        asistencia: '',
        titulo: '',
        descripcion: '',
        archivo: '',
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
          formData.value.numero = '';
          formData.value.pabellon = '';
        }
  
        return { visible, selectedType, selectedTypeValid, formData, submitForm, handleDropdownChange, resetForm };
      },
      methods: {
        createJustificacion() {
          var config_request = {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
          };
          axios
            .put(this.postURL + "/justificación", this.formData, { headers: config_request })
            .then(res => {
              this.justificaciones.push(res.data);
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
        const config = {
            headers: {
                'Authorization': `Bearer ${this.token}`,
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        };

        axios.post(this.postURL + '/justificaciones', null, config)
          .then((res) => { this.justificaciones = res.data; })
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