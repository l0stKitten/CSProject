<template>
    <MenuCompAl/>
    <div class="card custom-margin">
        <div class="container">
            <h2>Asistencias</h2>
        </div>
    </div>

    <div class="card-grid">
        
      <Card v-for="cu in cursosuser" :key="cu.codigo" style="width: 25em">
        <template #title>{{ cu.asig_nombre }}</template>
        <template #subtitle>{{ cu.fullname }}</template>
        <template #content>
          <p> Horario:  {{  cu.hora_inicio }} - {{ cu.hora_fin}} | {{ cu.dia}} </p>
        </template>
        <template #footer>
            <Button v-if="isButtonVisible(cu) && noasis" @click="visible = true" icon="pi pi-check-circle" severity="warning" label="Marcar Asistencia" />
            <Dialog v-model:visible="visible" modal header="Agregar Foto" :style="{ width: '50vw' }">
                <WebCam :cu="cu"/>
            </Dialog>
        </template>
      </Card>
    </div>
</template>

<script>
    import axios from 'axios'
    import MenuCompAl from './MenuCompAl.vue';
    import WebCam from './WebCam.vue';
    import { ref } from "vue";

    export default {

        components: {
            MenuCompAl,
            WebCam
        }, data() {
            return {
                noasis: true,
                visible: false,
                visible_video: false,
                today: new Date(),
                showWebcamModal: false,
                cursosuser: [],
                postURL: 'http://127.0.0.1:5000',
                config_request: {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                photo: null,
                stream: null,
            }
        },
        methods: {
            openModal() {
                this.showWebcamModal = true;
            },
            currentDay() {
                const today = new Date(); //comentar y usar this.today para conseguir que el usuario no pueda cambiar la fecha a su gusto
                const options = { weekday: 'long' };
                const today_day = today.toLocaleDateString('en-US', options);
                console.log(today_day)
                var dia = ""
                if (today_day == "Monday"){
                    dia = "L"
                } else if (today_day == "Tuesday"){
                    dia = "M"
                } else if (today_day == "Wednesday"){
                    dia = "X"
                } else if (today_day == "Thursday"){
                    dia = "J"
                } else if (today_day == "Friday"){
                    dia = "V"
                } else if (today_day == "Saturday"){
                    dia = "S"
                } else if (today_day == "Sunday"){
                    dia = "D"
                }
                return dia // Get the current day using the utility function
            },
            isButtonVisible(cu) {
                var show = false;
                var day_week = this.currentDay()

                if (day_week === cu.dia){
                    const today = new Date();
                    const year = today.getFullYear();
                    const month = String(today.getMonth() + 1).padStart(2, "0");
                    const day = String(today.getDate()).padStart(2, "0");

                    const date1 = new Date(`${year}-${month}-${day}T${cu.hora_inicio}`);
                    const date2 = new Date(`${year}-${month}-${day}T${cu.hora_fin}`);

                    console.log(date1)
                    console.log(date2)
                    console.log(today)

                    if (today >= date1 && today <= date2) {
                        show = true
                    }
                } else {
                    console.log("No es el día " + day_week)
                }
                return show;
            },
            captureImage(matri) {     

                const canvas = document.createElement('canvas');
                const video = this.$refs.videoElement;

                canvas.width = video.videoWidth;
                canvas.height = video.videoHeight;

                const context = canvas.getContext('2d');
                context.drawImage(video, 0, 0, canvas.width, canvas.height);

                this.photo = canvas.toDataURL("image/png");

                // Convert canvas data to a Blob object
                canvas.toBlob((blob) => {
                    // Create a File object from the Blob
                    const fil = new File([blob], 'captured-image.png', { type: 'image/png' });

                    // You can perform further processing with the captured image here
                    var config_request = {
                        "Content-Type": "application/json",
                        "Access-Control-Allow-Origin": "*"
                    };

                    var data = {
                        path: fil,
                        fecha_asistencia: this.today,
                        matricula: matri
                    };

                    axios.put(`${this.postURL}/asistencia`, data, config_request)
                        .then((res) => {
                        console.log(res.data);
                        })
                        .catch((error) => {
                        console.log(error);
                        });

                    // Close the modal after capturing the image
                    this.closeModal();
                    this.noasis = false
                }, 'image/png');


                }
        },
        created() {
            axios.post(this.postURL + '/cursosuser', {dni: "71218699"},  {
                        'Content-Type': 'application/json',
                        'Access-Control-Allow-Origin': '*'
                    } )
            
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