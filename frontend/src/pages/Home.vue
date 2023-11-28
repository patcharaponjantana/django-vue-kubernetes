<template>
    <div className="flex flex-col items-center justify-center text-left">
        <div className='mb-4 font-bold text-xl'>Ferry Transfer Booking for Koh Phi Phi</div>
            
        <a-form
            name="basic"
            layout="horizontal"
            :label-col="{ span: 13 }"
            :wrapper-col="{ span: 30 }"
            :model="formState"
            @finish="onButtonClick"
            @finishFailed="onFinishFailed"
            autoComplete="off"
        >
            <a-form-item
                name="from"
            >
                <template v-slot:label>
                    <label className="font-bold" :style="{ fontSize: '15px'}">From</label>
                </template>
                <a-select
                    v-model:value="formState.from"
                    show-search
                    placeholder="From"
                    option-filter-prop="children"
                    @change="onChange"
                    @search="onSearch"
                    :filter-option="filterOption"
                    :options="options"
                >
                </a-select>
            </a-form-item>
           
            <a-form-item
                name="to"
            >
                <template v-slot:label>
                    <label className="font-bold" :style="{ fontSize: '15px'}">To</label>
                </template>
                <a-select
                    v-model:value="formState.to"
                    show-search
                    placeholder="To"
                    option-filter-prop="children"
                    @change="onChange"
                    @search="onSearch"
                    :filter-option="filterOption"
                    :options="options"
                >
                </a-select>
            </a-form-item>
            
            <a-form-item
                name="passengers"
            >
                <template v-slot:label>
                    <label className="font-bold" :style="{ fontSize: '15px'}">No. of Passengers</label>
                </template>
                <a-input-number
                    v-model:value="formState.passengers" 
                    :min="1" 
                    :max="10"
                    style="width: 100%;"
                />
            </a-form-item>

            <a-form-item
                name="travelDate"
            >
                <template v-slot:label>
                    <label className="font-bold" :style="{ fontSize: '15px'}">Departure Date</label>
                </template>
                <a-date-picker
                    v-model:value="formState.travelDate" 
                    date-format="YYYY/MM/DD"
                    style="width: 100%;"
                />
            </a-form-item>
            
            <a-form-item>
                <button
                    style="width: 100%;"
                    type="submit" 
                    className="bg-blue-500 hover:bg-blue-700 text-white font-bold text-sm py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                >
                    Find
                </button>
            </a-form-item>
        </a-form>
    </div>
</template>

<script setup lang="ts">
import { ref, reactive, computed, onMounted } from 'vue';
import dayjs, { Dayjs } from 'dayjs';
import customParseFormat from 'dayjs/plugin/customParseFormat';
import { useRouter } from "vue-router";
import { useMainStore } from '../stores/main.store'

const store = useMainStore()
const router = useRouter();

dayjs.extend(customParseFormat);
const dateFormat = 'YYYY/MM/DD'; 

interface FormState {
    from: string;
    to: string;
    passengers: number;
    travelDate: Dayjs;
}

const formState = reactive<FormState>({
    from: 'Phuket',
    to: 'PhiPhi',
    passengers: 1,
    travelDate: dayjs('2023-11-28', dateFormat),
});

const options = computed(() => {
    return store.location.map((item: any) => {
        item['value'] = item['name']
        item['label'] = item['name']
        return item
    })    
})

onMounted(() => {
    store.getLocationList() // <div>
})


const onChange = (value: string) => {
  console.log(`selected ${value}`);
};

const onSearch = (value: string) => {
  console.log('search:', value);
};

const onButtonClick = (values: any) => {
  console.log('Success:', values);
  router.push({ name: "search" })
};

const onFinishFailed = (errorInfo: any) => {
  console.log('Failed:', errorInfo);
};

const filterOption = (input: string, option: any) => (option?.label ?? '').toLowerCase().includes(input.toLowerCase())

</script>

<style lang="scss" scoped>
</style>
