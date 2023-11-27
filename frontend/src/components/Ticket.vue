<template>
    <div className="bg-white shadow-lg rounded-lg overflow-hidden my-3 border-2">
      <div className="flex flex-col px-4 pt-5 pb-3 sm:p-6">
        <div className="text-xs text-left pb-3">
          Company A, High Speed Ferry
        </div>

        <!-- {/* top part */} -->
        <div className="flex items-center justify-between">         

          <div className="flex flex-col">
            <div className="text-sm font-bold">
              {{props.departureTime}}
            </div>
            <div className="inline-flex items-center px-2.5 py-0.5 rounded-full text-sm font-medium bg-blue-100 text-blue-800 text-xs">
              {{props.from}}
            </div>
          </div>
            
          <div className="flex flex-col">
            <div className="text-xs">
              {{props.duration}} 
            </div>
            <svg height="10" width="80">
              <line x1="0" y1="0" x2="80" y2="0" :style="{stroke: 'black', strokeWidth:2 }" />
            </svg>
          </div>


          <div className="flex flex-col">
            <div className="text-sm font-bold">
              {{props.arriveTime}} 
            </div>
            <div className="inline-flex items-center px-2.5 py-0.5 rounded-full text-sm font-medium bg-blue-100 text-blue-800 text-xs">
              {{props.to}}
            </div>
          </div>
        </div>
      </div>
      <hr/>

      <!-- {/* bottome part */} -->
      <div className="px-2 py-3 sm:p-6">

        <div className="flex flex-row justify-end "> 
          <div className=" pr-3">
            <div className="flex flex-col">
              <div className="text-sm font-bold">
                THB {{props.price}}
              </div>
              <div className="text-xs">
                per passenger
              </div>
            </div>
          </div>
          <div className="">
            <button 
              className="w-full bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded text-sm"
              @click="onButtonClick"
            >
              Book Now
            </button>
          </div>
        </div>


      </div>
    </div>
</template>

<script setup lang="ts">
import { ref, reactive, computed } from 'vue';
import Ticket from '../components/Ticket.vue'
import { useRouter } from "vue-router";

interface TicketProps {
  id: string;
  from: string;
  to: string;
  departureTime: string;
  arriveTime: string;
  duration: string;
  price: number;
  date: string;
}
const props = defineProps<TicketProps>()

const router = useRouter();

const onButtonClick = (values: any) => {
  router.push({ name: "booking" })
};

</script>

<style lang="scss" scoped>
</style>
