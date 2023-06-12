<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import MenuCompAd from './components/MenuCompAd.vue';
import TableComp from './components/TableComp.vue';
import PopUpForm from './components/PopUpForm.vue'
import MenuCompAl from './components/MenuCompAl.vue';
import MenuCompPro from './components/MenuCompPro.vue';
import LogIn from './components/LogIn.vue';

export default {
  name: 'App',
  components: {
    TableComp,
    MenuCompAd,
    PopUpForm,
    MenuCompAl,
    MenuCompPro,
    LogIn
}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
  margin-top: 0px;
  margin-left: 5%;
  margin-right: 5%;
}
</style>

