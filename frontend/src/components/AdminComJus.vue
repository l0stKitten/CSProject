<template>
    <MenuCompAd/>
    <div class="card-grid">
      <Card v-for="just in justificaciones" :key="just.codigo" style="width: 25em">
        <template #title>{{ just.titulo }}</template>
        <template #subtitle>{{ just.full_name }}</template>
        <template #content>
          <p>{{ just.descripcion }}</p>
        </template>
        <template #footer>
            <p>{{ just.fecha_asistencia }}</p>
          <Button icon="pi pi-pencil" severity="warning" label="Editar" />
        </template>
      </Card>
    </div>
</template>

<script>
    import axios from 'axios'
    import MenuCompAd from './MenuCompAd.vue';
    export default {
    data() {
        return {
            justificaciones: [],
            postURL: 'http://127.0.0.1:5000',
            config_request: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
        };
    },
    created() {
        axios.post(this.postURL + '/justificaciones')
            .then((res) => { this.justificaciones = res.data; })
            .catch((error) => { console.log(error) })
    },
    components: { MenuCompAd }
    };
</script>

<style>
    .card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    grid-gap: 1rem;
    margin-top: 40px;
    }
</style>