<template>
    <div>
      <div class="section-initial">
        <div class="desc">
          <h2>Вебсайт для <span style="color: #1572D3;">швидкого</span> пошуку та перегляду деталей автомобіля</h2>
          <p>
            Швидко знаходь необхідну машину, введи її характеристики та отримай необхідні запчастини
          </p>
        </div>
        <div class="background-car__main">
          <img src="../assets/car.png" alt="">
        </div>
      </div> 
      <div class="second-section">
        <h2>3 причини чому варто з нами працювати</h2>
        <div class="icons-section">
          <div>
              <i class="fas fa-book"></i>
              <h3>Оригінальні каталоги</h3>
              <p>Підбір унікальних запчастин, що відповідають характеристикам автомобіля.</p>
          </div>
          <div>
              <i class="fas fa-search"></i>
              <h3>Швидкі результати</h3>
              <p>Швидкий пошук та отримання потрібних деталей за мінімальний час.</p>
          </div>
          <div>
              <i class="fas fa-tools"></i>
              <h3>Професійний підбір</h3>
              <p>Професійний відбір автомобільних компонентів для точного відповідності потребам кожного автомобіля.</p>
          </div>
        </div>
      </div>
      <div class="third-section">
        <h2>Найпопулярніші автомобілі</h2>
        <div class="item-flex">
          <a :href="`#/model/${item.id}`" v-for="item in threemodels" :key="item.id" class="product-link" @mouseover="setSelectedProductId(item.id)">
            <img :src="getPhoto(item)">
            <div class="centdet">
              <p id="boldname">{{ item.model_name }}</p>
              <p>Рік: {{ item.model_years_of_production }}</p>
              <p>Тип кузова: {{ item.model_body_type }}</p>
              <p>Привід: {{ item.model_wheel_drive_type }}</p>
            </div>
          </a>
        </div>
      </div>
      <div class="cars-company">
        <h2 class="bold-cars">Про компанію</h2>
        <p class="about-text">
          Наш інтернет-майданчик - це веб-проєкт, що динамічно розвивається, що спеціалізується на сегменті електронної комерції серед українських сайтів, 
          спрямованих на підбір моторних олив, фільтрів та інших автомобільних товарів. У <span style="color: #1572D3;">2023</span> році ми були визнані одними з лідерів у цій 
          галузі, зосереджуючи увагу на наданні власникам автотранспорту простого та зручного способу знаходження необхідних аксесуарів та розхідних матеріалів 
          для їхніх транспортних засобів.
        </p>
      </div>
    </div>
  </template>
  
<script>
import axios from 'axios';
import '@fortawesome/fontawesome-free/css/all.css';
  
  export default {
    data() {
      return {
        selectedCategoryId: null,
        brands: [],
        threemodels: [],
        selectedProductId: null
      };
    },
    mounted() {
      axios.get(`${process.env.VUE_APP_BACKEND_URL}/home/`)
        .then((response) => {
          this.threemodels = response.data.top_3_cars_info;
          const storedId = localStorage.getItem('id');
          if (storedId) {
            this.selectedProductId = parseInt(storedId);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    watch: {
      selectedProductId: function(newVal) {
        localStorage.setItem('Model_id', newVal.toString());
      }
    },
    methods: {
      setSelectedProductId(Model_id) {
        this.selectedProductId = Model_id;
      },
      getPhoto(detail) {
        try {
          const photoPath = detail.model_image.split('/images/CarModels/')[1];
          const fileName = photoPath.split('/').pop();
          return require(`@/../../backend/images/CarModels/${fileName}`);
        } catch (error) {
          console.error('Error loading photo:', error);
          return '';
        }
      },
    }
  };
</script>
<style>
/* перша секція */
.section-initial {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 0 auto;
  padding: 20px 0;
}
.section-initial .desc {
  padding: 0 70px 0 350px;
}
.section-initial .desc h2 {
  font-style: normal;
  font-weight: 600;
  font-size: 48px;
  line-height: 120%;
  color: #242424;
}
.section-initial .desc p {
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 150%;
  color: #272727;
}
.background-car__main {
  background-image: url(../assets/back.png);
  background-repeat: no-repeat;
  background-position: right;
  background-size: 70%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.background-car {
  background-image: url(../assets/back.png);
  background-repeat: space repeat;
  background-position: top right;
  background-size: 60%;
}
.background-car img {
  padding-top: 50px;
}
/* друга секція */
.second-section h2 {
  text-align: center;
  font-style: normal;
  font-weight: 500;
  font-size: 38px;
  line-height: 130%;
  color: #333333;
  margin-bottom: 70px;
}
.icons-section {
  display: flex;
  text-align: center;
  justify-content: center;
  gap: 50px;
}
.icons-section div {
  width: 350px;
}
.icons-section div i {
  background-color: #ECF5FF;
  color: #1572D3;
  font-size: 45px;
  padding: 40px;
  border-radius: 15px;
}
.icons-section div h3 {
  font-style: normal;
  font-weight: 500;
  font-size: 20px;
  line-height: 150%;
  color: #000000;
}
.icons-section div p {
  font-style: normal;
  font-weight: 500;
  font-size: 14px;
  line-height: 150%;
  color: #6D6D6D;
}
/* Третя секція */ 
.third-section h2, .cars-company h2 {
  text-align: center;
  font-style: normal;
  font-weight: 500;
  font-size: 38px;
  line-height: 130%;
  color: #333333;
  margin: 70px 0;
}
.product-link {
  text-decoration: none;
  padding: 15px;
  box-shadow: 0px 12px 24px rgba(16, 76, 139, 0.16); 
  border-radius: 15px;
  transition: box-shadow 0.3s ease-in-out, transform 0.3s ease-in-out;
}
.product-link:hover {
  box-shadow: 0px 12px 24px rgba(16, 76, 139, 0.5); 
  transform: scale(1.05); 
}
.product-link img {
  width: 350px;
  height: 270px;
  object-fit: contain;
  border-radius: 15px;
}
#boldname {
  font-style: normal;
  font-weight: 500;
  font-size: 20px;
  line-height: 25px;
  color: #262626;
  margin-bottom: 10px;
}
.centdet {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.centdet p {
  margin: 7px;
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 17px;
  color: #959595;
}
.about-text {
  font-size: 20px;
  text-align: justify;
  line-height: 1.5;
  color: #5a5a5a;
}
.item-flex {
  display: flex;
  justify-content: center;
  margin: 0 0 40px;
}
.item-flex > a:nth-child(2) {
  margin: 0 80px;
}
.cars-company {
  width: 1050px;
  margin: 50px auto;
  text-align: left;
}
</style>