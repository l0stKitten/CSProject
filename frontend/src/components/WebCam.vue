<template>
    <div class="camera-container">
        <video ref="videoElement" class="camera-video"></video>
        <div>
            <img v-if="photo" :src="photo" alt="Foto tomada" class="camera-photo">
        </div>
    </div>
    <div class="button-container">
        <Button icon="pi pi-fw pi-camera" @click="captureImage" label="Tomar Asistencia" />
    </div>
</template>

<script>
import axios from 'axios'

export default {
    props: {
        cu: {
        type: Object,
        required: true
        }
    },

    data(){
        return {
            imageBase64: '',
            videoUrl: '',
            photo: null, 
            postURL: 'http://127.0.0.1:5000',
            today: new Date(),
            vec: {},
        }
    },
    methods: {
        dataURItoBlob(dataURI) {
            const byteString = atob(dataURI.split(',')[1]);
            const mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];
            const arrayBuffer = new ArrayBuffer(byteString.length);
            const uint8Array = new Uint8Array(arrayBuffer);

            for (let i = 0; i < byteString.length; i++) {
            uint8Array[i] = byteString.charCodeAt(i);
            }

            return new Blob([arrayBuffer], { type: mimeString });
        },
        captureImage() {   
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

                const canvas = document.createElement('canvas');
                const video = this.$refs.videoElement;
        
                canvas.width = video.videoWidth;
                canvas.height = video.videoHeight;
        
                const context = canvas.getContext('2d');
                context.drawImage(video, 0, 0, canvas.width, canvas.height);

                this.photo = canvas.toDataURL("image/png");

                if (this.photo) {
                    const blob = this.dataURItoBlob(this.photo);
                    console.log(this.cu.codigom)
                    console.log(this.today)

                    const formData = new FormData();
                    formData.append('file', blob, 'image.png');
                    //formData.append('fecha_asistencia', this.today);
                    //formData.append('matricula', this.cu.codigom);
                    //formData.append('dni', "21314566");
                    
                    var vector = {}
                    axios.post(' http://127.0.0.1:81/openfaceAPI', formData)
                    .then(response => {
                        console.log(response.data);
                        vector = response.data

                        const data = {
                            path: vector,
                            fecha_asistencia: this.today,
                            matricula: this.cu.codigom,
                            dni: "71218699"
                        };
                
                        axios.put(`${this.postURL}/asistencia`, data, {
                            "Content-Type": "application/json",
                            "Access-Control-Allow-Origin": "*"
                        })
                            .then((res) => {
                                console.log(res.data);
                                if (res.data.estado){
                                    alert("La Asistencia se guardó con éxito")
                                } else{
                                    alert("No hay coincidencia con la imagen original")
                                }
                            })
                            .catch((error) => {
                            console.log(error);
                            });
                        })
                        .catch(error => {
                        console.error('Error al enviar la imagen al servidor:', error);
                    });                
                }
                
            }
    },
    components:{
    }, created() {        
        navigator.mediaDevices.getUserMedia({ video: true })
            .then((stream) => {
            this.stream = stream;
            this.$refs.videoElement.srcObject = stream;
            this.$refs.videoElement.play();
            })
            .catch((error) => {
            console.error("Error al acceder a la cámara: ", error);
            });
    }, beforeUnmount() {
      if (this.stream) {
        this.stream.getTracks().forEach((track) => track.stop());
      }
    },
}
</script>

<style>
    .camera-video {
        border: 1px solid #ccc;
        box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
        width: 75%;
        height: auto;
    }
    .button-container {
        display: flex;
        justify-content: space-between;
    }
    @media (max-width: 900px) {
        .camera-container {
            flex-direction: column;
        }
    }
</style>