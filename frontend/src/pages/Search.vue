<template>
    <!-- <ListTicketPage :start="query.from" :end="query.to" :passengers="query.passengers" :date="query.date" /> -->
    <ListTicketPage :data="query.from" />
</template>

<script setup lang="ts">
import { ref, reactive, computed, onMounted } from 'vue';
import { useRoute } from 'vue-router'
import ListTicketPage from '../components/ListTicketPage.vue'
import { useMainStore } from '../stores/main.store'

const route = useRoute()
const store = useMainStore();

const query = reactive<any>(route.query);
// query = ;
query.from = query.from || "PhiPhi"
query.to = query.to || "Phuket"
query.passengers = parseInt(query.passengers || '1')
query.date = query.date || "2023-11-28"

const options = computed(() => {
    return store.searchResult.map((item: any) => {
        item['value'] = item['name']
        item['label'] = item['name']
        return item
    })    
})

onMounted(() => {
    store.getSearchResult(query.value.from, query.value.to, query.value.date) // <div>
})


interface ticketDetail {
    date: string; 
    departureTime: string; 
    arriveTime: string;
    duration: string;
    price: number;
}

const tickets = ref<Array<ticketDetail>>([
    { date: '2023-03-23', departureTime: "9:00 AM", arriveTime: "12:00 PM", duration: "3 hours", price: 20.00 },
    { date: '2023-03-23', departureTime: "12:00 AM", arriveTime: "13:00 PM", duration: "1 hours", price: 20.00 },
    { date: '2023-03-24', departureTime: "9:00 AM", arriveTime: "12:00 PM", duration: "3 hours", price: 20.00 },
    { date: '2023-03-25', departureTime: "9:00 AM", arriveTime: "12:00 PM", duration: "3 hours", price: 20.00 },
]);

const filteredTickets = computed(() => {
  return tickets.value.filter((ticket) => ticket.date === props.date);
})


</script>

<style lang="scss" scoped>
</style>
