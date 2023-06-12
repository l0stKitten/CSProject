<template>
    <div class="card flex justify-content-center">
      <Button label="Agregar Salón" icon="pi pi-plus" severity="success" @click="visible = true" />
      <Dialog v-model:visible="visible" modal header="Agregar Salón" :style="{ width: '50vw' }">
        <form @submit.prevent="submitForm" class="form-container">
          <div class="form-row">
            <label for="pabellon">Pabellón</label>
            <InputText id="pabellon" v-model="formData.pabellon" placeholder="A" required requiredMessage="Ingrese un pabellón"/>
          </div>
  
          <div class="form-row">
            <label for="numero">Número de Salón</label>
            <InputText id="numero" v-model="formData.numero" placeholder="1" required requiredMessage="Ingrese un nombre" />
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