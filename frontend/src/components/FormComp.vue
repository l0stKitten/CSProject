<template>
    <div class="card flex justify-content-center">
        <h2>Información Personal</h2>
        <form @submit.prevent="submitForm" class="form-container">
          <div class="form-row">
            <label for="dni">DNI</label>
            <InputText id="dni" v-model="formData.dni" required requiredMessage="Ingrese un DNI"/>
          </div>
  
          <div class="form-row">
            <label for="nombres">Nombres</label>
            <InputText id="nombres" v-model="formData.nombres" required requiredMessage="Ingrese un nombre" />
          </div>
  
          <div class="form-row">
            <label for="apellido_paterno">Apellido Paterno</label>
            <InputText id="apellido_paterno" v-model="formData.apellido_paterno" required requiredMessage="Ingrese el apellido paterno"/>
          </div>
  
          <div class="form-row">
            <label for="apellido_materno">Apellido Materno</label>
            <InputText id="apellido_materno" v-model="formData.apellido_materno" required requiredMessage="Ingrese el apellido materno"/>
          </div>
  
          <div class="form-row">
            <label for="fecha_nacimiento">Fecha Nacimiento</label>
            <div class="p-inputgroup flex-1">
                <span class="p-inputgroup-addon">
                    <i class="pi pi-calendar"></i>
                </span>
                <Calendar id="fecha_nacimiento" v-model="formData.fecha_nacimiento" touchUI required />
            </div>
            
          </div>
  
          <div class="form-row">
            <label for="email">Email</label>
            <InputText id="email" v-model="formData.email" placeholder="usuario@email.com" required requiredMessage="Ingrese el email" type="email" />
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
    </div>
</template>
  
<script setup>
  import { ref } from "vue";
  
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
    email: '',
    password: '',
    path: '',
    cargo: '',
    especialidad: ''

  });

  const formDat = ref ({
    password: '',
    password2: ''
  })

  const tipos = ref([
    { name: 'Alumno', code: 'al' },
    { name: 'Profesor', code: 'pro' },
    { name: 'Administrador', code: 'ad' }
]);

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

  const handleDropdownChange = () =>  {
      selected = selectedType.value.name
      selectedTypeValid.value = true;
    }
  
  function resetForm() {
    formData.value.dni = '';
    formData.value.nombres = '';
    formData.value.apellido_paterno = '';
    formData.value.apellido_materno = '';
    formData.value.fecha_nacimiento = '';
    formData.value.email = '';
    formData.value.password = '';
    formData.value.path = '';
    formData.value.cargo = '';
    formData.value.especialidad = '';
    selectedType.value = '';
    }
</script>

<style scoped>
    .form-container {
    display: grid;
    grid-template-columns: repeat(2, 5fr); /* Adjust the number of columns as needed */
    gap: 2rem;
    margin-bottom: 80px;
    }
    
    .form-row {
        display: grid;
        grid-column: span 1; /* Make the form-row span 2 columns */
    }

    label {
    display: block;
    margin-bottom: 0.5rem;
    }

    .card {
        margin-top: 50px;
    }

    .container {
        display: flex;
        justify-content: space-between;
        margin-bottom: 10px;
    }
</style>