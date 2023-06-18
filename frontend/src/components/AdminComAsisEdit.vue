<template>
    <div class="navbar">
      <MenuCompAd/>
    </div>
      
      <div class="card flex justify-content-center">
          <h2>Editar Justificación</h2>
          <form @submit.prevent="submitForm" class="form-container">
            <div class="form-row">
              <label for="asignatura">Título</label>
              <Dropdown v-model="asignatura" editable :options="asignaturas" optionLabel="name" placeholder="Selecciona un asignatura" class="w-full md:w-14rem" />
            </div>
    
            <div class="form-row">
              <label for="nombres">Estudiante</label>
              <Dropdown v-model="profesor" editable :options="profesores" optionLabel="name" placeholder="Selecciona un profesor" class="w-full md:w-14rem" />
            </div>
    
            <div class="form-row">
              <label for="horario">Observaciones</label>
              <Dropdown v-model="horario" editable :options="horarios" optionLabel="name" placeholder="Selecciona un horario" class="w-full md:w-14rem" />
            </div>
    
            <div class="form-row">
              <label for="salon">Salon</label>
              <Dropdown v-model="salon" editable :options="salones" optionLabel="name" placeholder="Selecciona un salón" class="w-full md:w-14rem" />
            </div>
  
            <div class="container">
              <Button label="Agregar" icon="pi pi-plus" type="submit" />
              <router-link to="/admin">
                  <Button label="Cancelar" icon="pi pi-times" @click="visible = false" text />
              </router-link>
              
            </div>
            
          </form>
      </div>
</template>
    
<script setup>
    import { ref } from "vue";
    import axios from 'axios'
  
    const visible = ref(false);
    const selectedType = ref('');
    const selectedTypeValid = ref(true);
    let route = '';
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
  
    const newTask = ref({});
    const postURL = 'http://127.0.0.1:5000';
    const config_request = {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    };
  
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
    
    const submitForm = (event) => {
      if (!selectedType.value) {
        selectedTypeValid.value = false;
      } else {
        selectedTypeValid.value = true;
  
        console.log(formData.value);
        visible.value = false;
        resetForm();
      }
    };
  
    const handleDropdownChange = () =>  {
        selected = selectedType.value.name;
        selectedTypeValid.value = true;
        if (selectedType.value.name == 'Alumno'){
          route = 'alumnos'
        } else if (selectedType.value.name == 'Profesor'){
          route = 'profesores'
        } else if (selectedType.value.name == 'Administrador'){
          route = 'administradores'
        } else {
          route = 'admin'
        }
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
  
  <script>
      import MenuCompAd from './MenuCompAd.vue';
  
      export default {
        
          components: {
              MenuCompAd
          }
      }
  </script>
  
  <style scoped>
      .form-container {
      display: grid;
      grid-template-columns: repeat(2, 5fr); /* Adjust the number of columns as needed */
      gap: 2rem;
      margin-bottom: 80px;
      }
  
      h2 {
        margin-top: 40px;
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