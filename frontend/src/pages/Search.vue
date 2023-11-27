<template>
    <ListTicketPage :start="query.from" :end="query.to" :passengers="query.passengers" :date="query.date" />
    {{ query.from }}
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRoute } from 'vue-router'
import ListTicketPage from '../components/ListTicketPage.vue'

const route = useRoute()

const query = ref<any>({});
query.value = route.query;
query.value.from = query.value.from || "PhiPhi"
query.value.to = query.value.to || "Phuket"
query.value.passengers = parseInt(query.value.passengers || '1')
query.value.date = query.value.date || "2023-03-23"
</script>

<style lang="scss" scoped>
</style>
