<template>
    <div class="card relative z-2 "> 
        <Menubar :model="items">
            <template #start>
                <img src="@/assets/logo.svg" alt="logo" height="40" class="mr-2" />
            </template>

            <template #end>
                    <button class="w-full p-link flex align-items-center p-2 pl-4 text-color hover:surface-200 border-noround" @click="logout">
                        <i class="pi pi-power-off" />
                        <span class="custom-margin">Cerrar Sesión</span>
                    </button>
            </template>
        </Menubar>
    </div>
</template>

<script setup>
    import { ref } from "vue";
    import { useRouter } from "vue-router";

    const router = useRouter();

    const items = ref([
        { 
            label: 'Perfil', 
            icon: 'pi pi-fw pi-user',
            items: [{ 
                label: 'Configuración',
                icon: 'pi pi-fw pi-cog',
                command: () => router.push('/prof/config')
            },
            { 
                label: 'Cambiar Contraseña',
                icon: 'pi pi-fw pi-cog',
                command: () => router.push('/prof/config/password')
            }
            ]
        },
        {
            label: 'Asistencia',
            icon: 'pi pi-fw pi-users'
        },
        {
            label: 'Justificaciones ',
            icon: 'pi pi-fw pi-bookmark'
        },
        {
            label: 'Participaciones ',
            icon: 'pi pi-fw pi-file',
            command: () => router.push('/prof/part')
        }
    ]);

    const logout = () => {
    // Implement your logout logic here
    // Clear the access token or perform any other necessary actions
        localStorage.removeItem('access_token');
        localStorage.removeItem('dni');
        localStorage.removeItem('rol');
        router.push('/');
    };
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