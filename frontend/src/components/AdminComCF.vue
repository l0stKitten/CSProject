<template>
  <div class="navbar">
    <MenuCompAd/>
  </div>

  <div class="card flex justify-content-center">
        <h2>Agregar Curso</h2>
        <form @submit.prevent="submitForm" class="form-container">
          <div class="form-row">
            <label for="asignatura">Asignatura</label>
            <Dropdown v-model="selectedAsig" editable :options="asignaturas" optionLabel="nombre" placeholder="Selecciona una asignatura" class="w-full md:w-14rem" />
          </div>
  
          <div class="form-row">
            <label for="nombres">Profesor</label>
            <Dropdown v-model="selectedProf" editable :options="profesores" optionLabel="fullname" placeholder="Selecciona un profesor" class="w-full md:w-14rem" />
          </div>
  
          <div class="form-row">
            <label for="ini_hora">Horarios</label>
            <Dropdown v-model="selectedHor" editable :options="horarios" optionLabel="fullhorario" placeholder="Selecciona un horario" class="w-full md:w-14rem" />
          </div>

          <div class="container">
            <Button label="Agregar" icon="pi pi-plus" type="submit" />
            <router-link to="/admin">
                <Button label="Cancelar" icon="pi pi-times" @click="visible = false" text />
            </router-link>
            
          </div>
          
        </form>
    </div>
    
    <div class="card flex justify-content-center">
        <h2>Agregar Asignatura</h2>
        <form @submit.prevent="submitFormA" class="form-container">
          <div class="form-row">
            <label for="asignatura">Asignatura</label>
            <InputText type="text" v-model="asignatura" />
          </div>

          <div class="form-row">
            <label for="semestre">Semestre</label>
            <InputText type="text" v-model="semestre" />
          </div>
  
          <div class="form-row">
            <label for="carrera">Carrera</label>
            <InputText type="text" v-model="carrera" />
          </div>

          <div class="container">
            <Button label="Agregar" icon="pi pi-plus" type="submit" />
            <router-link to="/admin">
                <Button label="Cancelar" icon="pi pi-times" @click="visible = false" text />
            </router-link>
            
          </div>
          
        </form>
    </div>

    <div class="card flex justify-content-center">
        <h2>Agregar Horario</h2>
        <form @submit.prevent="submitFormH" class="form-container">  
          <div class="form-row">
            <label for="ini_hora">Horario Dia</label>
            <InputText type="text" v-model="dia" />
          </div>

          <div class="form-row">
            <label for="fin_hora">Horario Inicio</label>
            <Calendar id="calendar-timeonly" v-model="time" timeOnly dateFormat="hh/mm" />
          </div>

          <div class="form-row">
            <label for="ini_hora">Horario Fin</label>
            <Calendar id="calendar-timeonly" v-model="time2" timeOnly dateFormat="hh/mm"/>
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
  import { onMounted } from 'vue';

  const profesores = ref([])
  const salones = ref([])
  const asignaturas = ref([])
  const horarios = ref([])
  const asig = ref([])
  const hor = ref([])
  const cur = ref([])

  const time = ref();
  const time2 = ref();

  const selectedProf = ref();
  const selectedSalon = ref();
  const selectedHor = ref();
  const selectedAsig =  ref();

  const visible = ref(false);
  const selectedType = ref('');
  const selectedTypeValid = ref(true);
  let route = '';
  let selected = '';

  const ti1 = ref();
  const ti2 = ref();

  const asignatura = ref()
  const carrera = ref()
  const semestre = ref()
  const dia = ref()

  const formData = ref({
    asignatura: '',
    semestre: '',
    profesor: '',
    dia: '',
    ini_hora: '',
    fin_hora: '',
    salon: '',
  });

  const newTask = ref({});
  const postURL = 'http://127.0.0.1:5000';
  const token = localStorage.getItem('access_token');
  const config_request = {
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
    }
  };

  const tipos = ref([
    { name: 'Alumno', code: 'al' },
    { name: 'Profesor', code: 'pro' },
    { name: 'Administrador', code: 'ad' }
]);

  function convertTime() {
    const currentDate = new Date(time.value);

    const currentHour = currentDate.getHours();
    const currentMinute = currentDate.getMinutes();

    ti1.value = `${currentHour}:${currentMinute}`;

    const currentDate2 = new Date(time2.value);

    const currentHour2 = currentDate2.getHours();
    const currentMinute2 = currentDate2.getMinutes();

    ti2.value = `${currentHour2}:${currentMinute2}`;
  }

  const submitFormH = (event) => {

    convertTime()

    let newHora = {
          "dia": dia.value,
          "hora_inicio": ti1.value,
          "hora_fin": ti2.value,
    }

    axios.put(`${postURL}/horario`, newHora, config_request)
        .then((res) => {
          hor.value = res.data;
          console.log(res.data);
        })
        .catch((error) => {
          console.log(error);
        });

        console.log(hor.value)
    
    getHorarios();
  };
  
  const submitFormA = (event) => {

    let newAsig = {
          "nombre": asignatura.value,
          "semestre": semestre.value,
          "carrera": carrera.value
    };

    console.log(newAsig)

    axios.put(`${postURL}/asignatura`, newAsig, config_request)
        .then((res) => {
          asig.value = res.data;
          console.log(res.data);
        })
        .catch((error) => {
          console.log(error);
        });

        console.log(asig.value)
    
    getAsignaturas();

  };

  const submitForm = (event) => {
    let newCur = {
      "asignatura": selectedAsig.value.codigo,
      "profesor": selectedProf.value.dni,
      "horario": selectedHor.value.codigo
    }

    axios.put(`${postURL}/curso`, newCur, config_request)
        .then((res) => {
          cur.value = res.data;
          console.log(res.data);
        })
        .catch((error) => {
          console.log(error);
        });
        console.log(cur.value)

  };

  const getProfesores = async () => {
    axios.post(`${postURL}/profesores`, null, config_request)
            .then((res) => { profesores.value = res.data; })
            .catch((error) => { console.log(error) })
  };

  const getAsignaturas = async () => {
    axios.post(`${postURL}/asignaturas`, null, config_request)
            .then((res) => { asignaturas.value = res.data; })
            .catch((error) => { console.log(error) })
  };

  const getHorarios = async () => {
    axios.post(`${postURL}/horarios`, null, config_request)
            .then((res) => { horarios.value = res.data; })
            .catch((error) => { console.log(error) })
  };


  onMounted(() => {
    getProfesores();
    getAsignaturas();
    getHorarios();
  });


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
    formData.value.asignatura = '';
    formData.value.semestre = '';
    formData.value.profesor = '';
    formData.value.ini_hora = '';
    formData.value.fin_hora = '';
    formData.value.salon = '';
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