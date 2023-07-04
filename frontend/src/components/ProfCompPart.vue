<template>
    <MenuCompPro/>
    <div class="card custom-margin">
        <div class="container">
            <h2>Participaciones</h2>
        </div>
    </div>

    <div class="card-grid">
        
      <Card v-for="cu in cursosuser" :key="cu.codigo" style="width: 25em">
        <template #title>{{ cu.asig_nombre }}</template>
        <template #subtitle>{{ cu.fullname }}</template>
        <template #content>
          <p> Horario:  {{  cu.hora_inicio }} - {{ cu.hora_fin}} | {{ cu.dia}} </p>

            <Button @click="visible = true" icon="pi pi-check-circle" severity="warning" label="Añadir Participaciones" />
            <Dialog v-model:visible="visible" modal header="Agregar Participaciones" :style="{ width: '50vw' }">
                <Participaciones :cu="cu.codigo"/>
            </Dialog>
        </template>
      </Card>
    </div>
</template>

<script>
    import axios from 'axios'
    import MenuCompPro from './MenuCompPro.vue';
    import Participaciones from './Participaciones.vue';
    import { ref } from "vue";

    export default {

        components: {
            MenuCompPro,
            Participaciones
        }, data() {
            return {
                visible: false,
                today: new Date(),
                cursosuser: [],
                postURL: 'http://127.0.0.1:5000',
                token: localStorage.getItem('access_token')
            }
        },
        methods: {
            
        },
        created() {
            const token = localStorage.getItem('access_token')
            const config = {
                headers: {
                    'Authorization': `Bearer ${token}`,
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
            };

            axios.post(this.postURL + '/cursosprof', {dni: localStorage.getItem('dni')}, config )
            
                .then((res) => { this.cursosuser = res.data; })
                .catch((error) => { console.log(error) })
            
            axios.get('http://worldtimeapi.org/api/timezone/America/Lima')
                .then(response => {
                    const { datetime } = response.data;
                    const currentTime = new Date(datetime);
                    this.today = currentTime
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

<style scoped>
    .custom-margin {
        margin-top: 50px;
    }
    .container {
        display: flex;
        justify-content: space-between;
        margin-bottom: 10px;
    }

    .container h2 {
        margin: 0;
    }

    .card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    grid-gap: 1rem;
    margin-top: 40px;
    }
  
  video {
    width: 100%;
  }

  

    @media (max-width: 767px) {
        .camera-container {
        flex-direction: column;
        }
    }

</style>