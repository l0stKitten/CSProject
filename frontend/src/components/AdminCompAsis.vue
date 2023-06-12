<template>
    <MenuCompAd/>
    <div class="card custom-margin">
        <div class="container">
            <h2>Asistencias</h2>
        </div>
        
        <DataTable :value="asistencias" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem">
            <Column field="nombre" header="Curso"></Column>
            <Column field="full_name" sortable header="Alumno"></Column>
            <Column field="fecha_asistencia" sortable header="Fecha Asistencia"></Column>
            <Column field="estado" header="Estado" dataType="boolean" bodyClass="text-center" style="min-width: 8rem">
                <template #body="{ data }">
                    <i class="pi" :class="{ 'pi-check-circle text-green-500 ': data.estado, 'pi-times-circle text-red-500': !data.estado }"></i>
                </template>
                <template #filter="{ filterModel }">
                    <label for="estado-filter" class="font-bold"> Asistió </label>
                    <TriStateCheckbox v-model="filterModel.value" inputId="estado-filter" />
                </template>
            </Column>
            <Column header="Editar">
                <template #body>
                    <Button label="Editar" severity="warning"></Button>
                </template>
            </Column>
            <Column header="Eliminar"> ¿
                <template #body>
                    <Button label="Eliminar" severity="danger"></Button>
                </template>
            </Column>
        </DataTable>
    </div>
</template>

<script>
    import axios from 'axios'
    import PopUpFormAsis from './PopUpFormAsis.vue';
    import MenuCompAd from './MenuCompAd.vue';

    export default {
        data() {
        return {
            asistencias: [],
            postURL: 'http://127.0.0.1:5000',
            config_request: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
        };
    },
    created() {
        axios.post(this.postURL + '/asistencias')
            .then((res) => { this.asistencias = res.data; })
            .catch((error) => { console.log(error) })
    },
    components: { PopUpFormAsis, MenuCompAd }
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

    .right-align {
        display: flex;
        justify-content: flex-end;
    }
</style>