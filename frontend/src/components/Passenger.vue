<style lang="scss" scoped>
</style>

<template>
  <div>
      <div className="flex flex-col justify-start pl-3 pt-4">
        <div className="text-lg text-left">Contact details</div>
        <div className="text-xs text-left pb-4">This is where your E-ticket will be sent</div>
        <div className="text-left">
        </div>
      </div>
        
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onBeforeMount } from "vue";

interface PassengerProps {
    data: any;
    onSuccess: any;
    onBack: any;
}

const props = defineProps<PassengerProps>()

</script>
