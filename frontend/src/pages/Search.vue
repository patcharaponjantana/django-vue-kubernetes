<template>
    <ListTicketPage :start="query.from" :end="query.to" :passengers="query.passengers" :date="query.date" :tickets="searchResult" />
</template>

<script setup lang="ts">
import { ref, reactive, computed, onMounted } from 'vue';
import { useRoute } from 'vue-router'
import ListTicketPage from '../components/ListTicketPage.vue'
import { useMainStore } from '../stores/main.store'

const route = useRoute()
const store = useMainStore();

const query = reactive<any>(route.query);
query.from = query.from || "Phuket"
query.to = query.to || "PhiPhi"
query.passengers = parseInt(query.passengers || '1')
query.date = query.date || "2023-11-28"

const searchResult = computed(() => {
    return store.searchResult.map((item: any) => {
        item['date'] = query.date
        item['departureTime'] = item['departure_time']
        item['arriveTime'] = item['arrive_time']
        item['duration'] = '30 minutes'
        return item
    })    
})

onMounted(() => {
    store.getSearchResult(query.from, query.to, query.date) // <div>
})

</script>

<style lang="scss" scoped>
</style>
