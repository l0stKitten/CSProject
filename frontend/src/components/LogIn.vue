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
          <Password id="password" v-model="password" />
        </div>
        <Button label="Login" class="p-button-primary" severity="info" type="submit" />
      </div>
    </form>
  </div>
</template>

<script>
  import { ref } from "vue";
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
        password: "",
      };
    },
    methods: {
      login() {
        // Implement your login logic here
        console.log("Username:", this.username);
        console.log("Password:", this.password);

        // Reset the form after login attempt
        this.username = "";
        this.password = "";
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