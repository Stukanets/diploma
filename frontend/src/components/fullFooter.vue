<template>
  <footer v-for="item in footerFull" :key="item.Electronic_store_logo_photo" >
    <div class="up__left cnter">
      <img src="../assets/Frame (2).png" alt="">
      <h2 id="color-white">{{ item.company_name }} </h2>
    </div>
      <div class="gradient-change">
        <div class="footerFull-midd">
          <p>НАШІ КОНТАКТИ</p>
          <div class="footerFull-midd__pers">
            <i class="fas fa-phone footerFull-icons gap-i"></i>
            <a :href="'tel:' + phoneNumberCh(item.company_phone_number)">{{ phoneNumberCh(item.company_phone_number) }}</a>
          </div>
          <div class="top__right-email">
            <i class="fa-solid fa-envelope gap-i"></i>
            <a v-bind:href="'mailto:' + company_email " class=""> {{ item.company_email }}</a>
          </div>
        </div>
      </div>
      <div class="fot-bottom">
        Copyright 2024 ・ {{ item.company_name }}, All Rights Reserved
      </div>
  </footer>
</template>

<script>
import axios from 'axios';
import '@fortawesome/fontawesome-free/css/all.css';

export default {
  data() {
    return {
      footerFull: []
    };
  },
  mounted() {
    axios.get(`${process.env.VUE_APP_BACKEND_URL}/home/`)
      .then((response) => {
        this.footerFull = response.data.company_info;
      })
      .catch((error) => {
        console.log(error);
      });
  },
  methods: {
    phoneNumberCh(phoneNumber) {
      return `${phoneNumber.slice(0, 3)} (${phoneNumber.slice(3, 6)}) ${phoneNumber.slice(6, 9)}-${phoneNumber.slice(9, 11)}-${phoneNumber.slice(11)}`
    }
  }
};
</script>
<style>
.cnter {
  padding: 30px 0;
  margin: 0 auto;
}
footer {
  font-size: 18px;
  background-color: #051C34;
}
.footerFull-midd a, #color-white {
  text-decoration: none;
  color: white;
}
.footerFull-midd p {
  margin: 0;
}
.footerFull-midd {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 55px;
  color: white;
  padding-bottom: 50px;
  border-bottom: 1px solid white;
  width: 1400px;
  margin: 0 auto;
}
.fot-bottom {
  padding: 40px 0;
  color: white;
  text-align: center;
}
</style>