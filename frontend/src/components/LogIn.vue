<template>
  <div class="login-container">
    <form class="login-form" @submit.prevent="login">
      <div class="login-header">
        <img src="@/assets/logo.svg" height="150" alt="Logo" />
      </div>
      <div class="p-fluid">
        <div class="p-field">
          <label for="username">Username</label>
          <InputText id="username" v-model="username" />
        </div>
        <div class="p-field">
          <label for="password">Password</label>
          <Password id="password" v-model="pass" />
        </div>
        <Button label="Login" class="p-button-primary" severity="info" type="submit" />
      </div>
    </form>
  </div>
</template>

<script>
  import axios from 'axios'
  import { useRouter } from "vue-router";
  import { InputText, Password, Button } from "primevue/inputtext";

  export default {
    components: {
      InputText,
      Password,
      Button,
    },
    data() {
      return {
        username: "",
        pass: "",
        postURL: 'http://127.0.0.1:5000',
        route: "",
        router: useRouter()
      };
    },
    methods: {
      check_route(rol_auth) {
        if (rol_auth == "profesor"){
          this.route = "/prof"
        } else if (rol_auth == "alumno"){
          this.route = "/alum"
        } else if (rol_auth == "admin"){
          this.route = "/admin"
        }
      },

      login() {

        axios.post(this.postURL + '/login', {dni: this.username, password: this.pass},  {
                        'Content-Type': 'application/json',
                        'Access-Control-Allow-Origin': '*'
                    } )
            
                .then((res) => { localStorage.setItem('access_token', res.data[0]["access"]); localStorage.setItem('dni', res.data[0]["dni"]); localStorage.setItem('rol', res.data[0]["rol"]);})
                .catch((error) => { console.log(error) })

        // Implement your login logic here        
        this.check_route(localStorage.getItem('rol'))

        console.log(localStorage.getItem('rol'))

        this.router.push(this.route)
      },
    },
  };
</script>

<style scoped>
  .login-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }

  .login-form {
    width: 400px;
    border: 1px solid #ccc;
    padding: 2rem;
    border-radius: 4px;
  }

  .login-header {
    display: flex;
    justify-content: center;
    margin-bottom: 2rem;
  }

  .p-fluid {
    display: flex;
    flex-direction: column;
  }

  .p-field {
    margin-bottom: 1rem;
  }
</style>