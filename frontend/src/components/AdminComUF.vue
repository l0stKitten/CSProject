<template>
  <div class="navbar">
    <MenuCompAd/>
  </div>
    
    <div class="card flex justify-content-center">
        <h2>Agregar Usuario</h2>
        <form @submit.prevent="submitForm" >
          <div class="form-container">
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
              <label for="correo_institucional">Email</label>
              <InputText id="correo_institucional" v-model="formData.correo_institucional" placeholder="usuario@email.com" required requiredMessage="Ingrese el email" type="email" />
            </div>

            <div class="form-row">
              <label for="password">Contraseña</label>
              <Password id="password" v-model="formData.password" toggleMask required />
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
              <label for="path">Foto</label>
              <FileUpload id="path" mode="basic" name="demo[]" url="/api/upload" accept="image/*" :auto="true" customUpload @uploader="customBase64Uploader" />
              <!--<label @change="updateFileName()"> {{ pathFileName }} </label>-->
            </div>
            
              <div class="form-row">
                <label for="tipo">Tipo</label>
                    <Dropdown v-model="selectedType" :options="tipos" optionLabel="name" placeholder="Selecciona un tipo" class="w-full md:w-14rem" @change="handleDropdownChange"/>
                    <div v-if="!selectedTypeValid" class="error-message">Por favor, selecciona un tipo.</div>
                  </div>

                    <div v-if="selected === 'Administrador'"> 
                        <div class="form-row">
                            <label for="cargo">Cargo</label>
                            <InputText id="cargo" v-model="formData.cargo"/>
                        </div>
                    </div>
                    <div v-else-if="selected === 'Profesor'"> 
                        <div class="form-row">
                            <label for="especialidad">Especialidad</label>
                            <InputText id="especialidad" v-model="formData.especialidad" />
                        </div>
                        
                    </div>
                    <div v-else> 
                        <div class="form-row">
                            <label for="al"></label>
                        </div>
                    </div>

            </div>
          
            <!--<Toast />
              <FileUpload name="demo[]" @upload="onAdvancedUpload($event)" :multiple="true" accept="image/*" :maxFileSize="1000000">
                  <template #empty>
                      <p>Arrastra y suelta los archivos aquí</p>
                  </template>
              </FileUpload>-->

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
  import { useToast } from "primevue/usetoast";

  let pathFileName = ref("");

  const visible = ref(false);
  const selectedType = ref('');
  const selectedTypeValid = ref(true);
  const postURL = 'http://127.0.0.1:5000';
  let route = '';
  let selected = '';

  const config_request = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*'
  };

  const formData = ref({
    dni: '',
    nombres: '',
    apellido_paterno: '',
    apellido_materno: '',
    fecha_nacimiento: '',
    correo_institucional: '',
    password: '',
    path: '',
    tipo: '',
    cargo: '',
    especialidad: ''

  });

  const tipos = ref([
    { name: 'Alumno', code: 'al' },
    { name: 'Profesor', code: 'pro' },
    { name: 'Administrador', code: 'ad' }
]);

  
  const toast = useToast();


  const customBase64Uploader = async (event) => {
        const file = event.files[0];
        
        const reader = new FileReader();
        let blob = await fetch(file.objectURL).then((r) => r.blob()); //blob:url

        reader.readAsDataURL(blob);
        

        reader.onloadend = function () {
            const base64data = reader.result;
        };

        pathFileName = file.name;
        formData.value.path = file.name;
    }

  
  function submitForm() {
    if (!selectedType.value) {
        selectedTypeValid.value = false; // Set validation state to false if no value is selected
    } else {
        selectedTypeValid.value = true;
        // Handle form submission logic here

        let newTask = {
          "dni": formData.value.dni,
          "nombres": formData.value.nombres,
          "apellido_paterno": formData.value.apellido_paterno,
          "apellido_materno": formData.value.apellido_materno,
          "fecha_nacimiento": formData.value.fecha_nacimiento,
          "correo_institucional": formData.value.correo_institucional,
          "password": formData.value.password,
          "path": formData.value.path,
          "tipo": formData.value.tipo,
          "cargo": formData.value.cargo,
          "especialidad": formData.value.especialidad,
        };

        console.log(newTask)
        axios.put(`${postURL}/persona`, newTask, config_request)
        .then((res) => {
          console.log(res.data);
        })
        .catch((error) => {
          console.log(error);
        });

        visible.value = false;
        resetForm();
    }
  }

  const handleDropdownChange = () =>  {
      selected = selectedType.value.name;
      selectedTypeValid.value = true;
      formData.value.tipo = selectedType.value.name;
      if (selectedType.value.name == 'Alumno'){
        route = '/alumnos'
      } else if (selectedType.value.name == 'Profesor'){
        route = '/profesores'
      } else if (selectedType.value.name == 'Administrador'){
        route = '/administradores'
      } else {
        route = '/admin'
      }
    }
  
  function resetForm() {
    formData.value.dni = '';
    formData.value.nombres = '';
    formData.value.apellido_paterno = '';
    formData.value.apellido_materno = '';
    formData.value.fecha_nacimiento = '';
    formData.value.correo_institucional = '';
    formData.value.password = '';
    formData.value.path = '';
    formData.value.cargo = '';
    formData.value.tipo = '';
    formData.value.especialidad = '';
    selectedType.value = '';
    }
    const usePathFileName = () => {
      return pathFileName;
    };
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
    margin-bottom: 40px;
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
        margin-top: 15px;
        margin-bottom: 80px;
    }
</style>