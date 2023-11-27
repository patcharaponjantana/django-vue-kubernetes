<template>
    <div className="">        
      <div className="flex pb-3">
        <div className="flex-col text-left mr-5" >
            <!-- <a href="#" onClick={() => navigate(-1)}><ArrowLeftOutlined /></a> -->
        </div>
        <div className="flex-col text-left">      
            <div className="text-sm font-bold"> {{props.start}} to {{props.end}}</div>
            <div className="text-xs"> {{props.date}} |  {{props.passengers}} passengers</div>
        </div>
      </div>
      <hr/>

      <!-- <div>      
        <div className="mb-6">
            <h2 className="text-xs mt-4 mb-4 text-left">{filteredTickets.length} results for {selectedDate}</h2>
            
            {filteredTickets.map((ticket) => (
                <Ticket
                key={ticket.date}
                id={ticket.date}
                from={start}
                to={end}
                departureTime={ticket.departureTime}
                arriveTime={ticket.arriveTime}
                duration={ticket.duration}
                price={ticket.price}
                date={ticket.date}
                />
            ))}
        </div>
      </div> -->
    </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue';
import { useRoute } from 'vue-router'

interface ListTicketPageProps {
  start: string;
  end: string;
  passengers: number;
  date: string;
}

const props = defineProps<ListTicketPageProps>()

console.log(props)

</script>

<style lang="scss" scoped>
</style>
