<style lang="scss" scoped>
</style>

<template>
  <div>
      <div>
        <div className="text-left text-lg">
          Ticket Summary
        </div>

        <div className="text-left text-xs">
          Please verify the ticket information
        </div>
      </div>

      <div className="bg-white shadow-lg rounded-lg overflow-hidden my-3 border-2">

        <!-- {/* top part */} -->
        <div className="flex flex-col px-4 pt-5 pb-3 sm:p-6">
          <div className="text-sm text-left font-bold">
            Company A, High Speed Ferry
          </div>
          <div className="flex flex-row justify-between text-xs text-left">
            <div className="pr-2">Departure Date:</div> 
            <div>Fri, 23 Mar</div>
          </div>
          <div className="flex flex-row justify-between text-xs text-left">
            <div className="pr-2">Location:</div> 
            <div>Koh Phi Phi Ferry Port</div>
          </div>


          <!-- {/* middle part */} -->
          <div className="flex items-center justify-between  py-4">         

            <div className="flex flex-col">
              <div className="text-sm font-bold">
                {{departureTime}}
              </div>
              <div className="inline-flex items-center px-2.5 py-0.5 rounded-full text-sm font-medium bg-blue-100 text-blue-800 text-xs">
                {{from}}
              </div>
            </div>
              
            <div className="flex flex-col">
              <div className="text-xs">
                {{duration}} 
              </div>
              <svg height="10" width="80">
                <line x1="0" y1="0" x2="80" y2="0" :style="{stroke: 'black', strokeWidth:2 }" />
              </svg>
            </div>


            <div className="flex flex-col">
              <div className="text-sm font-bold">
                {{arriveTime}} 
              </div>
              <div className="inline-flex items-center px-2.5 py-0.5 rounded-full text-sm font-medium bg-blue-100 text-blue-800 text-xs">
                {{to}}
              </div>
            </div>
          </div>
        </div>
        <hr/>

        <!-- {/* bottom part */} -->
        <div className="px-2 py-3 sm:p-6">
          <div className="flex flex-row justify-between text-gray-700 "> 
            <div className="text-left text-xs">
              ticket price
            </div>
            <div className="text-left text-xs ">
              THB {{price}}
            </div>
          </div>
          <div className="flex flex-row justify-between text-gray-700"> 
            <div className="text-left text-xs">
              no. of passengers
            </div>
            <div className="text-left text-xs">
              1
            </div>
          </div>
          <div className="flex flex-row justify-between mt-2"> 
            <div className="text-left text-sm">
              Total Price
            </div>
            <div className="">
              <div className="flex flex-col">
                <div className="text-sm font-bold">
                  THB {{price}} 
                </div>
              </div>
            </div>
          </div>  
        </div>
      </div>
      
      <div className="mt-4 ">
        <button
            className="w-full bg-blue-500 hover:bg-blue-700 text-white text-sm font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            @click="()=>{onSuccess(data);}"
        >
          Next
        </button>
      </div>
      

  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";

interface ItineraryProps {
    nPassenger: number;
    tripDetail: any;
    data: any;
    onSuccess: any;
}

const props = defineProps<ItineraryProps>()

// let sourceDate = new Date(props.tripDetail['source']['datetime']);
// let destinationDate = new Date(props.tripDetail['destination']['datetime']);
// let ticket = { date: '2023-03-23', time: "9:00 AM - 12:00 PM", duration: "3 hours", price: 20, from: 'phiphi', to: 'phuket', travelTime: "3 hours" };
let departureTime = ref('9:00 AM');
let from = ref('Koh Phi Phi');
let duration = ref(props.tripDetail['duration']);
let arriveTime = ref('10:00 AM');
let to = ref('Phuket');
let price = ref('200');

</script>
