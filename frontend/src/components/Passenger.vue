<style lang="scss" scoped>
</style>

<template>
  <div>
      <div className="flex flex-col justify-start pl-3 pt-4">
        <div className="text-lg text-left">Contact details</div>
        <div className="text-xs text-left pb-4">This is where your E-ticket will be sent</div>
        <div className="text-left">
          <a-form
            name="basic"
            :label-col="{ span: 4 }"
            :model="props.data"
            @finish="props.onSuccess"
            autoComplete="off"
          >
            <a-form-item
                label="Name"
                name="name"
                :rules="[{ required: true, message: 'Please input your name!' }]"
            >
              <a-input v-model:value="props.data.name" />
            </a-form-item>

            <a-form-item
                label="Email"
                name="email"
                :rules="[
                { type: 'email', message: 'The input is not valid Email!'},
                { required: true, message: 'Please input your email!' }
              ]"
            >
              <a-input v-model:value="props.data.email" />
            </a-form-item>

            <a-form-item
                label="Nationality"
                name="nationality"
            >
              <a-input v-model:value="props.data.nationality" />
            </a-form-item>

            <a-form-item>
              <div className='flex flex-row space-x-1'>
                <button
                    className="text-left bg-blue-400 hover:bg-blue-700 text-white text-sm font-bold py-2 px-2  rounded focus:outline-none focus:shadow-outline"
                    @click="()=>{onBack(data)}"
                >
                    <LeftOutlined className='font-bold text-sm'/>
                </button>
                <button
                    type='submit'
                    className="w-11/12 bg-blue-500 hover:bg-blue-700 text-white text-sm font-bold py-2 px-2   rounded focus:outline-none focus:shadow-outline"
                    style="width: 100%"
                >
                    <div className='flex flex-row'>
                      <div className='text-center w-11/12'>
                        Next
                      </div>
                      <div className='text-right w-1/12'>
                        <RightOutlined className='font-bold text-sm'/>
                      </div>
                    </div>
                </button>
              </div>
            </a-form-item>
          </a-form>
        </div>
      </div>
        
    </div>
</template>

<script setup lang="ts">
import { LeftOutlined, RightOutlined } from '@ant-design/icons-vue';

interface PassengerProps {
    data: any;
    onSuccess: any;
    onBack: any;
}

const props = defineProps<PassengerProps>()

</script>
