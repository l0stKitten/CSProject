<template>
    <div class="card flex justify-content-center">
        <h2>Cambiar Contraseña</h2>
        <form @submit.prevent="submitForm" class="form-container">
          <div class="form-row">
            <label for="dni">DNI</label>
            <InputText id="dni" v-model="formDat.dni" required requiredMessage="Ingrese un DNI"/>
          </div>

          <div class="form-row">
            <label for="password">Contraseña</label>
            <Password id="password" v-model="formDat.password" toggleMask required />
          </div>

          <div class="form-row">
            <label for="password">Validar Contraseña</label>
            <Password id="password" v-model="formDat.password2" toggleMask required />
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

  const formDat = ref ({
    dni: '',
    password: '',
    password2: ''
  })

  const tipos = ref([
    { name: 'Alumno', code: 'al' },
    { name: 'Profesor', code: 'pro' },
    { name: 'Administrador', code: 'ad' }
]);

  
  function submitForm() {
    // Handle form submission logic here
        console.log(formDat.value);
        visible.value = false;
        resetForm();
  
  }

  
  function resetForm() {
    formDat.value.dni = '',
    formDat.value.password = '';
    formDat.value.password2 = '';
    }
</script>

<style scoped>
    .form-container {
    display: grid;
    grid-template-columns: repeat(1, 3fr); /* Adjust the number of columns as needed */
    gap: 2rem;
    margin-bottom: 80px;
    align-content: center;
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