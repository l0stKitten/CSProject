<template>
  <div class="card flex justify-content-center">
    <Button label="Agregar Matrícula" icon="pi pi-plus" severity="success" @click="visible = true" />
    <Dialog v-model:visible="visible" modal header="Agregar Matrícula" :style="{ width: '50vw' }">
      <form @submit.prevent="submitForm" >
        <div class="form-container">
          <div class="form-row">
            <label for="alumno">Alumno</label>
            <Dropdown v-model="alumno" editable :options="alumnos" optionLabel="name" placeholder="Selecciona un alumno" class="w-full md:w-14rem" />
          </div>

          <div class="form-row">
            <label for="curso">Curso</label>
            <Dropdown v-model="curso" editable :options="cursos" optionLabel="name" placeholder="Selecciona un curso" class="w-full md:w-14rem" />
          </div>
        </div>
        <div class="card flex justify-content-center">
          <div class="flex flex-wrap gap-3">
            <div class="flex items-center">
              <RadioButton v-model="estado" inputId="1" name="estado" value="Regular" />
              <label for="1" class="ml-2">Regular</label>
            </div>
            <div class="flex items-center">
              <RadioButton v-model="estado" inputId="0" name="estado" value="Abandono" />
              <label for="0" class="ml-2">Abandono</label>
            </div>
            <div class="flex items-center">
              <RadioButton v-model="estado" inputId="2" name="estado" value="Retiro" />
              <label for="2" class="ml-2">Retiro</label>
            </div>
          </div>
        </div>

        <div class="container">
          <Button label="Agregar" icon="pi pi-plus" type="submit" />
          <Button label="Cancelar" icon="pi pi-times" @click="visible = false" text />
        </div>
        
      </form>
    </Dialog>
  </div>
</template>

<script setup>
import { ref } from "vue";

const estado = ref('');
const visible = ref(false);
const formData = ref({
  pabellon: '',
  numero: ''

});

function submitForm() {
  // Handle form submission logic here
    console.log(formData.value);
    visible.value = false;
    resetForm();

}

function resetForm() {
  formData.value.pabellon = '';
  formData.value.numero = '';
  }
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