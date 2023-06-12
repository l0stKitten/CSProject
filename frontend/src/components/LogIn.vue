<template>
    <div class="login-container">
      <Card title="Login" class="login-card">
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
          <Button label="Login" class="p-button-primary" severity="info"  @click="login" />
        </div>
      </Card>
    </div>
  </template>
  
<script>
  import { ref } from "vue";
  import { Card } from "primevue/card";
  import { InputText } from "primevue/inputtext";
  import { Password } from "primevue/password";
  import { Button } from "primevue/button";
  
  export default {
    components: {
      Card,
      InputText,
      Password,
      Button
    },
    setup() {
      const username = ref("");
      const password = ref("");
  
      const login = () => {
        // Perform login logic here
        if (username.value === "admin" && password.value === "password") {
          // Redirect to dashboard or perform other actions
          console.log("Logged in successfully");
        } else {
          console.log("Invalid username or password");
        }
      };
  
      return {
        username,
        password,
        login
      };
    }
  };
</script>
  
<style scoped>
  .login-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
  
  .login-card {
    width: 300px;
  }
  .login-header {
    display: flex;
    justify-content: center;
    margin-bottom: 2rem;
}
  
  .p-field {
    margin-bottom: 1rem;
  }
</style>
  