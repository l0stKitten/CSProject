<template>
    <div class="card flex justify-content-center">
      <Button label="Agregar Matricula" icon="pi pi-plus" severity="success" @click="visible = true" />
      <Dialog v-model:visible="visible" modal header="Agregar Matricula" :style="{ width: '50vw' }">
        <form @submit="createMatricula" class="form-container">
          <div class="form-row">
            <label for="alumno">DNI Alumno</label>
            <Dropdown v-model="selectedType" editable :options="alumnos" optionLabel="nombres" placeholder="Selecciona un alumno" class="w-full md:w-14rem" />
            <!--<InputText id="alumno" v-model="formData.alumno" required requiredMessage="Ingrese el DNI del alumno"/>-->
          </div>
  
          <div class="form-row">
            <label for="curso">Curso</label>
            <!--<Dropdown v-model="selectedType" editable :options="cursos" optionLabel="asig_nombre" placeholder="Selecciona un curso" class="w-full md:w-14rem"  />-->
            <InputText id="curso" v-model="formData.curso" required requiredMessage="Ingrese un curso" />
          </div>
  
          <div class="form-row">
            <label for="estado">Estado</label>
            <!--<Dropdown v-model="selectedType" editable :options="tipos" optionLabel="name" placeholder="Selecciona un estado" class="w-full md:w-14rem" />-->
            <InputText id="estado" v-model="formData.estado" required requiredMessage="Ingrese el estado"/>
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
    import axios from 'axios'
    import { ref } from "vue";
  
    export default {
      data() {
        return {
          alumnos: [],
          newMatricula: {},
          postURL: 'http://127.0.0.1:5000',
          config_request: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
          },
        };
      },
      setup() {
        const visible = ref(false);
        const selectedType = ref('');
        const selectedTypeValid = ref(true);
        let selected = '';

        const dataDropdown = ref({
          alumno: '',
          cursos: ''
        })
        const formData = ref({
          alumno: '',
          curso: '',
          estado: ''
        });

        const tipos = ref([
          { name: 'Regular', code: '1' },
          { name: 'Retirado', code: '2' },
          { name: 'Abandono', code: '0' }
      ]);

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
        
  
        function resetForm() {
          formData.value.alumno = '';
          formData.value.curso = '';
          formData.value.estado = '';
        }
  
        return { visible, selectedType, selectedTypeValid, formData, submitForm, resetForm };
      },
      methods: {
        createMatricula() {
          var config_request = {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
          };
          axios
            .put(this.postURL + "/matricula", this.formData, { headers: config_request })
            .then(res => {
              this.matriculas.push(res.data);
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
        axios.post(this.postURL + '/matriculas')
          .then((res) => { this.matriculas = res.data; })
          .catch((error) => { console.log(error) })

        axios.post(this.postURL + '/alumnos')
          .then((res) => { this.alumnos = res.data; })
          .catch((error) => { console.log(error) })
        
        axios.post(this.postURL + '/cursos')
          .then((res) => { this.cursos = res.data; })
          .catch((error) => { console.log(error) })
        
      },
    };
</script>

<style scoped>
    .form-container {
    display: grid;
    grid-template-columns: repeat(2, 5fr); 
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