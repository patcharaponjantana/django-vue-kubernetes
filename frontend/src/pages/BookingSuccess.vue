<template>
    <div className="flex flex-col items-center  mb-5">
        <h1 className="text-3xl font-bold mb-9 mt-7">Booking Successful!</h1>
        <p className="text-base mb-7">
            Thank you for booking with us. Your booking has been confirmed and your
            ticket have been sent to your email. 
        </p> 
        <p className="text-sm mb-7">
            Please save the QR Code below (same as in email) and show for boarding.
        </p>

        <a-qrcode value="https://ant.design/" />

        <div className="text-sm mt-7 mb-4">If you didn't receive any confirmation email, please resend it to your email again</div>
        <div className="flex items-center justify-center">
            <a-form
                name="basic"
                :model="formState"
                @finish="onFinish"
                autoComplete="off"
            >
                <a-form-item
                    label="Email"
                    name="email"
                    :rules="[{ type: 'email', message: 'The input is not valid Email!'}]"
                >
                    <a-input v-model:value="formState.email" />
                </a-form-item>

                <a-form-item>
                    <button 
                        type="submit"
                        :style="{ width: '50%' }"
                        className="w-full bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded"
                    >
                        Resend Email
                    </button>
                </a-form-item>
            </a-form>
        </div>  
    </div>
</template>

<script setup lang="ts">
import { reactive } from "vue";

interface FormState {
    email: string;
}
const formState = reactive<FormState>({
    email: '',
})

const onFinish = (values: any) => {
    console.log('Success:', values);
    alert(`email is sended to ${formState.email}!!`)
};
</script>

<style lang="scss" scoped>
</style>
