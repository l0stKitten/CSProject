<template>
    <div class="card relative z-2 "> 
        <Menubar :model="items">
            <template #start>
                <img src="@/assets/logo.svg" alt="logo" height="40" class="mr-2" />
            </template>

            <template #end>
                <router-link to="/">
                    <button class="w-full p-link flex align-items-center p-2 pl-4 text-color hover:surface-200 border-noround">
                        <i class="pi pi-power-off" />
                        <span class="custom-margin">Cerrar Sesión</span>
                    </button>
                </router-link>
            </template>
        </Menubar>
    </div>
</template>

<script setup>
    import { ref } from "vue";

    const items = ref([
        { 
            label: 'Perfil', 
            icon: 'pi pi-fw pi-user',
            items: [{ label: 'Configuración', icon: 'pi pi-fw pi-cog' }]
        },
        {
            label: 'Cursos',
            icon: 'pi pi-fw pi-bookmark',
            items: [
                {
                    label: 'Matrícula',
                    icon: 'pi pi-fw pi-bookmark'
                }
            ]
        },
        {
            label: 'Participaciones',
            icon: 'pi pi-fw pi-file'
        },
        {
            label: 'Asistencia',
            icon: 'pi pi-fw pi-file',
            items: [
                {
                    label: 'Justificaciones',
                    icon: 'pi pi-fw pi-file'
                }
            ]
        }
    ]);
</script>


<script>
    import InputText from 'primevue/inputtext'; // Import the InputText component from PrimeVue

    export default {
        components: {
            InputText // Register the InputText component
        },
        // Rest of your component's script code...
    }
</script>

<style scoped>
.custom-margin {
    margin-left: 0.5rem; /* Adjust the value as needed */
}
</style>