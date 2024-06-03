<template>
  <header>
    <div class="headIn__class">
      <div class="headIn__class-up">
        <div class="up__left">
          <img src="../assets/Frame.png" alt="">
          <h2 v-for="item in headIn" :key="item.company_name" class="name-titles">{{ item.company_name }} </h2>
        </div>
        <nav class="brnad-nav-links">
          <ul class="one_ul">
            <li class="brand_li"><a href="#/">Головна</a></li>
            <li class="dropdown brand_li">
              <p href="#/products_page">Автомобілі</p>
              <ul class="brands-menu" > 
                <li v-for="item in brands" :key="item.brand_name" class="types_li">
                  <a :href="`#/brands/${selectedCategoryId}`" @click="selectCategory(item.id)">{{ item.brand_name }}</a>
                </li>
              </ul>
            </li>
            <li class="brand_li"><a href="#/company_information">Інформація</a></li>
          </ul>
        </nav>
        <searchPage />
      </div>
      </div>
  </header>
</template>

<script>
import axios from 'axios';
import '@fortawesome/fontawesome-free/css/all.css';
import searchPage from './searchPage.vue';

export default {
  components: {
        searchPage
  },
  data() {
    return {
      showResults: false,
      headIn: [],
      brands: [],
      showDropdown: false,
      selectedCategoryId: null,
    };
  },
  mounted() {
    axios.get(`${process.env.VUE_APP_BACKEND_URL}/home/`)
      .then((response) => {
        this.headIn = response.data.company_info;
        this.brands = response.data.car_brand_name_info;
      })
      .catch((error) => {
        console.log(error);
      });
  },
  computed: {
    filteredCategoryItems() {
      return this.brands.filter(item => item.id === this.selectedCategoryId);
    }},
  methods: {
    selectCategory(categoryId) {
      this.selectedCategoryId = categoryId;
      window.location.href = `#/brands/${categoryId}`;
    },
    phoneNumberCha(phoneNumber) {
      return `${phoneNumber.slice(0, 3)} (${phoneNumber.slice(3, 6)}) ${phoneNumber.slice(6, 9)}-${phoneNumber.slice(9, 11)}-${phoneNumber.slice(11)}`
    },
    toggleDropdown() {
      this.dropdownVisible = !this.dropdownVisible;
    }
  }
};
</script>
<style>
.name-titles {
  color: #1572D3;
}
.up__right-email {
  margin: 15px 0 0!important;
  padding-top: 25px;
}
.dropdown {
  display: inline-block;
}
.brands-menu {
  background-color: #051C34;
  border-radius: 15px;
  display: none;
  position: absolute;
  left: -60px;
  top: 45px;
  padding-bottom: 10px
}
.brands-menu .types_li {
  list-style: none;
  margin: 30px 40px 20px 0;
  width: 150px;
  text-align: center;
}
.brand_li a {
  text-decoration: none;
  color: black
}
.types_li a {
  color: #ebebeb;
}
.headIn__class {
  margin: 0 auto;
}
.headIn__class-up {
  display: flex;
  justify-content: center;
  align-items: center;
}
.up__left {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 275px;
}
.up__left img {
  margin-right: 20px;
}
.up__left h2 {
  color: #1572D3;
}
.gap-i {
  margin-right: 10px;
}
.up__right {
  text-align: right;
  width: 375px;
}
.up__right div {
  margin: 10px 0;
}
.up__midd img {
  width: 300px;
  height: 200px;
  object-fit: cover;
}
.headIn__class-bot {
  background-color: #1572D3;
}
.brnad-nav-links {
  z-index: 100;
}
.brnad-nav-links .one_ul {
  display: flex;
  list-style: none;
  justify-content: center;
  padding: 0;
  margin: 5px 20px 0;
}
.brnad-nav-links .one_ul .brand_li {
  margin: 10px 30px;
  position: relative;
  padding: 10px
}
.brnad-nav-links .dropdown:hover .brands-menu {
  display: block;
}
.brnad-nav-links p{
  margin: 0;
  font-family: 'Montserrat';
  text-decoration: none;
  font-size: 20px;
  font-weight: bold;
  padding: 0;
  border-radius: 5px;
}
.brnad-nav-links a {
  margin: 0;
  font-family: 'Montserrat';
  text-decoration: none;
  font-size: 20px;
  font-weight: bold;
  padding: 10px 20px;
  border-radius: 5px;
}
.brnad-nav-links a:hover {
  color: #1572D3;
  background-color: #ebebeb;
}
</style>