<template>
    <div class="card flex justify-content-center">
      <Button label="Agregar Salon" icon="pi pi-plus" severity="success" @click="visible = true" />
      <Dialog v-model:visible="visible" modal header="Agregar Salon" :style="{ width: '50vw' }">
        <form @submit="createSalon" class="form-container">
  
          <div class="form-row">
            <label for="numero">Numero</label>
            <InputText id="numero" v-model="formData.numero" required requiredMessage="Ingrese un número de aula" />
          </div>
  
          <div class="form-row">
            <label for="pabellon">Pabellon</label>
            <InputText id="pabellon" v-model="formData.pabellon" required requiredMessage="Ingrese un pabellon"/>
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
          salones: [],
          newSalon: {},
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
          numero: '',
          pabellon: ''
        });

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
        createSalon() {
          const config = {
                headers: {
                    'Authorization': `Bearer ${this.token}`,
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
            }
          axios
            .put(this.postURL + "/salon", this.formData, { headers: config.headers })
            .then(res => {
              this.salones.push(res.data);
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

        axios.post(this.postURL + '/salones', null, config)
          .then((res) => { this.salones = res.data; })
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