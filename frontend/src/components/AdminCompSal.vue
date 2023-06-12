<template>
    <MenuCompAd/>
    <div class="card custom-margin">
        <div class="container">
            <h2>Salones</h2>
            <div class="right-align">
                <PopUpFormSal/>
            </div>
        </div>
        
        <DataTable :value="salones" paginator :rows="5" :rowsPerPageOptions="[5, 10, 20, 50]" tableStyle="min-width: 50rem">
            <Column field="codigo" header="Código"></Column>
            <Column field="pabellon" sortable header="Pabellón"></Column>
            <Column field="numero" sortable header="Número"></Column>
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
    import PopUpFormSal from './PopUpFormSal.vue';
    import MenuCompAd from './MenuCompAd.vue';

    export default {
        data() {
        return {
            salones: [],
            postURL: 'http://127.0.0.1:5000',
            config_request: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
        };
    },
    created() {
        axios.post(this.postURL + '/salones')
            .then((res) => { this.salones = res.data; })
            .catch((error) => { console.log(error) })
    },
    components: { PopUpFormSal, MenuCompAd }
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