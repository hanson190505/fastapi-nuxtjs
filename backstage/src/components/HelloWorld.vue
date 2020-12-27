<template>
  <div>
  <h1>{{ msg }}</h1>
  <button @click="count++">count is: {{ count }}</button>
  <p>Edit <code>components/HelloWorld.vue</code> to test hot module replacement.</p>
  <form :model="formData" ref="formRef">
    <input type="username" v-model="formData.username">
    <input type="password" v-model="formData.password">
  </form>
  <button @click="handleAxios">请求</button>
  <button @click="handleAxios2">创造</button>
    </div>
</template>

<script>
import axios from 'axios'
// import qs from 'qs'   报错
import {reactive, ref, unref} from "vue";
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      count: 0
    }
  },
  setup(){
    const formRef = ref(null);
    const formData = reactive(
        {
          username: '',
          password: ''
        }
    )
    function handleAxios(){
      const form = unref(formRef);
      axios.post('http://localhost:8000/api/v1/login/access_token', {"username": "hanson", "password": "123445"}, {
        headers : {'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
          "grant-type": "password"
        }
      })
      // axios.get('http://localhost:8000/api/v1/users')
    }
    function handleAxios2(){
       axios.post('http://localhost:8000/api/v1/departments', {"name": "hahaha1111"}, {
        headers : {'content-type': 'application/x-www-form-urlencoded;charset=UTF-8'}
      })
    }
    return {
      handleAxios,
      formData,
      formRef,
      handleAxios2
    }
  }
}
</script>
