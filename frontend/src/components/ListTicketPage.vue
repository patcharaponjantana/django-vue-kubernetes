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
            <h2 className="text-xs mt-4 mb-4 text-left">{{ tickets.length }} results for {{ props.date }}</h2>
            
            <div v-for="ticket in tickets">
                <Ticket 
                    :key="ticket.date"
                    :id="ticket.date"
                    :from="props.start"
                    :to="props.end"
                    :departureTime="ticket.departureTime.slice(11,16)"
                    :arriveTime="ticket.arriveTime.slice(11,16)"
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
import Ticket from '../components/Ticket.vue'
import { useRouter } from "vue-router";
import { ArrowLeftOutlined } from '@ant-design/icons-vue';

const router = useRouter();

interface TicketDetail {
    date: string; 
    departureTime: string; 
    arriveTime: string;
    duration: string;
    price: number;
}

interface ListTicketPageProps {
  start: string;
  end: string;
  date: string;
  passengers: number;
  tickets: Array<TicketDetail>;  
}

const props = defineProps<ListTicketPageProps>()
const goPreviousPage = () => router.go(-1);


</script>

<style lang="scss" scoped>
</style>
