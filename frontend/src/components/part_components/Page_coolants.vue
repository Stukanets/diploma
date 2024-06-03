<template>
  <div class="background-car">
    <div class="info-container">
      <h1 class="name_for">Охолоджувальні рідини</h1>
      <div v-for="(filter, index) in coolants" :key="index" class="container-cards">
        <div v-for="(detail, detailIndex) in filter" :key="detailIndex" class="container-details">
          <div class="container-names"> 
            <h2>{{ detail.coolant_name }}</h2>
          </div>
          <div class="container-image">
            <img :src="getPhoto(detail)" alt="Cabin Filter Photo" class="contain-image">
          </div>
          <div class="container-type">
            <p>Колір: {{ detail.coolant_color }}</p>
          </div>
          <div class="container-brands">
            <p>Марка: {{ detail.coolant_brand }}</p>
          </div>
          <div class="container-description">
            <p>{{ detail.coolant_description }}</p>
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
      coolants: [],
      loading: true,
    };
  },
  created() {
    this.fetchCabinFilters();
  },
  methods: {
    getPhoto(detail) {
      try {
        const photoPath = detail.coolant_image.split('/images/Coolants/')[1];
        const fileName = photoPath.split('/').pop();
        return require(`@/../../backend/images/Coolants/${fileName}`);
      } catch (error) {
        console.error('Error loading photo:', error);
        return '';
      }
    },
    fetchCabinFilters() {
      const data = JSON.parse(localStorage.getItem('userInfo'));
      console.log(data);
      axios
        .post(`${process.env.VUE_APP_BACKEND_URL}/selected_coolants/`, data)
        .then(response => {
          this.coolants = { ...response.data };
          console.log(this.coolants);
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
  height: 450px;
  object-fit: contain;
}
</style>