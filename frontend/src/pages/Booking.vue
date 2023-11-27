<style lang="scss" scoped>
</style>

<template>
    <a-steps
        :current="step"
        @change="onChange"
        :items="[
            {
              title: 'Ticket Summary',
              description: 'Ticket Summary'
            },
            {
              title: 'Contact',
              description: 'Contact Detail'
            },
            {
              title: 'Payment',
              description: 'Payment',
            },
        ]"
    ></a-steps>

    <a-divider></a-divider>
    <!-- <Itinerary nPassenger={3} :tripDetail="tripDetail" :data="data" onSuccess={handleNextStep}/> -->
    <Itinerary :nPassenger="3" :tripDetail="tripDetail" :data="data" />
</template>

<script setup lang="ts">
import { ref } from "vue";
import Itinerary from '../components/Itinerary.vue'

const step = ref<number>(0);
const data = ref({});

interface pointDetail {
    datetime: string; 
    locationName: string; 
}

interface tripDetail {
    source: pointDetail; 
    destination: pointDetail; 
    furryType: string;
    duration: string;
}

const tripDetail = ref<tripDetail>({
  'source': {
    'datetime': '2000-10-31T01:30:00.000-05:00',
    'locationName': 'Koh Phi Phi', 
  },
  'destination': {
    'datetime': '2000-10-31T03:30:00.000-05:00',
    'locationName': 'Phukets', 
  },
  'furryType': 'high speed',
  'duration': '2 hours'
});

const onChange = (value: number) => {
    step.value = value;
};


</script>
