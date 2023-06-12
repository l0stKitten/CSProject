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
    import { useRouter } from "vue-router";

    const router = useRouter();
    const items = ref([
        { 
            label: 'Perfil', 
            icon: 'pi pi-fw pi-user',
            items: [{ 
                label: 'Configuración',
                icon: 'pi pi-fw pi-cog',
                command: () => router.push('/admin/config')
            },
            { 
                label: 'Cambiar Contraseña',
                icon: 'pi pi-fw pi-cog',
                command: () => router.push('/admin/config/password')
            }
            ]
        },
        {
            label: 'Usuarios',
            icon: 'pi pi-fw pi-users',
            items: [
                {    
                    label: 'Agregar Usuario',
                    icon: 'pi pi-fw pi-plus',
                    command: () => router.push('/admin/adduser')
                },    
                {
                    separator: true
                },
                {
                    label: 'Alumno',
                    icon: 'pi pi-fw pi-user',
                    command: () => router.push('/admin/alumnos')
                },
                
                {
                    label: 'Profesor',
                    icon: 'pi pi-fw pi-user',
                    command: () => router.push('/admin/profesores')
                },
                {
                    label: 'Administrador',
                    icon: 'pi pi-fw pi-user',
                    command: () => router.push('/admin/administradores')
                }
            ]
        },
        {
            label: 'Académico',
            icon: 'pi pi-fw pi-bookmark',
            items: [
                {
                    label: 'Cursos',
                    icon: 'pi pi-fw pi-bookmark',
                    items: [
                        {
                            label: 'Agregar Curso',
                            icon: 'pi pi-fw pi-plus',
                            command: () => router.push('/admin/cursos/add')
                        },
                        {
                            label: 'Ver Cursos',
                            icon: 'pi pi-fw pi-bookmark',
                            command: () => router.push('/admin/cursos')
                        }
                    ]
                },
                {
                    separator: true
                },
                {
                    label: 'Salones',
                    icon: 'pi pi-fw pi-bookmark',
                    command: () => router.push('/admin/salon')
                },
                {
                    separator: true
                },
                {
                    label: 'Matrícula',
                    icon: 'pi pi-fw pi-bookmark',
                    command: () => router.push('/admin/matricula')
                },
                {
                    separator: true
                },
                {
                    label: 'Asistencia',
                    icon: 'pi pi-fw pi-bookmark',
                    command: () => router.push('/admin/asistencia')
                }
            ]
        },
        {
            label: 'Documentos',
            icon: 'pi pi-fw pi-file',
            items: [
                {
                    label: 'Justificaciones',
                    icon: 'pi pi-fw pi-file',
                    command: () => router.push('/admin/justificaciones')
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