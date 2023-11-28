<template>
    <div className="">        
      <div className="flex pb-3">
        <div className="flex-col text-left mr-5" >
            <a href="#" @click="goPreviousPage"><ArrowLeftOutlined /></a>
        </div>
        <div className="flex-col text-left">      
            <div className="text-sm font-bold"> {{props.start}} to {{props.end}}</div>
            <div className="text-xs"> {{props.date}} |  {{props.passengers}} passengers</div>
        </div>
      </div>
      <hr/>

      <div>      
        <div className="mb-6">
            <h2 className="text-xs mt-4 mb-4 text-left">{{ filteredTickets.length }} results for {{ props.date }}</h2>
            
            <div v-for="ticket in filteredTickets">
                <Ticket 
                    :key="ticket.date"
                    :id="ticket.date"
                    :from="props.start"
                    :to="props.end"
                    :departureTime="ticket.departureTime"
                    :arriveTime="ticket.arriveTime"
                    :duration="ticket.duration"
                    :price="ticket.price"
                    :date="ticket.date"
                />
            </div>
        </div>
      </div>
    </div>
</template>

<script setup lang="ts">
import { ref, reactive, computed } from 'vue';
import Ticket from '../components/Ticket.vue'
import { useRouter } from "vue-router";
import { ArrowLeftOutlined } from '@ant-design/icons-vue';

const router = useRouter();

interface ListTicketPageProps {
  start: string;
  end: string;
  passengers: number;
  date: string;
}

const props = defineProps<ListTicketPageProps>()

console.log(props)

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

const goPreviousPage = () => router.go(-1);

// const filteredTickets = tickets.filter((ticket) => ticket.date === selectedDate);

</script>

<style lang="scss" scoped>
</style>
