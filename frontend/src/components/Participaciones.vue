<template>

    <DataTable :value="personas" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem">
        <Column field="nombres" sortable header="Nombre"></Column>
        <Column header="Cantidad">
          <template #body="rowData">
            <span>{{ getCantidad(rowData) }}</span>
          </template>
        </Column>
        <Column header="Acciones">
                  <template #body="rowData">
                    <Button
                      icon="pi pi-fw pi-minus"
                      @click="decrement(rowData)"
                      class="p-button-danger"
                    />
                    
                    <Button
                      icon="pi pi-fw pi-plus"
                      @click="increment(rowData)"
                      class="p-button-success"
                    />
                  </template>
            </Column>
    </DataTable>
    <Button
      @click="saveAll"
      icon="pi pi-fw pi-check"
      label="Guardar todo"
      class="p-button-success"
    />
  </template>
  
  <script>
  import axios from 'axios'
  import cu from './ProfCompPart';
  
  export default {
    props: {
        cu: {
        type: Object,
        required: true
        }
    },
    data() {
      return {
        personas: [],
        cantidades: [],
        postURL: 'http://127.0.0.1:5000',
        cur: 1,
        today: new Date()
      };
    },
    methods: {
      saveAll() {
      

      const saveRequests = this.personas.map(rowData => {
        var index = this.personas.findIndex(persona => persona === rowData);
        console.log(index)
        console.log(this.cantidades[index])
        const data = {
          asistencia: rowData.asistencia,
          cantidad: this.cantidades[index]
        };
        const token = localStorage.getItem('access_token');
        const config = {
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
          },
        };
        return axios.put(this.postURL + '/participacion', data, { headers: config.headers});
      });

      axios
        .all(saveRequests)
        .then(responseArr => {
          // Handle success response if needed
          responseArr.forEach(response => {
            console.log(response.data);
          });
        })
        .catch(error => {
          // Handle error response if needed
          console.log(error);
        });
    },
    increment(rowData) {
      var index = this.personas.findIndex(persona => persona === rowData);
      index += 1
      this.cantidades[index]++;
    },
    decrement(rowData) {
      var index = this.personas.findIndex(persona => persona === rowData);
      index += 1
      if (this.cantidades[index] > 0) {
        this.cantidades[index]--;
      }
    },
    getCantidad(rowData) {
      var index = this.personas.findIndex(persona => persona === rowData);
      index += 1
      console.log(index)
      console.log(this.cantidades)
      return this.cantidades[index];
    },
      currentDay() {
                const tod = new Date(); //comentar y usar this.today para conseguir que el usuario no pueda cambiar la fecha a su gusto
                var month = tod.getUTCMonth() + 1; //months from 1-12
                var day = tod.getUTCDate();
                var year = tod.getUTCFullYear();
                this.today = new Date(`${year}-${month}-${day}`)

                console.log(this.today)
            },
    }, created() {
      console.log(cu)
      const token = localStorage.getItem('access_token')
      const config = {
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        };

        const tod = new Date(); //comentar y usar this.today para conseguir que el usuario no pueda cambiar la fecha a su gusto
                var month = tod.getUTCMonth() + 1; //months from 1-12
                var day = tod.getUTCDate();
                var year = tod.getUTCFullYear();
                this.today = new Date(`${year}-${month}-${day}`)

                console.log(this.today)
        const dat = { codigo: 1, fecha: this.today}
        //Creamos la fecha
        axios.post(this.postURL + '/alumnoscurso', dat, config)
            .then((res) => { 
              this.personas = res.data; 
              this.cantidades = Array.from({ length: this.personas.length }, () => 0);})
            .catch((error) => { console.log(error) })

        axios.get('http://worldtimeapi.org/api/timezone/America/Lima')
                .then(response => {
                    const { datetime } = response.data;
                    const currentTime = new Date(datetime);
                    var month = currentTime.getUTCMonth() + 1; //months from 1-12
                    var day = currentTime.getUTCDate();
                    var year = currentTime.getUTCFullYear();
                    this.today = new Date(`${year}-${month}-${day}`)
                    // Use the current date and time in your application
                    console.log(currentTime);
                    console.log(this.today)
                })
                .catch(error => {
                    console.error('Error fetching current date and time:', error);
                });

    }
  };
  </script>