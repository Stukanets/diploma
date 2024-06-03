<template>
  <div class="background-car">
    <div class="info-container">
      <h1 class="name_for">Повітряні фільтри</h1>
      <div v-for="(filter, index) in airFilters" :key="index" class="container-cards">
        <div v-for="(detail, detailIndex) in filter" :key="detailIndex" class="container-details">
          <div class="container-names"> 
            <h2>{{ detail.air_filter_name }}</h2>
          </div>
          <div class="container-image">
            <img :src="getPhoto(detail)" alt="Cabin Filter Photo" class="contain-image">
          </div>
          <div class="container-type">
            <p>Тип: {{ detail.air_filter_type }}</p>
          </div>
          <div class="container-brands">
            <p>Марка: {{ detail.air_filter_brand }}</p>
          </div>
          <div class="container-description">
            <p>{{ detail.air_filter_description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      airFilters: [],
      loading: true,
    };
  },
  created() {
    this.fetchCabinFilters();
  },
  methods: {
    fetchCabinFilters() {
      const data = JSON.parse(localStorage.getItem('userInfo'));
      console.log(data);
      axios
        .post(`${process.env.VUE_APP_BACKEND_URL}/selected_air_filters/`, data)
        .then(response => {
          this.airFilters = { ...response.data };
          console.log(this.airFilters);
        })
        .catch(error => {
          console.log('Error fetching cabin filters:', error);
        })
        .finally(() => {
          this.loading = false;
        });
    },
    getPhoto(detail) {
      try {
        const photoPath = detail.air_filter_image.split('/images/AirFilters/')[1];
        const fileName = photoPath.split('/').pop();
        return require(`@/../../backend/images/AirFilters/${fileName}`);
      } catch (error) {
        console.error('Error loading photo:', error);
        return '';
      }
    },
  },
};
</script>

<style>
.container-cards {
  display: flex;
  flex-wrap: wrap;
  width: 1200px;
  margin: 0 auto;
  font-size: 18px;
  gap: 40px;
}
.name_for {
  font-size: 28px;
  margin-bottom: 20px;
  width: 100%;
  text-align: center;
  font-style: normal;
  font-weight: 500;
  font-size: 38px;
  line-height: 150%;
  color: #333333;
}
.container-details {
  width: calc(45%);
  background-color: #fff;
  padding: 20px;
  margin-bottom: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  height: auto;
}
.container-details:nth-child(3n+1), .container-details:nth-child(3n) {
  margin-left: auto;
  margin-right: auto;
}
.container-names h2 {
  font-size: 32px;
  font-weight: 500;
  text-align: center;
  margin: 0;
  color: #5a5a5a;
}
.container-type,
.container-brands {
  margin-bottom: 10px;
  color: #000000;
  text-align: justify;
}
.container-description {
  margin-bottom: 10px;
  color: #5f5f5f;
  text-align: justify;
}
.container-image {
  display: flex;
  justify-content: center;
}
.contain-image {
  width: 400px;
}
</style>
