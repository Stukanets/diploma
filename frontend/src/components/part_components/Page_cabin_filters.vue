<template>
  <div class="background-car">
    <div class="info-container">
      <h1 class="name_for">Фільтри салону</h1>
      <div v-for="(filter, index) in cabinFilters" :key="index" class="container-cards">
        <div v-for="(detail, detailIndex) in filter" :key="detailIndex" class="container-details">
          <div class="container-names"> 
            <h2>{{ detail.cabin_filter_name }}</h2>
          </div>
          <div class="container-image">
            <img :src="getPhoto(detail)" alt="Cabin Filter Photo" class="contain-image">
          </div>
          <div class="container-type">
            <p>Тип: {{ detail.cabin_filter_type }}</p>
          </div>
          <div class="container-brands">
            <p>Марка: {{ detail.cabin_filter_brand }}</p>
          </div>
          <div class="container-description">
            <p>{{ detail.cabin_filter_description }}</p>
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
      cabinFilters: [],
      loading: true,
    };
  },
  created() {
    this.fetchCabinFilters();
  },
  methods: {
    getPhoto(detail) {
      try {
        const photoPath = detail.cabin_filter_image.split('/images/CabinFilters/')[1];
        const fileName = photoPath.split('/').pop();
        return require(`@/../../backend/images/CabinFilters/${fileName}`);
      } catch (error) {
        console.error('Error loading photo:', error);
        return '';
      }
    },
    fetchCabinFilters() {
      const data = JSON.parse(localStorage.getItem('userInfo'));
      console.log(data);
      axios
        .post(`${process.env.VUE_APP_BACKEND_URL}/selected_cabin_filters/`, data)
        .then(response => {
          this.cabinFilters = { ...response.data };
          console.log(this.cabinFilters);
        })
        .catch(error => {
          console.log('Error fetching cabin filters:', error);
        })
        .finally(() => {
          this.loading = false;
        });
    },
  },
};
</script>

<style>
.container-image {
  display: flex;
  justify-content: center;
}
.contain-image {
  width: 400px;
}
</style>