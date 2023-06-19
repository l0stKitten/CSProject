<template>
    <div class="modal" v-if="showModal">
      <div class="modal-content">
        <video ref="videoElement" autoplay></video>
        <button @click="startCamera">Start Camera</button>
        <button @click="stopCamera">Stop Camera</button>
        <button @click="captureImage">Capture Image</button>
        <button @click="closeModal">Close</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        showModal: false,
        mediaStream: null,
      };
    },
    methods: {
      startCamera() {
        navigator.mediaDevices
          .getUserMedia({ video: true })
          .then((stream) => {
            this.mediaStream = stream;
            this.$refs.videoElement.srcObject = stream;
          })
          .catch((error) => {
            console.log('Error accessing camera:', error);
          });
      },
      stopCamera() {
        if (this.mediaStream) {
          this.mediaStream.getTracks().forEach((track) => {
            track.stop();
          });
          this.$refs.videoElement.srcObject = null;
          this.mediaStream = null;
        }
      },
      captureImage() {
        const canvas = document.createElement('canvas');
        const video = this.$refs.videoElement;
  
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
  
        const context = canvas.getContext('2d');
        context.drawImage(video, 0, 0, canvas.width, canvas.height);
  
        // You can perform further processing with the captured image here
  
        // Close the modal after capturing the image
        this.closeModal();
      },
      closeModal() {
        this.showModal = false;
      },
    },
  };
  </script>
  
  <style>
  .modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .modal-content {
    background-color: white;
    padding: 1rem;
  }
  
  video {
    width: 100%;
  }
  </style>