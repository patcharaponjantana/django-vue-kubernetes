<style lang="scss" scoped>
</style>

<template>
  <div>
    <a href="booking-success">
      <button 
          :style="{ width: '25%' }"
          className="w-full bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded"
        >
          Pay
      </button>
    </a>
  </div>
</template>

<script setup lang="ts">

interface PaymentProps {
  nPassenger: number;
  tripDetail: any;
}

const props = defineProps<PaymentProps>()

</script>
