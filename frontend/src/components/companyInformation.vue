<template>
    <div class="info-width">
      <div v-for="item in infoJson" :key="item.Website_information" class="info-phones">
        <p class="bold-title-info">Контактна інформація</p>
        <div class="info-tables">
          <div>
            <a :href="'tel:' + formatPhoneNumber(item.company_phone_number)" class="info">Тел.: {{ formatPhoneNumber(item.company_phone_number) }}</a>
            <a v-bind:href="'mailto:' + company_email " class="info">Пошта: {{ item.company_email }}</a>
          </div>
          <div>
            <p class="info">Розробник: {{ item.company_owner }}</p>
            <p class="info">Адреса: {{ item.company_first_address }}</p>
            <p class="info">Адреса: {{ item.company_second_address }}</p>
          </div>
        </div>
      </div>
      <div v-for="item in infoJson" :key="item.Website_information" class="info-width">
        <p class="bold-title-info">Про компанію</p>
        <p class="info-website">
          Наш інтернет-майданчик - це веб-проєкт, що динамічно розвивається, що спеціалізується на сегменті електронної комерції серед українських сайтів, 
          спрямованих на підбір моторних олив, фільтрів та інших автомобільних товарів. У <span style="color: #1572D3;">2023</span> році ми були визнані одними з лідерів у цій 
          галузі, зосереджуючи увагу на наданні власникам автотранспорту простого та зручного способу знаходження необхідних аксесуарів та розхідних матеріалів 
          для їхніх транспортних засобів.
        </p>
        <p class="info-website">
          Наш веб-сайт володіє простим та інтуїтивно зрозумілим інтерфейсом, що дозволяє <span style="color: #1572D3;">швидко</span> та 
          <span style="color: #1572D3;">легко</span> знаходити необхідні деталі. Ми пропонуємо 
          різноманітні фільтри пошуку, включаючи бренд транспортного засобу, його модель та тип запчастини. Крім цього, кожен товар супроводжується детальними описами, 
          технічними характеристиками та фотографіями, що допомагає нашим клієнтам зробити обдумане рішення перед покупкою.
        </p>
        <p class="bold-title-info">Місцезнаходження</p>
        <iframe :src="item.company_address_google_map" width="800" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
      </div>
    </div>
</template>
  
<script>
import axios from 'axios';
import '@fortawesome/fontawesome-free/css/all.css';
  
export default {
data() {
    return {
      infoJson: [],
      };
    },
    mounted() {
      axios.get(`${process.env.VUE_APP_BACKEND_URL}/company_information/`)
        .then((response) => {
          this.infoJson = response.data.company_extended_info;
          console.log(this.infoJson)
        })
        .catch((error) => {
          console.log(error);
    });
    },
    methods: {
    formatPhoneNumber(phoneNumber) {
      return `${phoneNumber.slice(0, 3)} (${phoneNumber.slice(3, 6)}) ${phoneNumber.slice(6, 9)}-${phoneNumber.slice(9, 11)}-${phoneNumber.slice(11)}`
    }
  }
};
</script>
<style>
iframe {
  margin: 0 auto 40px;
  display: flex;
  justify-content: center;
}
.info-width {
  width: 850px;
  margin: 40px auto 0;
}
.bold-title-info {
  text-align: center;
  font-style: normal;
  font-weight: 500;
  font-size: 30px;
  line-height: 130%;
  color: #333333;
  margin-bottom: 40px;
}
.info-website {
  font-size: 18px;
  text-align: justify;
  line-height: 1.5;
  color: #6D6D6D;
}
.info-phones {
  display: flex;
  flex-direction: column;
}
.info-phones .info-tables div {
  display: flex;
  flex-direction: column;
}
.info-phones .info-tables div a:hover {
  color: #1572D3;
}
.info-tables {
  display: flex;
  justify-content: space-between;
  width: 650px;
  margin: 0 auto;
}
.info-phones a {
  margin-bottom: 10px;
  color: #6D6D6D;
}
.info {
  font-size: 18px;
  margin: 0 0 10px 0;
}
</style>