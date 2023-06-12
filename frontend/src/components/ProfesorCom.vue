<template>
    <MenuCompPro/>
</template>

<script>
    import MenuCompPro from './MenuCompPro.vue';
    import TableComp from './TableComp.vue';

    export default {
        name: 'App',
        components: {
            TableComp,
            MenuCompPro
        }
    }
</script>